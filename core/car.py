from __future__ import annotations

from typing import Literal
import numpy as np

from core.stats import Gaussian

class Car:
    def __init__(self, id: int, lane: int, position: float, ahead: Car, behind: Car, speed_lim: int, acc: float, num_lanes: int, global_stats: Gaussian):
        self.id = id
        self.lane = lane
        self.position = position
        self.ahead = ahead
        self.behind = behind
        self.speed_lim = speed_lim
        self.num_lanes = num_lanes
        self.global_stats = global_stats
        self.status: Literal["steady", "passing", "exiting"]
        self.mode: Literal["speed", "distance"] | None = None
        self.speed: float | None = None

        self.acc = acc

        # get random speed preferences SIMPLIFIED VERSION FOR NOW
        self.speed_pref = [self.global_stats.sample() + i*5.0 for i in range(self.num_lanes)]
        self.speed_tol = np.random.uniform(low=0.0, high=10.0) # use uniform for now

        self.switch_dist = 50 # SIMPLIFIED VERSION FOR NOW

        # get random following distance preference SIMIPLIFIED VERSION FOR NOW
        self.lamda = [np.random.exponential(scale=1/(self.speed)) if self.speed is not None else None for i in range(self.num_lanes)]

        self.init_v: float | None = None
        self.init_l: float | None = None
        self.init_v_rel: float| None = None

    def get_following_dist(self) -> float:

        return self.ahead.position - self.position
    
    def get_relative_speed(self) -> float:
        return self.ahead.speed - self.speed
    
    def update_mode(self) -> None:
        fol_dist = self.get_following_dist()

        if fol_dist > self.switch_dist:
            self.mode = "speed"
            self.init_v = self.speed
        else:
            self.mode = "distance"
            self.init_l = self.get_following_dist()
            self.init_v_rel = self.get_relative_speed()
