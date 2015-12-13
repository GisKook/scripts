__author__ = 'zhangkai'
import urllib2
import subprocess
import threading
import os
import StringIO

url = "http://www.baidu.com"
localurl="./www.baidu.com/index.html"
urlversionfile="https://github.com/GisKook/smarthomebox/blob/master/readme.md"


checktime = 5;
versionfiledownload = "./version.txt.download"
versionfile="./version.txt"

def wgetbrowser():
    command=['/bin/bash','./myget.sh',url]
    subprocess.call(command)

def openbrowseronline():
    command=['chromium', '--kiosk', '--incognito', url]
    subprocess.call(command)

def openbrowserlocal():
    command=['chromium', '--kiosk', '--incognito',localurl]
    subprocess.call(command)

def startbrowser():
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

def downloadfile(downloadurlfilepath, urlfilepath):
    command = ['wget','-O',downloadurlfilepath, urlfilepath]
    print command

    return 0 == subprocess.call(command)

def compareversion(downloadfile, localfile):
    srcline=""
    dstline=""
    if os.path.isfile(downloadfile):
        downloadversion = file(downloadfile,"r")
        dstline = downloadversion.readline()
        downloadversion.close()
    if os.path.isfile(localfile):
        localversion = file(localfile,"r")
        srcline = localversion.readline()
        localversion.close()
    if srcline == dstline:
        os.remove(downloadfile)
        return True
    else:
        if os.path.isfile(localfile):
            os.remove(localfile)
        os.rename(downloadfile,localfile)
        return False

def closebrowser():
    command = ['ps', '-ef']
    p = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    out, err = p.communicate()
    buf = StringIO.StringIO(out)
    for line in buf:
        if line.find("chromium") != -1:
            for pid in line.split(" "):
                if pid.isdigit():
                    subprocess.call(["kill",pid])
                    break

start = 0
def checkversionfile():
    threading.Timer(checktime,checkversionfile).start()
    if downloadfile(versionfiledownload, urlversionfile):
        if not compareversion(versionfiledownload, versionfile):
            closebrowser()
            startbrowser()
            start = 1

def main():
    checkversionfile()
    if start == 0:
        closebrowser()
        startbrowser()

if __name__ == "__main__":
    main()
