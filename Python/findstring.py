#查找文件中的内容
#参数1,目标文件夹 2，要找的文本
import sys
import os
import string 

if len(sys.argv)<3 or (not os.path.isdir(sys.argv[1])):
    print '''Please check your argvs
    Usage:
        python.exe findstring.py argv1 argv2
        argv1--Dest folder
        argv2--To-be find string
    '''
    sys.exit()
dir_path=sys.argv[1]
tobe_find=sys.argv[2]
complete_match=0
if len(sys.argv)==4:
    complete_match=sys.argv[3]

#从单个文件中查找目标内容，如果找到则显示
def find_string(filename):
    ext = os.path.splitext(filename)
    if ext[1]=='.h' or ext[1]=='.c' or ext[1]=='.cpp':
        src_file=file(filename,"r")
        i=0
        while True:
            line=src_file.readline();
            i=i+1
            if len(line)==0:
                src_file.close();
                break
            index=line.find(tobe_find)
            if -1!=index:
                if int(complete_match)==1:
                    
                    if (line[index-1] not in string.ascii_letters) and (line[index+len(tobe_find)] not in string.ascii_letters):
                        print filename
                        print line[0:len(line)-1] + "  ->linenum: %d " %(i) 
                else:
                    print filename
                    print line[0:len(line)-1] + "  ->linenum: %d " %(i) 

def find_string_infolder(folder_path):
    files=os.listdir(folder_path)
    for i in files:
        if os.path.isfile(os.path.join(folder_path,i)): 
            find_string(os.path.join(folder_path,i))

if __name__=="__main__":
    all_files = os.listdir(dir_path)
    for i in all_files:
        if os.path.isfile(os.path.join(dir_path,i)):
            find_string(os.path.join(dir_path,i))
        elif os.path.isdir(os.path.join(dir_path,i)):
            find_string_infolder(os.path.join(dir_path,i))



