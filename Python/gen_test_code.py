#/bin/python

import subprocess
import time
def gen_single(name, start_line, end_line):
    subprocess.Popen("mkdir %s" % name, shell=True, stdout=subprocess.PIPE)
    subprocess.Popen("cp gun/conf.json %s" % name, shell=True, stdout=subprocess.PIPE)
    subprocess.Popen("cp gun/main %s" % name, shell=True, stdout=subprocess.PIPE)
    subprocess.Popen("sed -n \"%d, %dp\" gun/id.txt > %s/id.txt" % (start_line , end_line , name) , shell=True, stdout=subprocess.PIPE)
    subprocess.Popen("./%s/main &" % name, shell=True, stdout=subprocess.PIPE)


def main():
    for i in range(0, 18):
	gen_single("main"+str(i), 1+500*i , 500+500*i)

if __name__ == "__main__":
    main()

