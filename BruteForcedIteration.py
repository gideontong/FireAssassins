from subprocess import Popen
import sys

keylist = open('SeedsRound1.txt')
filename = "TeamRandomizer.py"
nextKey = keylist.readline()

while nextKey:
    nextKey = nextKey[0:9]
    print("Now attempting key: " + nextKey)
    p = Popen("python " + filename + " " + nextKey, shell = True, stdout='output'+nextKey)
    nextKey = keylist.readline()