import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from enums import Action, RiskLevel
from risk_scorer import RiskScorer
from scoring import risk_weights


def test_calculate_score_email_only():
    scorer = RiskScorer(risk_weights, 100)

    detections = {
        "email": True,
        "phone": False,
        "ssn": False,
        "credit_card": False,
        "password": False,
        "api_key": False,
        "prompt_injection": False,
    }

    risk_score, risk_reasons = scorer.calculate_score(detections)

    assert risk_score == 20
    assert "email detected" in risk_reasons


def test_determine_risk_level_low():
    scorer = RiskScorer(risk_weights, 100)

    risk_level = scorer.determine_risk_level(20)

    assert risk_level == "LOW"


def test_determine_risk_level_medium():
    scorer = RiskScorer(risk_weights, 100)

    risk_level = scorer.determine_risk_level(50)

    assert risk_level == "MEDIUM"


def test_determine_risk_level_high():
    scorer = RiskScorer(risk_weights, 100)

    risk_level = scorer.determine_risk_level(75)

    assert risk_level == "HIGH"


def test_determine_risk_level_critical():
    scorer = RiskScorer(risk_weights, 100)

    risk_level = scorer.determine_risk_level(100)

    assert risk_level == "CRITICAL"


def test_determine_action_allow():
    scorer = RiskScorer(risk_weights, 100)

    action = scorer.determine_action(20)

    assert action == "ALLOW"


def test_determine_action_warn():
    scorer = RiskScorer(risk_weights, 100)

    action = scorer.determine_action(50)

    assert action == "WARN"


def test_determine_action_block():
    scorer = RiskScorer(risk_weights, 100)

    action = scorer.determine_action(100)

    assert action == "BLOCK"