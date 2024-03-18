
import os
import re

directory = 'd:\downloads'
files = []
sfile = ''
files = os.listdir(directory)
#print(files)
for file in files:
    if re.search(r'.txt$',file) and file != 'subtitle.txt':
        sfile = file
#print(sfile)

name = sfile[:-4]
#print(name)

nname = directory + '\\' + name + '_1.txt'
#print(nname)

os.rename('d:/downloads/subtitle.txt', nname)
