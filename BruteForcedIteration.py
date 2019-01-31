from subprocess import Popen
import sys

keylist = open('SeedsRound1.txt')
filename = "TeamRandomizer.py"
nextKey = keylist.readline()

while nextKey:
    nextKey = nextKey[0:9]
    f = open('output' + nextKey + '.txt', 'w+')
    print("Now attempting key: " + nextKey)
    p = Popen("python " + filename + " " + nextKey, shell = True)
    nextKey = keylist.readline()