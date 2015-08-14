__author__ = 'z'

import sys
import subprocess
import os
import threading

videoonline = "http://wwwold.cs.umd.edu/class/fall2002/cmsc818s/Readings/b-tree.pdf"
videodownloadname = "D:/download/HairMode_Final_03.mp4.download"
videolocal = "/mnt/usb/*"

downloadok = False

def play(videopath):
    command = ['/opt/vc/src/hello_pi/hello_video/hello_video.bin', '/mnt/usb/*']
    result = subprocess.call(command)

    return result == 0

def download(videoonlinepath):
    command = ['wget','-O', videodownloadname, videoonlinepath]
    print command
    result = subprocess.call(command)

    if result == 0:
        downloadok = True
    else:
        downloadok = False

def havenewvideo():
    return True

def main():
    playthread = threading.Thread(target=play,args=(videolocal,))
    downloadthread = threading.Thread(target=download,args=(videoonline,))
    if(os.path.isfile(videolocal) == True):
        playthread.start()
    if(havenewvideo()):
        downloadthread.start()

    """

    if(havenewvideo()):
        if(download(videoonline) == True):
            if(play(videodownloadname) != True):
                play(videolocal)
    play(videolocal)
    """

if __name__ == "__main__":
    main()