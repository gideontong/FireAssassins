"""
Program: Brute Forced Iteration
Author:  Gideon Tong
Version: Generator v4

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

keylist = open('seed/round3.txt')
filename = "TeamRandomizer.py"
i = 0

class Log(object):
    def __init__(self):
        self.terminal= sys.stdout
        self.log = open('v5_log.txt', 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Log()

for nextKey in keylist:
    i += 1
    nextKey = nextKey[0:10]
    seededGeneration = open('generates/round3/output' + nextKey + '.txt', 'w+')
    print("Testing iteration " + str(i) + " with key " + nextKey)
    seededGeneration.write("Key: " + nextKey)
    p = Popen("python3 " + filename + " " + nextKey, shell = True, stdout = seededGeneration)
    time.sleep(1)