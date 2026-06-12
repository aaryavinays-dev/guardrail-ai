class RiskScorer:
    def __init__(self, risk_weights, risk_threshold):
        self.risk_weights = risk_weights
        self.risk_threshold = risk_threshold

    def calculate_score(self, detections):
        risk_score = 0
        risk_reasons = []

        for detection_name, detected in detections.items():
            if detected:
                risk_score += self.risk_weights[detection_name]
                risk_reasons.append(f"{detection_name} detected")

        return risk_score, risk_reasons

    def determine_risk_level(self, risk_score):
        if risk_score <= 20:
            return "LOW"
        elif risk_score <= 50:
            return "MEDIUM"
        elif risk_score <= 99:
            return "HIGH"
        else:
            return "CRITICAL"