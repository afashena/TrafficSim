from uuid import UUID
from core.car import Car
from core.stats import LaneStats


class Lane():
    def __init__(self, id: int, speed_lim: int, lane_stats: LaneStats):
        self.id = id
        self.speed_lim = speed_lim
        self.lane_stats = lane_stats
        self.cars: list[Car] = []

    def add_car(self) -> None:
        """Add a car to this lane."""
        self.cars.append(Car(lane=self.id, position=0.0, ahead=self.cars[-1], behind=None, speed_lim=self.speed_lim, lane_stats = self.lane_stats))

    def remove_car(self, car_id: UUID) -> None:
        """A car exits from this lane."""
        # get car with this UUID, then remove

    def update(self) -> None:
        for car in self.cars:
            car.update_mode()
            car.update_status()

class Road():
    def __init__(self, num_lanes: int, speed_lim: int, speed_std_devs: list[tuple[int, float]], dt: float) -> None:
        self.num_lanes = num_lanes
        self.speed_lim = speed_lim
        self.lane_stats = LaneStats(speed_std_devs=speed_std_devs)
        self.lanes = [Lane(id=i, speed_lim=self.speed_lim, lane_stats=self.lane_stats) for i in range(self.num_lanes)]
        self.dt = dt

    def add_car(self) -> None:
        """Add a car to the right lane (id=0)."""
        self.lanes[0].add_car()

    def remove_car(self, car_id: UUID) -> None:
        """Remove a car from the right lane (id=0), a car exits."""
        self.lanes[0].remove_car(car_id)

    def update_cars(self) -> None:
        for lane in self.lanes:
            lane.update()

    def update_positions(self) -> None:
        return

    def timestep(self) -> None:
        """Increments time by self.dt, updating cars positions, lanes, modes, and statuses"""
        # function for computing next position/lane
        self.update_positions()

        self.update_cars()

        # function to visualize

        return