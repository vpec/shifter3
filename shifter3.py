import sys
import re
import datetime

# Arguments:
#   argv[1] -> input str file
#   argv[2] -> shift value

fr = open(sys.argv[1],"rb")
fw = open(sys.argv[1] + '.new',"wb+")
# Get shift parameter
shift = float(sys.argv[2])

if fr.mode == 'rb':
    # Get lines from file
    lines = fr.readlines()
    # Create regex pattern for recognizing timestamp lines
    intervalPattern = re.compile(b"[0-9]+:[0-9]+:[0-9]+,[0-9]+ --> [0-9]+:[0-9]+:[0-9]+,[0-9]+")
    for l in lines:
        if intervalPattern.match(l) :
            # Create a list with all numbers in line
            numberslist = re.findall(r'\d+', str(l, 'utf-8'))
            # Divide list in two
            list1 = numberslist[:4]
            list2 = numberslist[4:]
            # Get seconds from string
            secs1 = float(list1[0])*3600 + float(list1[1])*60 + float(list1[2]) + float(list1[3]) / 1000.0
            secs2 = float(list2[0])*3600 + float(list2[1])*60 + float(list2[2]) + float(list2[3]) / 1000.0
            # Apply shift
            new_secs1 = secs1 + shift
            new_secs2 = secs2 + shift
            # Check that timestamp is never negative
            if new_secs1 < 0.0 :
                new_secs1 = 0.0
            if new_secs2 < 0.0 :
                new_secs2 = 0.0
            # Get integer part from seconds float
            int_new_secs1 = int(new_secs1)
            int_new_secs2 = int(new_secs2)
            # Compose new time strings
            new_time1str = str(datetime.timedelta(seconds=int_new_secs1)) + "," + "{0:.3f}".format(new_secs1 - int_new_secs1)[2:]
            new_time2str = str(datetime.timedelta(seconds=int_new_secs2)) + "," + "{0:.3f}".format(new_secs2 - int_new_secs2)[2:]
            # Add another left zero to hours if necessary
            if len(new_time1str) < 12 :
                new_time1str = "0" + new_time1str
            if len(new_time2str) < 12 :
                new_time2str = "0" + new_time2str
            # New full string
            new_str = new_time1str + ' --> ' + new_time2str + '\r\n'
            # Write new full string to file
            fw.write(bytes(new_str, 'utf-8'))
        else :
            # Write line to file
            fw.write(l)
# Close files
fr.close()
fw.close()
print("Shifted " + str(shift) + " seconds")