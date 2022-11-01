# dummy : 02 00 05 13 20 01 03 df 88
def crc16(data, offset=0):
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

if __name__ == "__main__":
    data = [0x00, 0x05, 0x13, 0x20, 0x01, 0x03] #'c7', '8f'
    print(hex(str(crc16(data)[2:4])))
