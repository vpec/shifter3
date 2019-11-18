import sys
import re

fr = open(sys.argv[1],"rb")
fw = open(sys.argv[1] + '.new',"wb+")

if fr.mode == 'rb':
    lines = fr.readlines()
    for l in lines:
        intervalPattern = re.compile(b"[0-9]+:[0-9]+:[0-9]+,[0-9]+ --> [0-9]+:[0-9]+:[0-9]+,[0-9]+")
        if intervalPattern.match(l) :
            print(l)
        fw.write(l)

fr.close()
fw.close()