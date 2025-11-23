from core.car import Car
from core.stats import Gaussian


class Lane():
    def __init__(self, speed_lim: int):
        self.speed_lim = speed_lim
        self.global_stats = Gaussian(name="average speed distribution", mean=self.speed_lim, std_dev=10)
        self.cars: list[Car] = []

    def add_car(self, )