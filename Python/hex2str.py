import os
import sys

file_handle=file(sys.argv[1],"r+");
while True:
    string=file_handle.read(3)
    if len(string)==0:
        break
    print string

file_handle.close()
