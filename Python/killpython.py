#! /usr/bin/python
#killpython.py
import sys
import subprocess
import StringIO

def listprograms(processname):
    command = ['ps', '-ef']
    p = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    out, err = p.communicate()
    buf = StringIO.StringIO(out)
    havepid = 0
    for line in buf:
        if line.find(processname) != -1: 
            sys.stdout.write("    ****  ")
            print line

if len(sys.argv) < 2:
    print '''
    ****  which python program do you want to kill? ;)
    '''
    listprograms("python")
    exit()

processname = sys.argv[1]
processname = "python "+processname


def main(): 
    command = ['ps', '-ef']
    p = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    out, err = p.communicate()
    buf = StringIO.StringIO(out)
    havepid = 0
    for line in buf:
        if line.find(processname) != -1: 
            pid = line.split(" ")[5]
            subprocess.call(["kill",pid])
            havepid = 1
            print "kill this pid "+processname+"*"
    if havepid == 0:
        print "not find \"python "+processname+"*"



if __name__ == "__main__":
    main()
