
api_input = {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}

cart_value = api_input['cart_value'] / 100
fee_distance = 0

sub_charge = 0

if cart_value < 10:
    sub_charge += 10 - cart_value

if api_input['delivery_distance'] <= 1000:
    fee_distance += 2
elif api_input['delivery_distance'] > 1000:
    fee_distance += 2
    fee_distance += ((api_input['delivery_distance'] - 1000) // 500) + 1



