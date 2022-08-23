#Roll:21CS60R29
#Name:Banavathula Gowtham Naik
#Assignment-6

#open file
fp = open('dept_labels.txt', 'r')
fp1 = open('network.txt', 'r')
id_department = []

for l in fp:
    # to remove leading and trailing whitespace
    l = l.strip()
    # splitting the data on the basis of tab we have provided in mapper.py
    _, department = l.split(' ')
    id_department.append(department) #add the id  to deparment
fp.close() #close file


for l in fp1:
    # to remove leading and trailing whitespace
    l = l.strip()
    # splitting the data on the basis of tab we have provided in mapper.py
    w, r = l.split(' ')
    if id_department[int(w)] != id_department[int(r)]:
        #print the department id and number of outgoing emails sent by department
        print(id_department[int(w)], 1) 
fp1.close() #close file