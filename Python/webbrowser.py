__author__ = 'zhangkai'
import urllib2
import subprocess

url = "http://www.google.com"
localurl="./www.baidu.com/index.html"

def wgetbrowser():
    command=['/bin/bash','./myget.sh',url]
    subprocess.call(command)

def openbrowseronline():
    command=['chromium-browser', '--kiosk', '--incognito', url]
    subprocess.call(command)

def openbrowserlocal():
    command=['chromium-browser', '--kiosk', '--incognito',localurl]
    subprocess.call(command)


def main():
    showonline = 1
    try:
        urllib2.urlopen(url=url,timeout=10,)
    except urllib2.HTTPError, err:
        print err
        showonline = 0
    except urllib2.URLError, err:
        print err
        showonline = 0

    if showonline==1 :
        wgetbrowser()
        openbrowseronline()
    else:
	openbrowserlocal()

if __name__ == "__main__":
    main()
