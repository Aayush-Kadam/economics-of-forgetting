import math


def hard_access(reputation: float, threshold: float = 0.5) -> float:
    return float(reputation >= threshold)


def logistic_access(reputation: float, threshold: float = 0.5, slope: float = 6.0) -> float:
    z = max(-700.0, min(700.0, slope * (reputation - threshold)))
    return 1.0 / (1.0 + math.exp(-z))


def linear_access(reputation: float, intercept: float = 0.25, slope: float = 0.5) -> float:
    return max(0.0, min(1.0, intercept + slope * reputation))


def constant_access(_: float, level: float = 0.5) -> float:
    return level

