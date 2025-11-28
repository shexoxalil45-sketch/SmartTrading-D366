def generate_signals(data):
    last = data[-1]
    entry = round(last['close'], 2)

    return {
        "entry": entry,
        "take_profit": round(entry * 1.01, 2),
        "stop_loss": round(entry * 0.99, 2)
    }
