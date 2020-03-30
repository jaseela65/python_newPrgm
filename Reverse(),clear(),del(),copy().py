

 # Difference between copy and direct assignment

    copy

    a list can be copied with equal operator
    a=[1,2,3]
    b=a.copy()

    copy()method Doesnot take any parameters.
    copy will create a new object in memory and assign the variable to that.

    a=[1,2,3]
    b=a

    the assignment operator (=) only creates a reference to an object,and
    will create a new variable referencing the same memory address.
    
 # Difference between del and clear
 
    del removes the item at a specific index:
    a=[3,2,2,1]
    del(a[1])
    print(a)

    The clear() method removes all items from the list
    a.clear()
    The clear() method does not take any parameters
    and also this method only empties the given list.it does not return any value.
    if you are using python 2 or python 3.2 and below, you cannot use the clear() method
    you can use the del operator method.
    

 # How to reverse a list?

   The reverse() method reverses the elements of a given  list.

   a=["hi","hello","welcome"]
   b=a.reverse()
   print(a)
   print(b)

   output is given below
   
   ['hi','hello','welcome']
   ['welcome','hello','hi']

   it does not take any argument.
   
   









 
 
