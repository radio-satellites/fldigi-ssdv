import socket
import uuid
import time
import os

_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_s.settimeout(1)
num_nochars = 0

f = open("output.bin",'rb')

size = os.path.getsize('output.bin')

frames = int(size/256)

try:
    _s.connect(("127.0.0.1",7322))
except:
    print("ERROR: COULD NOT CONNECT TO FLDIGI")
    #exit()



for i in range(frames):
    frame = f.read(256)
    _s.send(("?"+str(frame.hex())+"!").encode())



"""
#TESTS!!!
frame = f.read(256)
_s.send(("?"+str(frame.hex())+"!").encode())
#_s.send("\n".encode())
print(str(frame.hex())+"")
"""
