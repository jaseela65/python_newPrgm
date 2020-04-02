list1=["hi",1,2,"welcome"]
tuple1=(1,2,5,"python")
set1={33,"hello",99}


#   conversion of list to tuple

a=tuple(list1)
print("converting list to tuple :",a)

# output-  converting list to tuple : ('hi', 1, 2, 'welcome')
.......................................................................

#   conversion of list to set

a=set(list1)
print("converting list to set :",a)

#output-  converting list to set : {1, 'hi', 2, 'welcome'}

......................................................................

#   conversion of tuple to list

a=list(tuple1)
print("converting tuple to list :",a)

#output-   converting tuple to list : [1, 2, 5, 'python']

......................................................................

#   conversion of tuple to set

a=set(tuple1)
print("converting tuple to set :",a)

# output -   converting tuple to set : {1, 2, 5, 'python'}

.......................................................................

#   conversion of set to list

a=list(set1)
print("converting set to list :",a)

# output - converting set to list : [33, 'hello', 99]

.......................................................................

#   conversion of set to tuple

a=tuple(set1)
print("converting set to tuple :",a)

# output -converting set to tuple : (33, 99, 'hello')


..........................................















































