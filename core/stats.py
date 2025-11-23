import numpy as np

class Gaussian():
    def __init__(self, name: str, mean: float, std_dev: float):
        self.name = name
        self.mean = mean
        self.std_dev = std_dev

    def sample(self) -> float:
        return np.random.normal(loc=self.mean, scale=self.std_dev)