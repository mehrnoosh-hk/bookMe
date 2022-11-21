import datetime
from core.interval import Interval

class Event:
    def __init__(self, name: str) -> None:
        self.name = name
        self.intervals = []

    def add_date_time(self, interval: Interval):
        self.intervals.append(interval)
