import sys

fr = open(sys.argv[1],"rb")
fw = open(sys.argv[1] + '.new',"wb+")

if fr.mode == 'rb':
    lines = fr.readlines()
    for l in lines:
        fw.write(l)

fr.close()
fw.close()