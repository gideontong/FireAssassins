from subprocess import Popen
import sys

key = 1548716400
target = 1548727920

filename = "TeamRandomizer.py"

while key < target:
    print("Now attempting key: " + str(key))
    p = Popen("python " + filename + " " + str(key), shell = True)
    key += 1
    p.wait()