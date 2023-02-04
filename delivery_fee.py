from datetime import datetime, time
from dateutil import parser


def is_time_between(begin_time, end_time, check_time=None):
    """
    Function calculates that a given time is in provided range that is (begin_time, end_time).
    If time is not provided it checks it for current time.
    :param begin_time: start time of window.
    :param end_time: end time of window.
    :param check_time: time need to be checked if it lies in the window.
    :return: True if time is in window else False
    """
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return begin_time <= check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time


def small_order_surcharge(cart_value):
    """
    Function calculates the fee on smaller orders based on Price.
    :param cart_value: Price of total items currently in the cart
    :return: fee for small order
    """

    if cart_value < 1000:
        return 1000 - cart_value
    return 0


def distance_surcharge(distance):
    """
    Function calculates the fee based on the distance of delivery.
    :param distance: distance of the delivery
    :return: fee based on the distance for delivery
    """

    distance_fee = 0
    if distance <= 1000:
        distance_fee += 200
    elif distance > 1000:
        distance_fee += 200
        distance_fee += (((distance - 1000) // 500) + 1) * 100

    return distance_fee


def item_count_surcharge(number_of_items):
    """
    Function calculates the increment in delivery fee based on the count of items.
    :param number_of_items: Number of items in the cart
    :return: Fee based on the number of items in the cart
    """

    item_count_fee = 0
    if number_of_items >= 5:
        item_count_fee += ((number_of_items - 4) * 50)

    if number_of_items >= 12:
        item_count_fee += 1.2 * item_count_fee

    return item_count_fee


def friday_peak_surcharge(order_time):
    """
    Function calculates the additional fee if the order is placed at peak times on Friday.
    :param order_time: Date and time of order
    :return: Surcharge if order is placed in peak time on Friday.
    """
    time_fee = 0

    date = parser.parse(order_time)

    if date.weekday() == 4 and is_time_between(time(15, 00), time(19, 00), date.time()):
        time_fee = 1.2 * time_fee
    return time_fee


def calculate_delivery_fee(api_input):
    total_fee = 0

    if api_input['cart_value'] > 10000:
        total_fee = 0
    else:
        total_fee += small_order_surcharge(api_input['cart_value'])
        total_fee += distance_surcharge(api_input['delivery_distance'])
        total_fee += item_count_surcharge(api_input['number_of_items'])
        total_fee += friday_peak_surcharge(api_input['time'])

    return min(1500, total_fee)
