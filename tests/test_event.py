import datetime

from core import event
from core.interval import Interval


def test_create_event() -> None:
    my_event = event.Event("Interview")
    assert my_event.name == "Interview"


def test_add_date_time_interval_to_event() -> None:
    my_event = event.Event("Test_Event")
    first_interval = Interval(
        start=datetime.datetime(2022, 11, 24),
        end=datetime.datetime(2022, 11, 30)
    )
    my_event.add_date_time(first_interval)
