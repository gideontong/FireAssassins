"""
Program: Brute Forced Iteration
Author:  Gideon Tong

Description
===========
This program is very similar to BruteForce.py, except in the sense that it doesn't actually
brute force through a sequence of values in order to find possible keys. Instead it takes
an input (in this case, pwned.txt) and iterates through it to find more detailed outputs,
sometimes not analyzing them but puting them into a certain output in order to be analyzed
further without regenerating the lists or for some other purpose.
"""

from subprocess import Popen
import sys
import time

keylist = open('pwned.txt')
filename = "TeamRandomizer.py"
i = 0

for nextKey in keylist:
    i += 1
    nextKey = nextKey[0:10]
    f = open('generates/output' + nextKey + '.txt', 'w+')
    print("Iteration " + str(i) + "/87 with key " + nextKey)
    f.write("Key: " + nextKey)
    p = Popen("python " + filename + " " + nextKey, shell = True, stdout=f)
    time.sleep(1)