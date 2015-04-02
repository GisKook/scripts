__author__ = 'z'
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

def formatRGBList(rawcolors):
    RGBlist = [];
    colors = ""
    length = len(rawcolors);
    for i in range(0,length):
        if (rawcolors[i] >= '0' and rawcolors[i] <= '9') or (rawcolors[i] >= 'a' and rawcolors[i] <= 'f') or (rawcolors[i] >= 'A' and rawcolors[i] <= 'f'):
            colors+=rawcolors[i];
    length = len(colors)
    length = length/2
    length = length/3

    for i in range(0, length):
        R = int(colors[i:i+2], 16)
        G = int(colors[i+2:i+4], 16)
        B = int(colors[i+4:i+6], 16)

        RGBlist.append((R,G,B))

    return  RGBlist

def main():
    # RGBlist = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for i in range(100)]
    RGBlist = formatRGBList("49 20 61 6D 20 74 68 69 6E 6B 69 6E 67 20 69 6E 20 74 68 65 20 70 6C 61 6E 61 72 20 33 44 20 6D 6F 64 65 6C 20 77 69 6C 6C 20 72 65 73 65 6D 62 6C 65 20 73 6F 6D 65 20 73 6F 72 74 20 6F 66 20 6C 61 6E 64 73 63 61 70 65 2D 6C 69 6B 65 20 73 75 72 66 61 63 65 20 77 69 74 68 20 64 69 70 73 20 61 6E 64 20 72 69 73 65 73 20 74 68 61 74 20 63 6F 72 72 65 73 70 6F 6E 64 20 74 6F 20 74 68 65 20 68 65 78 20 64 61 74 61 2E 20 54 68 69 73 20 69 73 20 66 6F 72 20 61 6E 20 76 69 73 75 61 6C 20 61 72 74 20 70 72 6F 6A 65 63 74 20 62 75 74 20 49 20 61 6D 20 6E 6F 74 20 73 75 72 65 20 6F 66 20 69 74 27 73 20 66 69 6E 61 6C 20 66 6F 72 6D 20 69 6E 20 74 68 65 20 65 6E 64 2C 20 62 75 74 20 49 20 6B 6E 6F 77 20 69 74 20 77 69 6C 6C 20 77 69 74 68 20 74 68 65 73 65 20 22 6C 61 6E 64 73 63 61 70 65 22 20 70 6C 61 6E 61 72 20 73 75 72 66 61 63 65 73 2E")

    paleta=zip(*RGBlist)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(paleta[0],paleta[1],paleta[2], c=[(r[0] / 255., r[1] / 255., r[2] / 255.) for r in RGBlist])
    ax.grid(False)
    ax.set_title('grid on')
    plt.savefig('c:/blah.png')

if __name__ == "__main__":
    main()
