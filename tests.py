from datetime import time
from dateutil import parser

from delivery_fee import is_time_between, small_order_surcharge, item_count_surcharge, distance_surcharge, \
    is_friday_peak


def test_is_time_between():

    date = parser.parse('2021-01-16T16:00:00Z')
    assert is_time_between(time(15, 00), time(19, 00), date.time()) is True

    date = parser.parse('2021-01-16T13:00:00Z')
    assert is_time_between(time(15, 00), time(19, 00), date.time()) is False

    date = parser.parse('2021-01-16T14:59:00Z')
    assert is_time_between(time(15, 00), time(19, 00), date.time()) is False

    date = parser.parse('2021-01-16T03:00:00Z')
    assert is_time_between(time(15, 00), time(19, 00), date.time()) is False


def test_small_order_surcharge():

    assert small_order_surcharge(1000) == 0
    assert small_order_surcharge(999) == 1
    assert small_order_surcharge(800) == 200
    assert small_order_surcharge(1500) == 0
    assert small_order_surcharge(0) == 1000


def test_item_count_surcharge():

    assert item_count_surcharge(4) == 0
    assert item_count_surcharge(5) == 50
    assert item_count_surcharge(10) == 300
    assert item_count_surcharge(13) == 570


def test_distance_surcharge():

    assert distance_surcharge(1499) == 300
    assert distance_surcharge(1500) == 300
    assert distance_surcharge(1501) == 400


def test_friday_peak():

    assert is_friday_peak('2021-10-12T13:00:00Z') is False
    assert is_friday_peak('2023-02-03T16:00:00Z') is True
    assert is_friday_peak('2023-02-03T14:59:59Z') is False
    assert is_friday_peak('2022-11-25T15:00:00Z') is True
