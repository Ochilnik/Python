import sys
import subprocess
# sys.argv[1]
f =  open('oldFiles.txt')
lines = f.readlines()
f.close()
for line in lines:
    old = line.strip()
    print(old)
    new = old.replace("jane", "jdoe")
    print(new)
    #result = subprocess.run("rename", old, new)
# mv source destination
# f.close()