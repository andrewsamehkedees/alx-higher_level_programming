#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1
    count = 0
    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(num))
        for arg in sys.argv:
            if count != 0:
                print("{}: {}".format(count, arg))
            count += 1
