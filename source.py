from datetime import datetime, time
from dateutil import parser


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return begin_time <= check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time


api_input = {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}

cart_value = api_input['cart_value'] / 100


total_fee = 0
free_delivery = False

if cart_value > 100:
    free_delivery = True
    total_fee = 0
else:
    if cart_value < 10:
        total_fee += 10 - cart_value

    print('Fee:', total_fee)

    if api_input['delivery_distance'] <= 1000:
        total_fee += 2
    elif api_input['delivery_distance'] > 1000:
        total_fee += 2
        total_fee += ((api_input['delivery_distance'] - 1000) // 500) + 1
    print('Fee:', total_fee)

    if api_input['number_of_items'] >= 5:
        total_fee += ((api_input['number_of_items'] - 4) * 50) / 100
    print('Fee:', total_fee)

    if api_input['number_of_items'] >= 12:
        total_fee += 1.2 * total_fee
    print('Fee:', total_fee)

    date = parser.parse(api_input['time'])

    if date.weekday() == 4 and is_time_between(time(15, 00), time(19, 00), date.time()):
        print("Yes, It's Friday Peak")
        total_fee = 1.2 * total_fee
    print('Fee:', total_fee)

if not free_delivery:
    total_fee = min(15, total_fee)

print(total_fee * 100)
