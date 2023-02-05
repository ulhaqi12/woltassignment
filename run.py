import requests

# Change input values as per requirement.
api_input = {"cart_value": 3300, "delivery_distance": 5243, "number_of_items": 12, "time": "2023-02-03T16:00:00Z"}
response = requests.get("http://127.0.0.1:5000/delivery/", json=api_input)
print(response.content)
