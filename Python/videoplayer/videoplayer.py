__author__ = 'z'

import sys
import subprocess
import os

videoonline = "http://dim.solutions/03_ashibo/store01/display02/ashibo_st01_ds02.h264" #online video url must be h264
videoonlineversionfile = "http://dim.solutions/03_ashibo/store01/display02/ashibo_st01_ds02.txt" #online video url must be h264
videodownloadname = "/home/pi/video/ashibo_st01_ds02.h264.download"
videodownloadversionname = "/home/pi/video/ashibo_st01_ds02.txt.download"
videolocal = "/home/pi/video/ashibo_st01_ds02.h264" #local video file
videoversionlocal = "/home/pi/video/ashibo_st01_ds02.txt"

# play videopath located video file use hello_video.bin
def play(videopath):
    print "play........."
    command = ['/opt/vc/src/hello_pi/hello_video/hello_video.bin', videopath]
    print command
    result = subprocess.call(command)

    return result == 0

# download online video use wget
def download(videodownloadpath,videoonlinepath):
    command = ['wget','-O', videodownloadpath, videoonlinepath]
    result = subprocess.call(command)

    if result == 0:
        return True
    else:
        return False

def isnewvideo():
    srcline=""
    dstline=""
    if(download(videodownloadversionname,videoonlineversionfile) == True):
        if(os.path.isfile(videoversionlocal)):
            srcversion=file(videoversionlocal,"r")
            srcline = srcversion.readline()
            srcversion.close()
        if(os.path.isfile(videoversionlocal)):
            dstversion = file(videodownloadversionname,"r")
            dstline = dstversion.readline()
            dstversion.close()
            print srcline
            print dstline
        if(srcline == dstline):
            os.remove(videodownloadversionname)
            return False
        else:
            print "-------------------------"  
            print srcline
            print dstline
            os.remove(videoversionlocal)
            os.rename(videodownloadversionname,videoversionlocal)

            return True
    else:
        return False

# try to download online video,if download success compare the size with local one 
# if size is not equal remove the local one and rename the downloaded file the the 
# local file's name then play.If no local file then rename the download one to local
# file then play it.If download fail play the local video.
def havenewvideo():
    if(isnewvideo()):
        if(download(videodownloadname,videoonline) == True):
            if(os.path.isfile(videolocal) == True):
                os.remove(videolocal)
                os.rename(videodownloadname, videolocal)
                return True
            else:
                os.rename(videodownloadname, videolocal)

                return True
    return False

# input endpoint
def main():
    havenewvideo()
    play(videolocal)

if __name__ == "__main__":
    main()
