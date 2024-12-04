from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received data: {data}")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)
