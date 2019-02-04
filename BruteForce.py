"""
Program: Brute Force
Author:  Gideon Tong
Version: Generator v5

Description
===========
This program iterates through a list of keys from the starting value to the target, hence the name
brute force, because it is brute forcing for a certain value. It displays this output, which is
traditionally piped to a text file using the pipe selector or the alligator selector, and is used
for analysis at a later time.
"""

from subprocess import Popen
import sys

# key = 1548716400
key = 1548718999
# realTarget = 1548727920
target = 1548727920

filename = "TeamRandomizer.py"

while key < target:
    print("Now attempting key: " + str(key))
    p = Popen("python3 " + filename + " " + str(key), shell = True)
    key += 1
    p.wait()