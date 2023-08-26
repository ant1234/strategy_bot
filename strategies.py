import logging
from typing import *
from models import *

logger = logging.getLogger()

TF_EQUIV = {'1m': 60, '5m': 300, '15m': 900, '30m': 1800, '1h': 3600, '4h': 14400}

class Strategy:
    def __init__(self, 
                 contract: Contract, 
                 exchange: str, 
                 timeframe: str, 
                 balance_pct: float, 
                 take_profit: float,
                 stop_loss: float):
        
        self.contract = contract
        self.exchange = exchange
        self.tf = timeframe
        self.tf_equiv = TF_EQUIV[timeframe] * 1000
        self.balance_pct = balance_pct
        self.take_profit = take_profit
        self.stop_loss = stop_loss
        self.candles: List[Candle] = []

    def parse_trades(self, price: float, size: float, timestamp: int):
        
        last_candle = self.candles[-1]

        # same candle 
        if timestamp < last_candle.timestamp * self.tf_equiv:
            last_candle.close = price
            last_candle.volume += size

            if price > last_candle.high:
                last_candle.high = price
            elif price < last_candle.low:
                last_candle.low = price

        # missing candle(s)
        elif timestamp >= last_candle.timestamp + 2 * self.tf_equiv:
            return

        # new candle
        elif timestamp >= last_candle.timestamp + self.tf_equiv:
            return


class TechnicalStrategy(Strategy):
    def __init__(self, 
                 contract: Contract, 
                 exchange: str, 
                 timeframe: str, 
                 balance_pct: float, 
                 take_profit: float,
                 stop_loss: float,
                 other_params: Dict):
    
        super().__init__(contract,
                        exchange,
                        timeframe,
                        balance_pct,
                        take_profit,
                        stop_loss)
        
        self._ema_fast = other_params['ema_fast']
        self._ema_slow = other_params['ema_slow']
        self._ema_signal = other_params['ema_signal']

        print("Activated strategy for ", contract.symbol)
 
class BreakoutStrategy(Strategy):
    def __init__(self, 
                 contract: Contract, 
                 exchange: str, 
                 timeframe: str, 
                 balance_pct: float, 
                 take_profit: float,
                 stop_loss: float,
                 other_params: typing.Dict):
    
        super().__init__(contract,
                        exchange,
                        timeframe,
                        balance_pct,
                        take_profit,
                        stop_loss)
        
        self._minimum_volume = other_params['minimum_volume']
    