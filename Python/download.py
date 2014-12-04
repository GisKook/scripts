import subprocess
import sys

def main():
    if(len(sys.argv)<2):
        print '''
        useage:
            python download.py url [location]
        '''
        sys.exit()
    url = sys.argv[1]
    location = sys.argv[2]
    subprocess.call(["wget.exe", " -c "+"\""+url+"\" "+"--directory-prefix="+"\""+location+"\""])

if __name__ == "__main__":
    main()
