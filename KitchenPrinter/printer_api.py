from escpos.printer import Network
from datetime import datetime
from dataclasses import dataclass
from typing import List


# ---------- data class for PrintData ----------
@dataclass
class SubProduct:
    sub_product_name: str


@dataclass
class Product:
    product_name: str
    product_quantity: int
    sub_product_list: List[SubProduct]


@dataclass
class PrintData:
    order_id: int
    product_list: List[Product]
    is_printed: bool = False


# ----------------------------------------------

class Printer:

    def __init__(self):
        self.is_printed = None
        self.product_list = None
        self.order_id = None
        self.data = None

    def getPD(self, data):
        self.data = data

    def getOrderData(self):
        self.order_id = str(self.data.order_id)[-3:]
        self.product_list = self.data.product_list
        self.is_printed = self.data.is_printed

    def prinReceipt(self):
        if not self.data.is_printed:
            self.getOrderData()
            L = len(self.product_list)

            p = Network("192.168.1.19")
            p.set('center', 'BU', 'normal', 3, 3, 10)
            p.text("No." + self.order_id + "\n")
            p.set('center', 'B', 'normal', 2, 2, 10)
            p.text("----------------------------\n")

            # product loop
            for i in range(L):
                p.set('left', 'B', 'normal', 2, 2, 10)
                p.text(str(i+1) + ". " +
                       str(self.product_list[i].product_name) + " " * (
                                   22 - len(str(self.product_list[i].product_name))))
                p.text(str(self.product_list[i].product_quantity) + "\n")

                # sub-product loop
                L_sub = len(self.product_list[i].sub_product_list)
                if L_sub != 0:
                    for j in range(L_sub):
                        p.set('left', 'B', 'normal', 2, 2, 10)
                        p.text(" --> " + self.product_list[i].sub_product_list[j].sub_product_name + "\n")

            p.set('center', 'B', 'normal', 2, 2, 10)
            p.text("----------------------------\n")
            p.set('right', 'B', 'normal', 2, 2, 10)
            p.text(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            p.cut()
            p.close()

            self.data.is_printed = True
            return 0
        else:
            print("order already printed")
            return 1


if __name__ == "__main__":
    # generate PrintData object
    sub_product_data = [[SubProduct("Onion flavor"), SubProduct("Limited figure")], [SubProduct("Original")]]
    product_data = [Product("pringles", 3, sub_product_data[0]), Product("pepero", 5, sub_product_data[1])]
    print_data = PrintData(6989407965291876352, product_data)

    pt = Printer()
    pt.getPD(print_data)
    pt.prinReceipt()
