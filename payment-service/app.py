from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'Payment Service is running'})

@app.route('/payments', methods=['GET'])
def get_payments():
    return jsonify([
        {'id': 1, 'orderId': 1, 'amount': 999.99, 'status': 'completed'},
        {'id': 2, 'orderId': 2, 'amount': 29.99, 'status': 'completed'}
    ])

@app.route('/payments', methods=['POST'])
def create_payment():
    return jsonify({'message': 'Payment processed', 'data': request.json}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
