from enums import Action, RiskLevel


class RiskScorer:
    def __init__(self, risk_weights: dict[str, int], risk_threshold: int) -> None:
        self.risk_weights = risk_weights
        self.risk_threshold = risk_threshold

    def calculate_score(self, detections: dict[str, bool]) -> tuple[int, list[str]]:
        risk_score = 0
        risk_reasons = []

        for detection_name, detected in detections.items():
            if detected:
                weight = self.risk_weights.get(detection_name, 0)
                risk_score += weight
                risk_reasons.append(f"{detection_name} detected")

        return risk_score, risk_reasons

    def determine_risk_level(self, risk_score: int) -> RiskLevel:
        if risk_score <= 20:
            return RiskLevel.LOW
        elif risk_score <= 50:
            return RiskLevel.MEDIUM
        elif risk_score < self.risk_threshold:
            return RiskLevel.HIGH
        else:
            return RiskLevel.CRITICAL

    def determine_action(self, risk_score: int) -> Action:
        if risk_score <= 20:
            return Action.ALLOW
        elif risk_score < self.risk_threshold:
            return Action.WARN
        else:
            return Action.BLOCK