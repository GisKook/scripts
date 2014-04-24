#/usr/bin/python

import subprocess

def main():
	for i in range(100):
		subprocess.call(['/usr/bin/python','./manager_terminal.py'])


if __name__=="__main__":
	main()
