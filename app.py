from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import time, random, os
app = Flask(__name__, static_folder='../web', static_url_path='/')
CORS(app)
@app.route('/api/ping')
def ping():
    return jsonify({"ok": True, "time": time.time()})
@app.route('/api/signals')
def signals():
    sample = [
        {"symbol":"BTC/USDT","strategy":"MACD","signal":"HOLD","confidence":50},
        {"symbol":"ETH/USDT","strategy":"RSI","signal":"SELL","confidence":62},
        {"symbol":"XRP/USDT","strategy":"MA","signal":"BUY","confidence":71}
    ]
    return jsonify({"signals": sample})
@app.route('/api/candles/<symbol>')
def candles(symbol):
    data = []
    ts = int(time.time()) - 3600
    price = 1000.0
    for i in range(60):
        o = price + random.uniform(-5,5)
        h = o + random.uniform(0,6)
        l = o - random.uniform(0,6)
        c = o + random.uniform(-3,3)
        data.append([ts + i*60, round(o,2), round(h,2), round(l,2), round(c,2)])
        price = c
    return jsonify({"symbol": symbol, "candles": data})
@app.route('/')
def index():
    web_dir = os.path.abspath(os.path.join(app.root_path, '../web'))
    if os.path.exists(os.path.join(web_dir, 'index.html')):
        return send_from_directory(web_dir, 'index.html')
    return jsonify({"ok": True, "msg": "SmartTrading-D366 backend running"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
