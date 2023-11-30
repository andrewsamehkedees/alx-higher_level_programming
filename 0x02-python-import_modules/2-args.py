#!/usr/bin/python3
import sys

num = len(sys.argv)
count = 0
if num == 0:
    print ("0 arguments.")
else:
    print("{} arguments:".format(num))
    for i in argv:
        print("{}: {}".format(count, i))
