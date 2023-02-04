import requests

# Change input values as per requirement.
api_input = {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
response = requests.get("http://127.0.0.1:5000/delivery/", json=api_input)
print(response.content)
