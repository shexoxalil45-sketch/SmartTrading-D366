def simple_momentum(prices):
    if len(prices) < 3:
        return 'hold'
    if prices[-1] > prices[-2] > prices[-3]:
        return 'buy'
    if prices[-1] < prices[-2] < prices[-3]:
        return 'sell'
    return 'hold'
