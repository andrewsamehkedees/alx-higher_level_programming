#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if not int(number):
    print("TypeError")
last = str(number)
theLast = int(last[-1])
if number < 0:
    theLast = theLast * -1
if theLast > 5:
    print(f"Last digit of {number} is {theLast} and is greater than 5")
elif theLast == 0:
    print(f"Last digit of {number} is {theLast} and is 0")
else:
    print(f"Last digit of {number} is {theLast} and is less than 6 and not 0")
