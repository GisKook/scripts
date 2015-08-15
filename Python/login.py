import sys, select
import subprocess

print "Do You want to debug videoplayer?"

i, o, e = select.select( [sys.stdin], [], [], 10 )

if (i):
  print "welcome to debug raspberry pi"
else:
	command=['python','/home/pi/videoplayer.py']
	subprocess.call(command)
	
