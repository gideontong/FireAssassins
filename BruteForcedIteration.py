from subprocess import Popen
import sys
import time

keylist = open('pwned.txt')
filename = "TeamRandomizer.py"
i = 0

for nextKey in keylist:
    i += 1
    nextKey = nextKey[0:9]
    '''f = open('output' + nextKey + '.txt', 'w+')'''
    print("Iteration " + str(i) + "/87 with key " + nextKey)
    p = Popen("python " + filename + " " + nextKey, shell = True)
    nextKey = keylist.readline()
    time.sleep(1)