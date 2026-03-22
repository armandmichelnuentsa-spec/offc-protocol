import numpy as np

class ValuationEngine:
    def __init__(self, currencies, weights):
        self.currencies = currencies
        self.weights = np.array(weights)

    def normalize_weights(self):
        self.weights = self.weights / np.sum(self.weights)

    def compute_offc(self, values):
        """
        values: list of currency values at time t
        """
        values = np.array(values)
        return np.dot(self.weights, values)

    def dynamic_adjustment(self, volatility):
        """
        volatility: list of volatility indexes per currency
        """
        alpha = 0.05
        mu = np.mean(volatility)

        adjustment = alpha * (mu - np.array(volatility))
        self.weights = self.weights + adjustment

        self.normalize_weights()
