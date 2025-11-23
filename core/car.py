from typing import Literal
import numpy as np

from core.stats import Gaussian

class Car:
    def __init__(self, id: int, lane: int, speed_lim: int, acc: float, num_lanes: int, global_stats: Gaussian):
        self.id = id
        self.lane = lane
        self.speed_lim = speed_lim
        self.num_lanes = num_lanes
        self.global_stats = global_stats
        self.mode: Literal["traveling", "exiting"]
        self.speed: float | None = None

        self.acc = acc

        # get random speed preferences SIMPLIFIED VERSION FOR NOW
        self.speed_pref = [self.global_stats.sample() + i*5.0 for i in range(self.num_lanes)]
        self.speed_tol = np.random.uniform(low=0.0, high=10.0) # use uniform for now

        # get random following distance preference SIMIPLIFIED VERSION FOR NOW
        self.lamda = [np.random.exponential(scale=1/(self.speed)) if self.speed is not None else None for i in range(self.num_lanes)]