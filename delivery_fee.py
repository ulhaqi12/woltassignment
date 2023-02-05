from datetime import datetime, time
from dateutil import parser


class DeliveryFee:

    @staticmethod
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

    @staticmethod
    def small_order_surcharge(cart_value):
        """
        Function calculates the fee on smaller orders based on Price.
        :param cart_value: Price of total items currently in the cart
        :return: fee for small order
        """

        if cart_value < 1000:
            return 1000 - cart_value
        return 0

    @staticmethod
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

            extra = (distance - 1000) // 500 + 1
            if (distance - 1000) % 500 == 0:
                extra -= 1
            distance_fee += extra * 100

        return distance_fee

    @staticmethod
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
            item_count_fee += 120

        return item_count_fee

    @staticmethod
    def is_friday_peak(order_time):
        """
        Function calculates the additional fee if the order is placed at peak times on Friday.
        :param order_time: Date and time of order
        :return: Surcharge if order is placed in peak time on Friday.
        """

        date = parser.parse(order_time)

        if date.weekday() == 4 and DeliveryFee.is_time_between(time(15, 00), time(19, 00), date.time()):
            return True
        return False

    @staticmethod
    def calculate_delivery_fee(api_input):
        """
        Function takes input the information about the delivery and calculates the delivery fee using utility functions.
        :param api_input: This dictionary variable contains the information about delivery.
        :return:
        """

        total_fee = 0
        wrong_input = False

        if api_input['cart_value'] < 0 or api_input['delivery_distance'] < 0 or api_input['number_of_items'] < 0:
            wrong_input = True

        try:
            parser.parse(api_input['time'])
        except Exception as e:
            wrong_input = True

        if wrong_input:
            return 'Bad Input'

        if api_input['cart_value'] > 10000:
            total_fee = 0
        else:
            total_fee += DeliveryFee.small_order_surcharge(api_input['cart_value'])
            total_fee += DeliveryFee.distance_surcharge(api_input['delivery_distance'])
            total_fee += DeliveryFee.item_count_surcharge(api_input['number_of_items'])
            if DeliveryFee.is_friday_peak(api_input['time']):
                total_fee = total_fee * 1.2

        return min(1500, total_fee)
