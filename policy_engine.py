def apply_department_policy(
    department: str,
    detections: dict[str, bool],
    current_action: str,
    risk_reasons: list[str],
) -> tuple[str, list[str]]:
    normalized_department = department.strip().lower()

    policy_reasons = []

    if normalized_department == "finance" and detections.get("ssn"):
        policy_reasons.append("finance policy blocks ssn usage")

    if normalized_department == "finance" and detections.get("credit_card"):
        policy_reasons.append("finance policy blocks credit card usage")

    if normalized_department == "engineering" and detections.get("api_key"):
        policy_reasons.append("engineering policy blocks api key exposure")

    if normalized_department == "hr" and detections.get("password"):
        policy_reasons.append("hr policy blocks password exposure")

    if detections.get("prompt_injection"):
        policy_reasons.append("global policy blocks prompt injection attempt")

    if policy_reasons:
        updated_action = "BLOCK"
    else:
        updated_action = current_action

    updated_risk_reasons = risk_reasons + policy_reasons

    return updated_action, updated_risk_reasons