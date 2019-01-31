from subprocess import Popen
import sys

key = 1548716400

filename = "TeamRandomizer.py"
while True:
    print("\nNow attempting key: " + str(key))
    p = Popen("python " + filename + " " + str(key), shell = True)
    key += 1
    p.wait()