import serial
import time

SPD = serial.Serial('COM4', 115200, timeout=0.1)

class SPD_500_controller():
    def __init__(self):
        self.response = bytes(bytearray([0x06, 0x06, 0x06, 0x06]))
        self.cnt = 0
        self.STX = [0x02]
        self.EXT = [0x03]
    
    #default len for price is 8 bytes
    def crc16(self, data, offset=0):
        length = len(data)
        if data is None or offset < 0 or offset > len(data) - 1 and offset+length > len(data):
            return 0
        crc = 0x0000
        for i in (range(0, length)):
            crc ^= data[i]
            print(bin(crc))
            for j in range(0, 8):
                if (crc & 0x0001) > 0:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc = crc >> 1
        return hex(crc)

    def check_card_init(self):
        self.init_read = []
        while self.cnt < 9:
            res = SPD.read().hex() # str
            if len(res) == 2:
                self.init_read.append(res)
                self.cnt += 1
        return(self.init_read)
    def send_response(self):
        SPD.write(self.response)
        
    def set_price(self):
        self.price_in_won = input("enter price in won : ")
        if len(self.price_in_won < 6):
            for i in range(6 - self.price_in_won):
                self.price_in_won = "0" + self.price_in_won
        
        self.header = [0x00, 0x08, 0xF8, 0x20, 0x02]
        self.price = [int(self.price_in_won[0:2]), int(self.price_in_won[2:4]), int(self.price_in_won[4:6])]
        data_for_crc = self.header + self.price + self.EXT
        self.hexcrc = self.crc16(data_for_crc)
        self.pcrc = []
    
    def main(self):
        init = self.check_card_init()
        print(init)
        self.send_response()
        time.sleep(0.5)

if __name__ == "__main__":
    SPD500 = SPD_500_controller()
    SPD500.main()