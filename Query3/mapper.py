#Roll:21CS60R29
#Name:Banavathula Gowtham Naik
#Assignment-6
#run:  cat network.txt | python3 mapper.py | sort | python3 reducer.py > result.txt

import sys


def main():
    # input comes from STDIN (standard input)
  for l in sys.stdin:
      # remove leading and trailing whitespace
    l = l.strip()
    # split the line into words
    sender = l.split()
    # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
    print ('%s\t%s' % (sender[0], sender[1]))

    
if __name__ == "__main__":
    main()