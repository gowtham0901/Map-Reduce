#Roll:21CS60R29
#Name:Banavathula Gowtham Naik
#Assignment-6
# run: cat network.txt | python mapper.py | sort | python reducer.py > result.txt

from operator import itemgetter
import sys
w2 = {}
for l in sys.stdin:
    l = l.strip()
    sender, c = l.split('\t', 1)
    try:
        c = int(c)
        w2[sender] = w2.get(sender, 0) + c
    except:
        pass
sort_w2 = sorted(w2.items(), key=itemgetter(0))

output = sorted(sort_w2, key = lambda x: x[1], reverse = True)[0:10]
# write the results to STDOUT (standard output)
for sender, c in output:
    print ('%s\t%s'% (sender, c))