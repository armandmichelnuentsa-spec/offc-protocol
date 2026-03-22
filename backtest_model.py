import numpy as np

class OFFCBacktest:
    def __init__(self, engine):
        self.engine = engine

    def run_simulation(self, dataset):
        results = []

        for timestep in dataset:
            values = timestep["values"]
            volatility = timestep["volatility"]

            self.engine.dynamic_adjustment(volatility)
            offc_value = self.engine.compute_offc(values)

            results.append(offc_value)

        return results

    def stress_test(self, dataset, shock_factor=2.5):
        shocked = []

        for t in dataset:
            values = [v * shock_factor for v in t["values"]]
            shocked.append(values)

        return self.run_simulation([{"values": v, "volatility": [1]*len(v)} for v in shocked])
