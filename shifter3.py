import sys
import re

# Arguments:
#   argv[1] -> input str file
#   argv[2] -> shift value

fr = open(sys.argv[1],"rb")
fw = open(sys.argv[1] + '.new',"wb+")
shift = float(sys.argv[2])

if fr.mode == 'rb':
    lines = fr.readlines()
    for l in lines:
        intervalPattern = re.compile(b"[0-9]+:[0-9]+:[0-9]+,[0-9]+ --> [0-9]+:[0-9]+:[0-9]+,[0-9]+")
        if intervalPattern.match(l) :
            # print binary stream
            print(l)
            # Transform binary stream to string
            lstr = str(l, 'utf-8')
            # Create a list with all numbers in lstr
            numberslist = re.findall(r'\d+', lstr)
            # Insert dots in list to make conversion to float easier
            numberslist.insert(3, '.')
            numberslist.insert(8, '.')
            # Join each numbersList into a single string
            time1str = ''.join(numberslist[:5])
            time2str = ''.join(numberslist[5:])
            # Convert string to float
            time1f = float(time1str)
            time2f = float(time2str)
            # Print strings
            print(time1str)
            print(time2str)
            # Print floats
            print(time1f)
            print(time2f)
            # Print floats + shift (rounded at miliseconds)
            new_time1f = round(time1f + shift, 3)
            new_time2f = round(time2f + shift, 3)
            print(new_time1f)
            print(new_time2f)
            # Get the new time string (adding zeros to the left if necessary)
            new_time1str = '0' * (len(time1str) - len(str(new_time1f))) + str(new_time1f)
            new_time2str = '0' * (len(time2str) - len(str(new_time2f))) + str(new_time2f)
            print(new_time1str)
            print(new_time2str)
            o = len(time1str) - 10 # Necessary if hours > 99
            new_time1str = new_time1str[:(2 + o)] + ':' +  new_time1str[(2 + o):(4 + o)] + ':' +  new_time1str[(4 + o):]
            new_time1str = new_time1str.replace('.', ',')
            new_time2str = new_time2str[:(2 + o)] + ':' +  new_time2str[(2 + o):(4 + o)] + ':' +  new_time2str[(4 + o):]
            new_time2str = new_time2str.replace('.', ',')
            print(new_time1str)
            print(new_time2str)
        fw.write(l)

fr.close()
fw.close()