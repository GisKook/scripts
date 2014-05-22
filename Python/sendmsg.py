import string
import socket
import os
import sys

def CalcCheckSum(buf):
    
    sum = 0;
    byarray=bytearray(buf)
    for i in byarray:
        sum ^=i
        sum %= 255
    else:
        return sum

def BuildMsg(mobile,content):
    result=bytearray('')
    result.insert(len(result),0) 
    result.insert(len(result),0)
    result.insert(len(result),0)
    result.insert(len(result),0)
    result.insert(len(result),0)
    result.insert(len(result),0)
    result.insert(len(result),0)
    result.insert(len(result),0)
    
    i=0
    while(1):
        tmp1=string.atoi(mobile[i:i+1])
        tmp2=string.atoi(mobile[i+1:i+2])
        result.insert(len(result),tmp1*16+tmp2)
        if i==8:
            break
        i+=2

    result.insert(len(result), string.atoi(mobile[10:11])*16+15)
    bycontent=bytearray(content)
    lenth = len(bycontent)
    if lenth/255>=1:
        result.insert(len(result), (lenth-255)*8)
    else:
            result.insert(len(result),0)
    result.insert(len(result),lenth*8)

    for j in bycontent:
        result.insert(len(result),j)

    totallen=len(result)+3
    
    if totallen/255>=1:
        result.insert(5, (totallen-255))
    else:
            result.insert(5,0)
    result.insert(6,totallen)
    checksum = CalcCheckSum(result)
    result.insert(len(result),checksum)

    return result
    

mobiles=sys.argv[1]
content=sys.argv[2]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', ))

res =BuildMsg(mobiles,content)
print res
import time
time.sleep(2)
sock.send(res)
sock.close()
'''os.system("pause")'''
