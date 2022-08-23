#Roll:21CS60R29
#Name:Banavathula Gowtham Naik
#Assignment-6
#run: cat network.txt | python3 mapper.py | sort | python3 reducer.py > result.txt


from operator import itemgetter
import sys

def main():
   #create empty list 
  fp=[] 
  fp1=[]
  fp2=[]
  sender=[]
  receiver=[]
  # input comes from STDIN (standard input)
  for l in sys.stdin:   
    # remove leading and trailing whitespace   
    l = l.strip()
    # split the line into words
    word1, word2 = l.split('\t')
    #add the value to word1
    sender.append(word1)
    #add the value word2
    receiver.append(word2)
    #intilaize the current word is none and current count is zero
  current_w = None
  current_c = 0
  w2 = None
  #using loop the w2 is sender
  for w2 in sender:
      #intilaize the count value is one
      c=1
      # if the current word is equal to the w2 ,therefore increment  the crrent count to count
      if current_w == w2:
        current_c += c
      #if current word is nothing just append the integer of current word and current count
      else:
        if current_w:
            fp.append((int(current_w),int(current_c)))
        #after we append the value to fp the current count is count and current word is w2
        current_c = c
        current_w = w2
   #if the cuurent word is equal to w2 we append the fp tho cuurent word and current count it is none and zero we sort the receiver
  if current_w == w2:
     fp.append((int(current_w),int(current_c)))   
  current_w = None
  current_c = 0
  w2 = None
  receiver.sort()
  for w2 in receiver:
      #the count value is one
      c=1
      # current word id equal to w2 the current count is add to count
      if current_w == w2:
        current_c += c
      # otherwise append to list
      else:
        if current_w: 
            fp2.append((int(current_w),int(current_c)))
            fp1.append(int(current_w))
        current_c = c
        current_w = w2
        
  if current_w == w2:
    fp2.append((int(current_w),int(current_c)))
  #create list 
  #and find the length of fp
  list = len(fp) 
  #the list range zero and length of  fp
  for j in range(0, list):
      #k range is list of j in range to decrement -1  
      for k in range(0, list-j-1): 
            if (fp[k][1] > fp[k + 1][1]): 
                t = fp[k] 
                fp[k]= fp[k + 1] 
                fp[k + 1]= t
   #to take top-10 values
  for j in range(1,11):
      a=fp[-j][0]
      id_employee=int(a)
      index=fp1.index(id_employee)
      #print the values of the empolyee id and employees
      print ('%s\t%s' % (fp2[index][0], fp2[index][1]))
      
    
    
if __name__ == "__main__":
    main()
