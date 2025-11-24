import numpy as np

class Gaussian():
    def __init__(self, name: str, mean: float, std_dev: float):
        self.name = name
        self.mean = mean
        self.std_dev = std_dev

    def sample(self) -> float:
        return np.random.normal(loc=self.mean, scale=self.std_dev)
    
class LaneStats():
    def __init__(self, speed_std_devs: list[tuple[int, float]]) -> None:

        self.lane_stats: list[Gaussian] = [Gaussian(name=f"lane {i}", mean=x[0], std_dev=x[1]) for i, x in enumerate(speed_std_devs)]

    def get_sample(self, lane_idx: int) -> float:
        return self.lane_stats[lane_idx].sample()
    
    def get_speed_prefs(self) -> list[float]:
        speed_prefs = []
        for i in range(len(self.lane_stats)):
            speed_prefs.append(self.get_sample(i))

        return speed_prefs