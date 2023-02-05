from datetime import time
import json
from dateutil import parser
import requests

from delivery_fee import DeliveryFee


def test_api():
    """
    This is test for api.
    :return:
    """

    api_input = {"cart_value": 1200, "delivery_distance": 4536, "number_of_items": 6, "time": "2021-10-12T13:00:00Z"}
    response = requests.get("http://127.0.0.1:5000/delivery/", json=api_input).content.decode("utf-8")

    print(response)
    data = json.loads(response)
    print(data)

    assert data['delivery_fee'] == 1100

    api_input = {"cart_value": 3300, "delivery_distance": 5243, "number_of_items": 12, "time": "2023-02-03T16:00:00Z"}
    response = requests.get("http://127.0.0.1:5000/delivery/", json=api_input).content.decode("utf-8")

    print(response)
    data = json.loads(response)
    print(data)

    assert data['delivery_fee'] == 1500


def test_is_time_between():
    """
    This is a test to check function 'is_time_between()'
    :return:
    """

    date = parser.parse('2021-01-16T16:00:00Z')
    assert DeliveryFee.is_time_between(time(15, 00), time(19, 00), date.time()) is True

    date = parser.parse('2021-01-16T13:00:00Z')
    assert DeliveryFee.is_time_between(time(15, 00), time(19, 00), date.time()) is False

    date = parser.parse('2021-01-16T14:59:00Z')
    assert DeliveryFee.is_time_between(time(15, 00), time(19, 00), date.time()) is False

    date = parser.parse('2021-01-16T03:00:00Z')
    assert DeliveryFee.is_time_between(time(15, 00), time(19, 00), date.time()) is False


def test_small_order_surcharge():
    """
    This is a test to check function 'small_order-surcharge()'
    :return:
    """

    assert DeliveryFee.small_order_surcharge(1000) == 0
    assert DeliveryFee.small_order_surcharge(999) == 1
    assert DeliveryFee.small_order_surcharge(800) == 200
    assert DeliveryFee.small_order_surcharge(1500) == 0
    assert DeliveryFee.small_order_surcharge(0) == 1000


def test_item_count_surcharge():
    """
    This is a test to check function 'item_count_surcharge()'
    :return:
    """

    assert DeliveryFee.item_count_surcharge(4) == 0
    assert DeliveryFee.item_count_surcharge(5) == 50
    assert DeliveryFee.item_count_surcharge(10) == 300
    assert DeliveryFee.item_count_surcharge(13) == 570


def test_distance_surcharge():
    """
    This is a test to check function 'distance_surcharge()'
    :return:
    """

    assert DeliveryFee.distance_surcharge(1499) == 300
    assert DeliveryFee.distance_surcharge(1500) == 300
    assert DeliveryFee.distance_surcharge(1501) == 400


def test_friday_peak():
    """
    This is a test to check function 'friday_peak()'
    :return:
    """

    assert DeliveryFee.is_friday_peak('2021-10-12T13:00:00Z') is False
    assert DeliveryFee.is_friday_peak('2023-02-03T16:00:00Z') is True
    assert DeliveryFee.is_friday_peak('2023-02-03T14:59:59Z') is False
    assert DeliveryFee.is_friday_peak('2022-11-25T15:00:00Z') is True
