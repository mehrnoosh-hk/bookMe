import datetime


class Interval:
    def __init__(self,
                 start: datetime.datetime,
                 end: datetime.datetime) -> None:
        self.start = start
        self.end = end
