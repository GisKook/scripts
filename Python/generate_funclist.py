#生成头文件函数列表
#对头文件的文件说明有要求，对函数声明的格式也有要求
#头文件的文件说明如下
#    /*
#     * brief: 数据库的约束类, 约束分为表级约束和列级约束
#     * function list:
#     * 
#     * author: zhangkai
#     * date: 2013年12月30日
#     */
#函数声明如下
#    // brief 设置主键
#	 // param[in] strPrimaryKey主键
#	 void SetPrimaryKey(const GKString& IN strPrimaryKey);
#    参数: 文件的位置
import sys
import os
import shutil
import string


if len(sys.argv)<2:
    print '''
    please check you args
    Usage: python.exe generate_funclist.py xxxxxx.cpp'''
    sys.exit()

#复制一个文件作为目标文件
#des_file_name=sys.argv[1]+'.bak'
#if os.path.isfile(des_file_name):

if os.path.isfile(sys.argv[1]):
    shutil.copyfile(sys.argv[1],des_file_name)
    print 'copy source file... finished'
des_file = file(des_file_name, 'r+')

#找到要注释的行
while True:
    func_list=des_file.readline()
    func_list_line_num = string.find(func_list, 'function list')
    if func_list_line_num != -1: 
        break
    if len(func_list)==0:
        des_file.close()
        break;

#从源文件中找到class关键字，
if(func_list_line_num != -1):
    src_file = file(sys.argv[1], 'r')
    while True: 
        line=src_file.readline()
        print line
        class_line_num = string.find(line, 'class') 
        if class_line_num != -1:
            des_file.write(line)
            des_file.flush()
            break
