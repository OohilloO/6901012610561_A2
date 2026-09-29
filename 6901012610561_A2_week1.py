class Item:

    def __init__(self, code, title, unit_price, qty):
        self.code = code
        self.title = title
        self.unit_price = unit_price
        self.qty = qty

    def show(self):
        print(f"รหัสสินค้า : {self.code}")
        print(f"ชื่อสินค้า : {self.title}")
        print(f"ราคา       : {self.unit_price} บาท")
        print(f"จำนวน      : {self.qty} ชิ้น")

    def add_qty(self, amount):
        self.qty += amount

    def can_sell(self, amount):
        return amount <= self.qty

    def remove_qty(self, amount):
        self.qty -= amount
        return amount * self.unit_price

    def is_low(self, limit=5):
        return self.qty <= limit