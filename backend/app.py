from flask import Flask, jsonify
from tradingview_api import get_tradingview_data
from ai_model import predict_direction
from signal_engine import generate_signals

app = Flask(__name__)

@app.route("/analysis")
def analysis():
    data = get_tradingview_data()
    direction = predict_direction(data)
    signals = generate_signals(data)
    return jsonify({
        "trend": direction,
        "signals": signals
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
