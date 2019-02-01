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