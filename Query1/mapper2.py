#21CS60R29
#BANAVATHULA GOWTHAM NAIK
#ASSIGNMENT-07
import sys
for l in sys.stdin:
    l = l.strip()
    d =  l.split("\t")
    department = d[0].split()
    #w = l.split()
    print ('%s\t%s' % (department[0], 1))
    print ('%s\t%s' % (department[1], 1))