from core.interval import Interval


class Event:
    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError("Event only accepts strings as name")
        self.name = name
        self.intervals: list[Interval] = []

    def add_date_time(self, interval: Interval) -> None:
        self.intervals.append(interval)
