# SmartTrading-D366 backend

1) Copy config.example.json -> config.json and fill your API keys.
2) Install dependencies:
   pip install -r requirements.txt
3) Run in demo mode:
   export ST_CFG=config.json
   python app.py
4) To test a signal:
   POST /api/signal with JSON {"symbol":"BTC/USDT", "exchange":"binance", "timeframe":"1m"}
5) When confident, set MODE to "LIVE" and ensure keys/capital are correct.
6) Secure the server: use HTTPS, API auth, IP allowlist, secrets manager.
