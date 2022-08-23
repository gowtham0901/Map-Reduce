#21CS60R29
#BANAVATHULA GOWTHAM NAIK
#ASSIGNMENT-07
from operator import itemgetter
import sys
w2c = {}
for l in sys.stdin:
    l = l.strip()
    w, c = l.split('\t', 1)
    try:
        c = int(c)
        w2c[w] = w2c.get(w, 0) + c
    except:
        pass
sorted_w2c = sorted(w2c.items(), key=itemgetter(0))
for w, c in sorted_w2c:
    print('%s\t%s'% (w, c))