#!/usr/bin/python

import sys
import os
import subprocess


print len(sys.argv)
if(len(sys.argv)<2):
	print '''
	useage:
		./xxx.py file_ext [dest_folder]
	'''
	sys.exit()
file_ext=sys.argv[1]
shfiledir = os.path.dirname(sys.argv[0]);
if(file_ext[0]!='.'):
	file_ext="."+file_ext;
des_folder="./"
if(len(sys.argv)>2):
	des_folder=sys.argv[2]
des_folder=os.path.abspath(des_folder)
files=os.listdir(des_folder)
for i in files:
	if(os.path.splitext(i)[1]==file_ext):
		returncode=subprocess.call(["sh",shfiledir+"/CNChangeCharset.sh",i,i+"_t"])
		if returncode == 0:
			os.remove(i)
			os.rename(i+"_t",i)
			print "process "+i+" complete"
		else:
			print "iconv fail"
		
	
