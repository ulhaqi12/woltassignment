from delivery_fee import calculate_delivery_fee
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/delivery/', methods=['POST', 'GET'])
def delivery():

    api_input = request.json
    deliver_fee = {"delivery_fee": calculate_delivery_fee(api_input)}
    return jsonify(deliver_fee)


if __name__ == '__main__':
    app.run()

