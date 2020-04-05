'''
 Task1
 ..........
 
a=[]  # create an empty  list
b=a+[5,6,8,9]# concatenate it with [5,6,8,9]
print(b)    #output :[5, 6, 8, 9]

c=b+[8,9,1,5,6,7,8]# add 8,9,1,5,6,7,8
print(c) # output: [5, 6, 8, 9, 8, 9, 1, 5, 6, 7, 8]

 # find number of occurence of 8
print(c.count(8)) # output : 3

 # find avg of the list
avg=sum(c)/len(c)
print("Average of list : ",avg)  # output : Average of list :  6.5454

# find sum of list+min ele +max ele of list
print( sum(c)+min(c)+max(c)) # output : 82

# find mean,median of list

mean=sum(c)/len(c)
print("Mean : " ,mean)# output : Mean :  6.5454

c.sort()
print(c) # op:[1, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9]
median= c[len(c)//2]
print("Median : ", median) # op :Median :  7

 # remove duplicates from concatenated list and give output in tuple format

c=set(c) 
print(tuple(c)) # op :(1, 5, 6, 7, 8, 9)
........................................................................

   Task2

  #create two empty sets

set1=set()
set2=set()

  # update set1 with 7,8,9,1,2,3,4,5,0

set1.update({7,8,9,1,2,3,4,5,0})
print(set1) # op : {0, 1, 2, 3, 4, 5, 7, 8, 9}

  # update set2 with 4,5,6,0

set2.update({4,5,6,0})
print(set2) # op : {4,5,6,0}

  # check wheather set2 is subset of set1

print(set2.issubset(set1)) # op :False

   # check wheather both are disjoint

print(set1.isdisjoint(set2)) # op : False

  # remove 8 from set1

set1.remove(8)
print(set1) # op : {0, 1, 2, 3, 4, 5, 7, 9}

  # discard 0 from set2

set2.discard(0)
print(set2) # op : {4, 5, 6}

  #find sum(set1 union set2)

z=set1.union(set2)
print(sum(z)) # op :37

..................................................................................

 Task3

  # create  two tuples (1,4,5,6,7) (5,6,7,8,9)

t1=(1,4,5,6,7)
t2=(5,6,7,8,9)
  
  # concatenate two tuples after duplicate removal from both

t1=set(t1)
t2=set(t2)
t3=t1.union(t2)
t3=tuple(t3)
print((t3)) # output : (1, 4, 5, 6, 7, 8, 9)
  
  # find the index value of 9
  
index=t3.index(9)
print(index)

  # find common elements between above elements with {0,4,5}

t3=set(t3)
t4={0,4,5}
print(t3.intersection(t4)) # op :{4, 5}

  # multiple above tuple 3 times

t5=tuple(t3.intersection(t4))
print(t5*3) # op :P(4, 5, 4, 5, 4, 5)

.....................................................................

Task4
'''

 # create a dictionary {1:["english","maths","science",["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}

a={1:["english","maths","science",["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}

 # extract botany

print(a[1][3][1][4:])

 # extract "english","maths","science" from that dictionary and convert into tuple and print len
b=a[1]
print(b)
print(b.pop())
print(b)# ['english', 'maths', 'science']
b=tuple(b) 
print(b)  # ('english', 'maths', 'science')
print(len(b)) # 3
 
 # print all keys in a dictionary

print(a.keys()) # op:   dict_keys([1, 2])

 # extract "python" from dictionary

print(a[2][3][0:6])

 # add all numbers in values under key2

print(sum(a[2][0:3]))











      
