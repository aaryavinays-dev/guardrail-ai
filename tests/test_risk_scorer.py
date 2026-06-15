import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from risk_scorer import RiskScorer


def test_calculate_score_for_ssn_detection():
    risk_weights = {
        "ssn": 50
    }

    detections = {
        "ssn": True
    }

    risk_scorer = RiskScorer(risk_weights, 50)

    risk_score, risk_reasons = risk_scorer.calculate_score(detections)

    assert risk_score == 50
    assert risk_reasons == ["ssn detected"]

def test_calculate_score_no_detections():
    risk_weights = {
        "ssn": 50
    }

    detections = {
        "ssn": False
    }

    risk_scorer = RiskScorer(risk_weights, 50)

    risk_score, risk_reasons = risk_scorer.calculate_score(detections)

    assert risk_score == 0
    assert risk_reasons == []

def test_determine_risk_level_high():
    risk_scorer = RiskScorer({}, 50)

    risk_level = risk_scorer.determine_risk_level(70)

    assert risk_level == "HIGH"