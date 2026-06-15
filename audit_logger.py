from datetime import datetime
import json
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AuditLogger:
    def __init__(self, audit_log_file):
        self.audit_log_file = audit_log_file

    def load_logs(self):
        print("LOAD_LOGS CALLED")
        if not os.path.exists(self.audit_log_file):
            return []

        try:
            with open(self.audit_log_file, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
               print("JSON FILE IS CORRUPTED")
               logger.error("Audit log JSON file is corrupted")
               return []
               

    def save(self, prompt, risk_score, risk_level, action, risk_reasons):
        timestamp = datetime.now()

        audit_record = {
            "timestamp": str(timestamp),
            "prompt": prompt,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "action": action,
            "risk_reasons": risk_reasons
        }

        audit_logs = self.load_logs()
        audit_logs.append(audit_record)

        try:
            with open(self.audit_log_file, "w") as file:
                json.dump(audit_logs, file, indent=4)
        except OSError:
            logger.error("Failed to write audit log")
            return {
                "error": "Failed to write audit log"
            }

    