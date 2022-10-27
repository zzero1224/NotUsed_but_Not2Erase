import os
import pandas as pd
import datetime as dt

def getDate():
   today = dt.datetime.now().strftime('%y%m%d')
   return today

def getFileNo():
   files =  os.listdir("C:/Users/master/Desktop/Everything/python_based/RFIDautomation/tag")
   return len(files), files
   
def getFiles_today():
    dummy = []
    today = getDate()
    L, files = getFileNo()
    for i in range(L):
        if files[i].split("_")[3] == today:
            dummy.append(pd.read_excel("tag/"+files[i]))
    return dummy, today
    
def mergeFiles():
    total_excel, today = getFiles_today()
    outputDF = pd.concat(total_excel)
    filename = "RFID_TAG_"+ today + "_total.xlsx"
    outputDF.to_excel("./"+ filename)
    print("excel file in : " + os.getcwd() + "/" + filename)
    print("generate tag from record 2 to " + str(outputDF.count()[0]))

def main():
    mergeFiles()
    os.system('C:/Users/master/Desktop\TagPrint\TagPrint.exe')

if __name__== "__main__":
    print(getDate())
    main()
    