# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import json, logging, os

# نستخدم executor جاهز لديك (كما وضعنا سابقاً)
from executor import TradeExecutor
from notifier import Notifier

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SmartBackend")

# load config (use config.json or config.example.json)
cfg_path = os.environ.get("ST_CFG", "backend/config.example.json")
with open(cfg_path) as f:
    CFG = json.load(f)

notifier = Notifier(CFG)
executor = TradeExecutor(CFG, notifier=notifier)

app = Flask(__name__)
CORS(app)

@app.route("/api/ping")
def ping():
    return jsonify({"ok": True, "mode": CFG.get("MODE","DEMO")})

# TradingView webhook receiver
# In TradingView alert you must set webhook URL to: https://your-server.com/api/webhook
@app.route("/api/webhook", methods=["POST"])
def webhook():
    """
    Expect TradingView to send JSON like:
    {
      "ticker":"BINANCE:BTCUSDT",
      "strategy":"MyStrategy",
      "action":"BUY",
      "price": 12345.67,
      "time":"2025-11-28T12:00:00Z",
      "extra": {...}
    }
    """
    try:
        data = request.get_json(force=True)
        logger.info("Webhook received: %s", data)

        # Map tradingview symbol to exchange/symbol format we use (e.g. BINANCE:BTCUSDT -> BTC/USDT)
        raw_ticker = data.get("ticker") or data.get("symbol")
        if raw_ticker and ":" in raw_ticker:
            parts = raw_ticker.split(":")
            provider = parts[0].lower()
            symbol_tv = parts[1]
        else:
            provider = "binance"
            symbol_tv = raw_ticker or data.get("symbol")

        # convert to ccxt symbol format
        # TradingView uses BTCUSDT -> convert to BTC/USDT
        if symbol_tv and symbol_tv.endswith("USDT"):
            sym = symbol_tv.replace("USDT", "/USDT")
        else:
            sym = symbol_tv

        action = data.get("action") or data.get("signal") or data.get("strategy_action")
        timeframe = data.get("timeframe", "1m")

        # If TradingView sends BUY/SELL directly, execute using executor
        if action and action.upper() in ("BUY", "SELL"):
            res = executor.evaluate_and_execute(sym, exchange_name=provider, timeframe=timeframe)
            return jsonify({"ok": True, "executed": res}), 200

        return jsonify({"ok": True, "msg": "no action mapped"}), 200

    except Exception as e:
        logger.exception("Webhook error: %s", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
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
