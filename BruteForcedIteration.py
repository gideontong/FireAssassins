from subprocess import Popen
import sys

keylist = open('pwned.txt')
filename = "TeamRandomizer.py"
nextKey = keylist.readline()
i = 0

while nextKey:
    i += 1
    nextKey = nextKey[0:9]
    f = open('output' + nextKey + '.txt', 'w+')
    print("Iteration " + str(i) + "/87")
    p = Popen("python " + filename + " " + nextKey, shell = True)
    nextKey = keylist.readline()