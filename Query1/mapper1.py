#21CS60R29
#BANAVATHULA GOWTHAM NAIK
#ASSIGNMENT-07
import sys
for l in sys.stdin:
    l = l.strip()
    w = l.split()
    r = w[1] + ' ' + w[0]
    if(w[0] != w[1]):
        if(w[0] < w[1]):
            print ('%s \t %s'%(l,1))
        else:
            print ('%s\t%s' % (r, 1))