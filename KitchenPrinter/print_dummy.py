from escpos.printer import Network
import psycopg2 as pg2
from datetime import datetime, timedelta
import os
import time as t


# need randint, time, product, amount
class Printer:
    def __init__(self):

        # need to call order data
        self.dummy = {
            "order_id" : 6991149581065129984,
            "order_status" : 2,
            "order_price" : 54500,
            "product_list" : [
                {
                    "product_id" : 6989407965291876352,
                    "product_name" : "pringles",
                    "product_quantity" : 3,
                    "product_price" : 9000,
                    "sub_product_list": [
                        {
                            "sub_product_id" : 6986451025192423424,
                            "sub_product_name" : "Onion flavor",
                            "sub_product_price" : 1000,
                        },
                        {
                            "sub_product_id" : 6986451025192423424,
                            "sub_product_name" : "Limited figure",
                            "sub_product_price" : 5000,
                        },
                    ]
                },
                {
                    "product_id" : 6989406770791845888,
                    "product_name" : "pepero",
                    "product_quantity" : 5,
                    "product_price" : 5500,
                    "sub_product_list": [
                        {
                            "sub_product_id" : 6986450945467092992,
                            "sub_product_name" : "Original",
                            "sub_product_price" : 0,
                        },
                    ]
                },
            ]
        }
        
    def getOrderData(self):
        self.order_id = str(self.dummy["order_id"])[-3:]
        self.product_list = self.dummy["product_list"]
        self.orderData = [self.order_id, self.product_list]
        
    
    def prinReceipt(self):
        self.getOrderData()
        L = len(self.orderData[1])
        
        p = Network("192.168.1.19")
        p.set('center','BU','normal',3,3,10)
        p.text("No."+self.orderData[0]+"\n")
        p.set('center','B','normal',2,2,10)
        p.text("----------------------------\n")
        
        # product loop
        for i in range(L):
            p.set('left','B','normal',2,2,10)
            p.text(str(self.orderData[1][i]["product_name"])+ " "*(22 - len(str(self.orderData[1][i]["product_name"]))))
            p.text(str(self.orderData[1][i]["product_quantity"]) + "\n")
            
            # sub-product loop
            L_sub = len(self.orderData[1][i]["sub_product_list"])
            if L_sub != 0 : 
                for j in range(L_sub):
                    p.set('left','B','normal',2,2,10)
                    p.text(" --> " + str(self.orderData[1][i]["sub_product_list"][j]["sub_product_name"]) + "\n")
                    
        p.set('center','B','normal',2,2,10)
        p.text("----------------------------\n")
        p.set('right','B','normal',2,2,10)
        p.text(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                   
        p.cut()
        p.close()
        
        
if __name__ == "__main__":
    pt = Printer()
    pt.prinReceipt()
