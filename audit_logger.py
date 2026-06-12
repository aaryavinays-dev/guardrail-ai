from datetime import datetime
import json
import os


class AuditLogger:
    def __init__(self, audit_log_file):
        self.audit_log_file = audit_log_file

    def load_logs(self):
        if os.path.exists(self.audit_log_file):
            with open(self.audit_log_file, "r") as file:
                return json.load(file)
        else:
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

        with open(self.audit_log_file, "w") as file:
            json.dump(audit_logs, file, indent=4)