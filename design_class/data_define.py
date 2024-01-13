class Record:
    def __init__(self,data,order_id, money,provice) -> None:
        self.date = data
        self.order_id = order_id
        self.money = int(money)
        self.provice = provice
        
    def __str__(self) -> str:
        return  f'{self.date}, {self.order_id}, {self.money}, {self.provice}.'
        