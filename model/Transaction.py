class Transaction():
    def __init__(self, time: str, buy_price: float, sell_price: float, deal_price: float, fluctuation: float, vol: int,
                 total_vol: int) -> None:
        self.time = time
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.deal_price = deal_price
        self.fluctuation = fluctuation
        self.vol = vol
        self.total_vol = total_vol
