class Item:
    """แทนสินค้า 1 ชิ้นในคลัง"""

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

class Warehouse:
    """จัดการรายการสินค้าทั้งหมด"""

    def __init__(self):
        self.items = []

    def find(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def add(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def low_items(self):
        return [item for item in self.items if item.is_low()]


class App:
    """ส่วนติดต่อผู้ใช้ (เมนู)"""

    SEP = "-------------------------"

    def __init__(self):
        self.warehouse = Warehouse()

    def menu_add(self):
        print("\n===== เพิ่มสินค้า =====")
        code = input("รหัสสินค้า: ")
        title = input("ชื่อสินค้า: ")
        unit_price = float(input("ราคาสินค้า: "))
        qty = int(input("จำนวนสินค้า: "))
        self.warehouse.add(Item(code, title, unit_price, qty))
        print("เพิ่มสินค้าสำเร็จ!")

    def menu_show(self):
        print("\n===== สินค้าทั้งหมด =====")
        if self.warehouse.is_empty():
            print("ยังไม่มีสินค้า")
            return
        for item in self.warehouse.items:
            print(self.SEP)
            item.show()
        print(self.SEP)

    def menu_search(self):
        print("\n===== ค้นหาสินค้า =====")
        item = self.warehouse.find(input("กรอกรหัสสินค้า: "))
        if item is None:
            print("ไม่พบสินค้านี้")
            return
        print("พบสินค้า")
        print(self.SEP)
        item.show()
        print(self.SEP)