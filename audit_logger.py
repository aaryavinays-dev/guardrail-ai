from datetime import datetime, timezone
import json
import logging
import os
from typing import Any

from redactor import redact_prompt


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AuditLogger:
    def __init__(self, audit_log_file: str) -> None:
        self.audit_log_file = audit_log_file

    def _ensure_log_directory_exists(self) -> None:
        log_directory = os.path.dirname(self.audit_log_file)

        if log_directory:
            os.makedirs(log_directory, exist_ok=True)

    def load_logs(self) -> list[dict[str, Any]]:
        if not os.path.exists(self.audit_log_file):
            return []

        try:
            with open(self.audit_log_file, "r", encoding="utf-8") as file:
                audit_logs = json.load(file)

                if isinstance(audit_logs, list):
                    return audit_logs

                logger.error("Audit log file does not contain a valid list")
                return []

        except json.JSONDecodeError:
            logger.error("Audit log JSON file is corrupted")
            return []

        except OSError as error:
            logger.error("Failed to read audit log file: %s", error)
            return []

    def save(
        self,
        prompt: str,
        risk_score: int,
        risk_level: str,
        action: str,
        risk_reasons: list[str],
    ) -> None:
        self._ensure_log_directory_exists()

        redacted_prompt = redact_prompt(prompt)

        audit_record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "prompt": redacted_prompt,
            "prompt_redacted": True,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "action": action,
            "risk_reasons": risk_reasons,
        }

        audit_logs = self.load_logs()
        audit_logs.append(audit_record)

        try:
            with open(self.audit_log_file, "w", encoding="utf-8") as file:
                json.dump(audit_logs, file, indent=4)

            logger.info("Audit log saved successfully")

        except OSError as error:
            logger.error("Failed to write audit log file: %s", error)