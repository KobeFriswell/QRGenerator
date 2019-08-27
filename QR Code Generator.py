from qrtools import QR
import os
import shutil
import sys

low = input("What is the lower bound?")
print low

high = input("What is the higher bound?")
print high

#Try to create folder for code, but pass if already exists
try:
    os.makedirs("/home/student/QR/"+str(low)+"-"+str(high)+"/")
except OSError:
    print "Files Already Exist!"
    sys.exit()



for x in range (low,high+1):
    print str(x)
    myCode = QR(data=str(x), pixel_size=10)
    myCode.encode()
    filepath = myCode.filename
    QRfile = filepath.split("/")
    shutil.move(filepath,"/home/student/QR/"+str(low)+"-"+str(high)+"/"+str(x)+".png")

    

