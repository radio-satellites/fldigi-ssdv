import socket
import uuid
import time
import os

_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_s.settimeout(1)
num_nochars = 0
try:
    _s.connect(("127.0.0.1",7322))
except:
    print("ERROR: COULD NOT CONNECT TO FLDIGI")
    #exit()

total_data = bytearray()

buffer = ""

packetstart = False

while True:
    try:
        _char = _s.recv(1).decode()
        #print(_char)
        
        if _char == "!":
            packetstart = False
            #flush buffer, write to file
            #print(buffer)
            print("WRITE")
            try:
                total_data = total_data + bytearray(bytes.fromhex(buffer))
            except Exception as e:
                bad_char = int(str(e)[58:])
                try:
                    total_data = total_data + bytearray(bytes.fromhex(buffer[bad_char:]))
                except:
                    print("Couldn't recover data from packet due to bad header")
                
                    
            buffer = ""
            f = open("decoded.bin",'wb')
            f.write(total_data)
            f.close()
        else:
            if _char == "\x00":
                pass
            elif packetstart:
                buffer = buffer + _char
            else:
                pass
            if _char == "?":
                packetstart = True
    except Exception as e:
        print(e)
        pass
    
