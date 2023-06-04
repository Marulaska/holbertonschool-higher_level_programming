#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if (x < y):
            print("{:1d}".format(x) + "{:1d}".format(y), end="")
            if (x < 8):
                print(end=", ")
            else:
                print()
