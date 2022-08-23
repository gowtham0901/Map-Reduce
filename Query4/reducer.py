import fileinput
p = None # previous value is None
c = 0  #intilaize count is zero
m = (0, 0) #the maximum value the previous and sender is intilaize zero

for l in fileinput.input():
    # to remove leading and trailing whitespace
    l = l.strip()
    # splitting the data on the basis of tab we have provided in mapper.py
    w, r = l.split(' ') #sender and reciever split the line with comma
    if p == None: #previous is none
        p = w #previous is equal to sender 
        c = c+1 # add to the c value
    else:
        if w != p: #if sender not equal to the previous
            if c > m[1]: #if c grater than of the maximun of 1
                m = (p, c) #maximum equals to the previous ,count value
            c = 1 #if count value is 1
            p = w # previous value is sender
        else:
            c = c+1 #add to the count value to one
            p = w # previous value is sender

print(m[0], m[1]) # print maximum value