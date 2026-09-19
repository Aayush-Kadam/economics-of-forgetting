from dataclasses import dataclass


@dataclass(frozen=True)
class BaselineParameters:
    phi: float = 0.8
    rho: float = 0.7
    alpha: float = 0.8
    beta: float = 0.95
    kappa: float = 1.0
    value: float = 2.0
    threshold: float = 0.5
    logistic_slope: float = 6.0
    horizon: int = 3

    def validate(self) -> None:
        if not 0 <= self.phi <= 1:
            raise ValueError("phi must lie in [0, 1]")
        if not 0 <= self.rho <= 1:
            raise ValueError("rho must lie in [0, 1]")
        if self.alpha < 0 or not 0 < self.beta < 1 or self.kappa <= 0:
            raise ValueError("invalid technology, discount, or cost parameter")
        if self.horizon < 1:
            raise ValueError("horizon must be positive")

