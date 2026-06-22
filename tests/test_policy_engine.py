from policy_engine import apply_department_policy


def test_finance_ssn_policy_blocks_prompt():
    detections = {
        "ssn": True,
        "credit_card": False,
        "api_key": False,
        "password": False,
        "prompt_injection": False,
    }

    action, reasons = apply_department_policy(
        department="Finance",
        detections=detections,
        current_action="WARN",
        risk_reasons=["ssn detected"],
    )

    assert action == "BLOCK"
    assert "finance policy blocks ssn usage" in reasons


def test_engineering_api_key_policy_blocks_prompt():
    detections = {
        "ssn": False,
        "credit_card": False,
        "api_key": True,
        "password": False,
        "prompt_injection": False,
    }

    action, reasons = apply_department_policy(
        department="Engineering",
        detections=detections,
        current_action="WARN",
        risk_reasons=["api_key detected"],
    )

    assert action == "BLOCK"
    assert "engineering policy blocks api key exposure" in reasons


def test_safe_prompt_keeps_current_action():
    detections = {
        "ssn": False,
        "credit_card": False,
        "api_key": False,
        "password": False,
        "prompt_injection": False,
    }

    action, reasons = apply_department_policy(
        department="Marketing",
        detections=detections,
        current_action="ALLOW",
        risk_reasons=[],
    )

    assert action == "ALLOW"
    assert reasons == []