from datetime import datetime
import json
import os


def save_audit_log(prompt, risk_score, risk_level, action, risk_reasons):
    timestamp = datetime.now()

    audit_record = {
        "timestamp": str(timestamp),
        "prompt": prompt,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "action": action,
        "risk_reasons": risk_reasons
    }

    audit_log_file = "logs/audit_log.json"

    if os.path.exists(audit_log_file):
        with open(audit_log_file, "r") as file:
            audit_logs = json.load(file)
    else:
        audit_logs = []

    audit_logs.append(audit_record)

    with open(audit_log_file, "w") as file:
        json.dump(audit_logs, file, indent=4)