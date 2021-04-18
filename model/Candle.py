class Candle():
    def __init__(self, high_price: float, low_price: float, deal_price: float, start_price: float,end_price: float, vol: int) -> None:
        self.high_price = high_price
        self.low_price = low_price
        self.deal_price = deal_price
        self.start_price = start_price
        self.end_price = end_price
        self.vol = vol

