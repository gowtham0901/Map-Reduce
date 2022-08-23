#Roll:21CS60R29
#Name:Banavathula Gowtham Naik
#Assignment-6
#run:cat network.txt | python mapper.py | sort | python reducer.py > result.txt

import sys
for l in sys.stdin:
    sender = l.split() #split line
    print ('%s\t%s' % (sender[0], 1))#employee sender count is equal to 1