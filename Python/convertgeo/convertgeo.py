# -*- coding: utf-8 -*-
import sys
import os
import string
import math


def main():
    filename = sys.argv[1]
    src_file = file(filename, "r")
    dst_file = file(filename+"bak", "w")
    index = 1
    indexpart = 0
    while True:
        line_content = src_file.readline()

        if len(line_content) == 0:
            break
        if line_content.find("[地块坐标]") != -1 :
            line_content = src_file.readline()
            line_content_list = string.split(line_content, ",")

            if line_content_list[4] == "线":
                point_count = int(line_content_list[0])
                dst_file.write("Polyline\n")
                line_content = src_file.readline()
                line_content_list = line_content_list = string.split(line_content, ",")
                dst_file.write(line_content_list[1]+" 0\n")
                for i in range(0, point_count):
                    line_content_list = string.split(line_content, ",")
                    dst_file.write(str(i)+" "+line_content_list[2] + " " + line_content_list[3].strip('\n') + "1.#QNAN 1.#QNAN\n")
                    line_content = src_file.readline()
                dst_file.write("END\n")
            elif line_content_list[4] == "面":
                point_count = int(line_content_list[0])
                dst_file.write("Polygon\n")
                line_content = src_file.readline()
                line_content_list = line_content_list = string.split(line_content, ",")
                dst_file.write(line_content_list[1]+" 0\n")
                for i in range(0, point_count):
                    line_content_list = string.split(line_content, ",")
                    dst_file.write(str(i)+" "+line_content_list[2] + " " + line_content_list[3].strip('\n') + "1.#QNAN 1.#QNAN\n")
                    line_content = src_file.readline()
                dst_file.write("END\n")



if __name__ == "__main__":
    main()
