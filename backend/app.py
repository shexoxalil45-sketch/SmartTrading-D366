from flask import Flask, jsonify, request
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"status":"ok","name":"SmartTrading-D366 backend"})

@app.route('/signal', methods=['POST'])
def signal():
    data = request.json or {}
    symbol = data.get('symbol','BTCUSDT')
    t = int(time.time())
    side = "BUY" if (t // 10) % 2 == 0 else "SELL"
    return jsonify({
        "symbol": symbol,
        "side": side,
        "entry": 50000,
        "take_profit": 50500,
        "stop_loss": 49500
    })

@app.route('/connect', methods=['POST'])
def connect():
    d = request.json or {}
    return jsonify({"connected": True, "platform": d.get("platform","unknown")})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
