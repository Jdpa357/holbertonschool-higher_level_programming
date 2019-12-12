#!/usr/bin/python3
import sys

if len(sys.argv) is 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(len(sys.argv) - 1))
for i, a in enumerate(sys.argv):
    if i > 0:
        print("{}: {}".format(i, a))
