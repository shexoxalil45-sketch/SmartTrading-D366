import numpy as np

def predict_direction(data):
    closes = [c['close'] for c in data[-20:]]
    change = closes[-1] - closes[-5]
    if change > 0:
        return "BUY"
    elif change < 0:
        return "SELL"
    return "HOLD"
