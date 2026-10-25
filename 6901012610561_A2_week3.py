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


def menu_receive(self):
        print("\n===== รับสินค้าเข้า =====")
        item = self.warehouse.find(input("กรอกรหัสสินค้า: "))
        if item is None:
            print("ไม่พบสินค้านี้")
            return
        item.add_qty(int(input("จำนวนที่รับเข้า: ")))
        print("รับสินค้าเข้าสำเร็จ")
        print(f"จำนวนคงเหลือ : {item.qty} ชิ้น")

    def menu_sell(self):
        print("\n===== ขายสินค้าออก =====")
        item = self.warehouse.find(input("กรอกรหัสสินค้า: "))
        if item is None:
            print("ไม่พบสินค้านี้")
            return
        amount = int(input("จำนวนที่ขาย: "))
        if not item.can_sell(amount):
            print("สินค้าในคลังไม่เพียงพอ")
            return
        total = item.remove_qty(amount)
        print("ขายสินค้าสำเร็จ")
        print(f"จำนวนที่ขาย : {amount}")
        print(f"ราคา        : {total} บาท")
        print(f"เหลือสินค้า : {item.qty} ชิ้น")

    def menu_low(self):
        print("\n===== สินค้าใกล้หมด =====")
        low = self.warehouse.low_items()
        if not low:
            print("ไม่มีสินค้าใกล้หมด")
            return
        for item in low:
            print(f"{item.code} {item.title} เหลือ {item.qty} ชิ้น")

    def print_menu(self):
        print("\n==============================")
        print("     ระบบจัดการคลังสินค้า")
        print("==============================")
        print("1. เพิ่มสินค้า")
        print("2. แสดงสินค้าทั้งหมด")
        print("3. ค้นหาสินค้า")
        print("4. รับสินค้าเข้า")
        print("5. ขายสินค้าออก")
        print("6. ตรวจสอบสินค้าใกล้หมด")
        print("0. ออกจากโปรแกรม")

    def run(self):
        actions = {
            "1": self.menu_add,
            "2": self.menu_show,
            "3": self.menu_search,
            "4": self.menu_receive,
            "5": self.menu_sell,
            "6": self.menu_low,
        }
        while True:
            self.print_menu()
            choice = input("เลือกเมนู: ")
            if choice == "0":
                print("จบการทำงาน")
                break
            if choice in actions:
                actions[choice]()
            else:
                print("กรุณาเลือกเมนู 0-6")


if __name__ == "__main__":
    App().run()