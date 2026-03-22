import numpy as np

class ValuGuard:
    def __init__(self, sensitivity=0.7):
        self.sensitivity = sensitivity

    def filter_shock(self, offc_value, volatility_index):
        """
        Applies nonlinear damping to extreme volatility.
        """
        damping_factor = np.exp(-self.sensitivity * volatility_index)
        return offc_value * damping_factor

    def systemic_balance(self, basket_vector):
        """
        Stabilizes extreme divergence in currency contributions.
        """
        mean = np.mean(basket_vector)
        return [mean + (x - mean) * 0.5 for x in basket_vector]
