import win32com.client
from ctypes import *
import pythoncom
import os
import socket

# in registry editor 컴퓨터\HKEY_CLASSES_ROOT\TAGPRINTX.TagPrintXCtrl.1
# CLSID : {42575D0B-C9FC-4CA7-BABC-749803F00D90}
# dir : TAGPRINTX.TagPrintXCtrl.1
ocx_path = "C:/Users/master/Desktop/TagPrint/TagPrint.ocx" # ocx file path
dll_path = "C:/Users/master/Desktop/TagPrint/TagPrint_DLL.dll"

TagPrint = win32com.client.Dispatch("TAGPRINTX.TagPrintXCtrl.1") # activeX bringup
libc = cdll.LoadLibrary(dll_path)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(sock.connect_ex(('192.168.1.20', 9100)))

# PING TEST
# hostname = "192.168.1.20"
# response = os.system("ping -n 1 " + hostname)
# if response == 0:
#     Netstatus = "Network Active" 
# else:
#     Netstatus = "Network Error"

print(libc.setPrintIP("192.168.1.20"))
print(libc.setPrintPort("9100"))
# print(libc.setFileName("C:/Users/master/Desktop/Everything/python_based/RFIDautomation/RFID_format.txt"))
# print(libc.setTagDts("002209300003002210110001!!00220930-0003-00221011-0001!!파워에이드!!2,200원!!↑태그가 천장을 바라보게 해주세요."))
# print(libc.TagPrint())

print(type(TagPrint))