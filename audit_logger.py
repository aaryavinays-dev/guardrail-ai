from datetime import datetime


def save_audit_log(prompt, risk_score, risk_level, action, risk_reasons):
    timestamp = datetime.now()

    with open("audit_log.txt", "a") as file:
        file.write("--------------------------------------------------\n")
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Prompt: {prompt}\n")
        file.write(f"Risk Score: {risk_score}\n")
        file.write(f"Risk Level: {risk_level}\n")
        file.write(f"Action: {action}\n")
        file.write(f"Risk Reasons: {risk_reasons}\n")
        file.write("--------------------------------------------------\n\n")