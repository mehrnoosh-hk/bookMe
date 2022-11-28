import datetime

import pytest

from core import event
from core.interval import Interval


class TestEvent:

    def test_create_event(self) -> None:
        my_event = event.Event("Interview")
        assert my_event.name == "Interview"

    def test_create_event_with_incorrect_value(self) -> None:
        with pytest.raises(ValueError) as ve:
            my_event = event.Event(38)
        assert ve.value.args[0] == "Event only accepts strings as name"

    def test_add_date_time_interval_to_event(self) -> None:
        my_event = event.Event("Test_Event")
        first_interval = Interval(
            start=datetime.datetime(2022, 11, 24),
            end=datetime.datetime(2022, 11, 30)
        )
        my_event.add_date_time(first_interval)


    def test_add_date_time_with_incorrect_value(self) -> None:
        my_event = event.Event("Test_Event")
        with pytest.raises(TypeError) as te:
            my_event.add_date_time("Friday")
        assert te.value.args[0] == "You can only add time intervals"