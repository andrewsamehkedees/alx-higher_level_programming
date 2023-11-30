#!/usr/bin/python3
if __name__ = "__main__":
    import sys

    num = len(sys.argv) - 1
    count = 0
    if num == 0:
        print ("0 arguments.")
    else:
        print("{} arguments:".format(num))
        for arg in sys.argv:
            print("{}: {}".format(count, arg))
