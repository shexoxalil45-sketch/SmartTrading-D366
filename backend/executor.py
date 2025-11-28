# executor.py
import logging
import time
from connectors.ccxt_connector import ExchangeConnector
from connectors.mt5_connector import MT5Connector
from strategies.indicators import df_from_ohlcv, combined_signal
import requests

logger = logging.getLogger("executor")

class TradeExecutor:
    def __init__(self, cfg, notifier=None):
        self.cfg = cfg
        self.mode = cfg.get("MODE","DEMO")
        self.connector = ExchangeConnector(cfg)
        self.mt5 = MT5Connector(cfg.get("MT5",{}))
        self.notifier = notifier

    def evaluate_and_execute(self, symbol, exchange_name='binance', timeframe='1m'):
        ohlcv = self.connector.fetch_ohlcv(symbol, timeframe=timeframe, limit=200, exchange_name=exchange_name)
        df = df_from_ohlcv(ohlcv)
        signal = combined_signal(df)
        logger.info(f"Signal {symbol} => {signal}")
        if signal['signal'] in ('BUY','SELL'):
            # compute amount (example: fixed USD amount)
            try:
                size_usd = self.cfg.get('ORDER_SETTINGS', {}).get('SIZE_USD', 10)
                # fetch price
                last_price = df['close'].iloc[-1]
                amount = round(size_usd / float(last_price), 6)
                res = self.connector.place_order(exchange_name, symbol, signal['signal'].lower(), amount, mode=self.mode)
                message = f"Executed {signal['signal']} {symbol} on {exchange_name} mode={self.mode} amt={amount} price={last_price} res={res}"
                logger.info(message)
                if self.notifier:
                    self.notifier.send(message)
                return {"result": res, "signal": signal}
            except Exception as e:
                logger.exception("Order error: " + str(e))
                if self.notifier:
                    self.notifier.send("Order error: " + str(e))
        else:
            logger.debug("No trade (HOLD)")
            return {"result": None, "signal": signal}
