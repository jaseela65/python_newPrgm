 # Basic  Data Structures in python
'''
   1  List
   2  Tuple
   3  Set
   4  Dictionary

   List

   * indexing\ ordering possible(access the values using index).
   * duplicates possible.
   * mutable(add or remove values).

   Tuple
   
   * indexing\ordering possible.
   * duplicates possible.
   * immutable.

   Set

   * indexing\ ordering  impossible.
   * duplicates impossible.
   * mutable.

   Dictionary

   * indexing\ ordering  impossible,using keys we can access values.
   * duplicate key is impossible.
   * mutable.

 How to create a list?

a=[1,"hi",2,3,"hello",4]
print(a)
print(type(a))
print(len(a))
print(a[0])#access index values
a.append("welcome")# mutable
print(a)

output
............
[1, 'hi', 2, 3, 'hello', 4]
<class 'list'>
6
1
[1, 'hi', 2, 3, 'hello', 4, 'welcome']

List methods ?

We can add one item to a list using append() method or add several items using extend() method.


   1,  extend()

                a=[1,"hi",2,3,"hello",4]
                a.extend([999,88,55])
                print(a)

               output
               ............

                [1, 'hi', 2, 3, 'hello', 4, 999,88,55]

    2, insert()- we can insert one item at a desired location by using the method insert().

               a= [1, 9]
              a.insert(1,3)

              # Output: [1, 3, 9] 
               print(a)

               a[2:2] = [5, 7]

              # Output: [1, 3, 5, 7, 9]
               print(odd)

    3,   delete() - We can delete one or more items from a list using the keyword del.
                 It can even delete the list entirely.

           a=[1,"hi",2,3,"hello",4,9,88]

           # delete one item
            del a[2]

           # Output: [1,"hi",3,"hello",4,9,88]
           print(a)

           # delete multiple items
           del a[1:5]  

           # Output: [1,9,88]
            print(a)

           # delete entire list
              del a


    4,  remove() - We can use remove() method to remove the given item.

          a=[1,"hi",2,3,"hello",4,9,88]
          a.remove("hi")

          # Output: [1,,2,3,"hello",4,9,88]
          print(my_list)


    5,  pop() - this method to remove an item at the given index.

    a=[1,"hi",2,3,"hello",4,9,88]
    print(a.pop(4))

   # Output:[1,"hi",2,3,4,9,88]
    print(a)
    
    print(a.pop())
    print(a)
    # Output:[1,"hi",2,3,4,9]
    

    
    6, clear()- We can also use the clear() method to empty a list.

    a=[1,"hi",2,3,"hello",4,9,88]  
    a.clear()

   # Output: []
    print(a)

    7,index() - Returns the index of the first matched item
    
    8,count() - Returns the count of number of items passed as an argument
    
    9,sort() - Sort items in a list in ascending order
    
    10,reverse() - Reverse the order of items in the list

       a = [3, 8, 1, 6, 0, 8, 4]

      print(a.index(8))# Output: 1

      print(a.count(8)) # Output: 2

      a.sort()
      print(a) # Output: [0, 1, 3, 4, 6, 8, 8]

      a.reverse()
      print(a)# Output: [8, 8, 6, 4, 3, 1, 0]

    
    11,copy() - Returns a shallow copy of the list also called shallow copy.

      a = [3, 8, 1, 6, 0, 8, 4]
      b= a.copy()
      
      print(a)  Output:  [3, 8, 1, 6, 0, 8, 4]
      print(b) Output:   [3, 8, 1, 6, 0, 8, 4]
      
      a[1]=9
      print(a) Output:  [3, 9, 1, 6, 0, 8, 4]
      print(b) Output:    [3, 8, 1, 6, 0, 8, 4]
.........................................................................................

      Tuple

       How to create a tuple?

       # Empty tuple
       a = ()
       print(a)  # Output: ()

      # Tuple having integers
       a = (1, 2, 3)
       print(a)  # Output: (1, 2, 3) 

      # tuple with mixed datatypes
      a = (1, "Hello", 3.4)
      print(a)  # Output: (1, "Hello", 3.4)


      Tuple methods

      1, concatenation(+) and multiplication(*)

      t1=(1,2,3)
      t2=(2,3,4)
      t3=t1+t2  
      print(t3) # Output: (1,2,3,2,3,4)
      t4=t1*2
      print(t4) # Output: (1,2,3,1,2,3)

     2, assignment
       
     t1=(1,2,3,4,5)
     t2=t1[2:4]
     print(t2) # Output: (3,4)
     

     3, count()	-Returns the number of items
     
     4,index(x)- Returns the index of the first item that is equal to x

     a = ('a','p','p','l','e',)

     print(a.count('p'))  # Output: 2
     print(a.index('l'))  # Output: 3

..............................................................................     

    Set

    How to create a set?

    # set of integers
    a = {1, 2, 3}
    print(a) # Output:{1, 2, 3}

    # set of mixed datatypes
     a = {1.0, "Hello", (1, 2, 3)}
     print(a) # Output: {1.0, 'Hello', (1, 2, 3)}


     Set Methods

     1, add()-	Adds an element to the set

         a={2,3,4,5}
         a.add(6)
         print(a) # output : {2,3,4,5,6}

     2, update()- Updates the set with the union of itself and others

        a={2,3,4,5,6}
        a.update({4,5,6,7,8,9})
        print(a) # output : {2,3,4,5,6,7,8,9}

    3,  remove() -Removes an element from the set. If the element is not a member, raise a KeyError
        
        a={2,3,4,5,6}
        a.remove(4)
        print(a) # output : {2,3,5,6}

        a.remove(8)
        print(a) # output : show error

    4, discard()- Removes an element from the set if it is a member,
                   (Do nothing if the element is not in set).

        a={2,3,5,6}
        a.discard(5)
        print(a) # output : {2,3,6}

    5, pop()- Removes and returns an arbitary set element. Raise KeyError if the set is empty

        a={2,3,4}
        a.pop()
        print(a) # output : {3,4}
        
    6, clear() - Removes all elements from the set  ,empty the set

        a={2,3,4}
        a.clear()
        print(a) # output : {}

    7, copy() - Returns a copy of the set.

        a={2,3,4}
        b=a.copy()
        print(b) # output : {2,3,4}

    8, union()-	Returns the union of sets in a new set

         a={2,3,4}
         b={9,8,74}
         c=a.union(b)
         print(a) # output : {2,3,4,9,8,74}

    9, intersection()- 	Returns the intersection of two sets as a new set.(A n B).

         a={2,3,4}
         b={4,8,74}
         print(a.intersection(b)) # output : {4}

     10, intersection_update()- Updates the set with the intersection of itself and another          

         a={2,3,4}
         b={4,8,74}
         print(a.intersection_update(b)) # output : None
         print(b.intersection_update(a)) # output : None

     11, difference() - Returns the difference of two or more sets as a new set(A-B)
     12, difference_update() - Removes all elements of another set from this set
          
          a={1,2,3,4}
          b={3,4,8,74}
          print(a.difference(b)) # output : {1,2}
          print(a.difference_update(b)) # output : None
          print(b.difference_update(a)) # output : None

      13, symmetric_difference() - Returns the symmetric difference of two sets as a new set(AuB -Anb)
      14, symmetric_difference_update()-Updates a set with the symmetric difference of itself and
      another

          a={1,2,3,4}
          b={3,4,8,74}
          print(a.symmetric_difference(b)) # output : {1,2,8,74}
          print(a.symmetric_difference_update(b)) # output : None
          print(b.difference_update(a)) # output : None

      15, isdisjoint()-	Returns True if two sets have a null intersection
      16,issubset() -Returns True if another set contains this set
      17,issuperset()-Returns True if this set contains another set

          a={2,3,4,5,6,7}
          b={2,3}
          print(a.issuperset(b)) # output : True
          print(b.issuperset(a)) # output : False
          print(a.issubset(b)) # output : False
          print(b.issubset(a)) # output : True
          c={8,9}
          print(a.isdisjoint(b)) # output : False
          print(b.isdisjoint(a)) # output : True
          
................................................................................................   


   Dictionary


   # empty dictionary
    a = {}

  # dictionary with integer keys
    a = {1: 'apple', 2: 'ball'}

    Dictonary Methods

    1, clear()	-Remove all items form the dictionary.
    2, copy()	-Return a shallow copy of the dictionary.

      a = {1: 'apple', 2: 'ball'}
      b=a.copy()
      print(a) # output : {1: 'apple', 2: 'ball'}
      print(b) # output : {1: 'apple', 2: 'ball'}
      print(a.clear())# output : {}

    3, items()- Return a new view of the dictionary's items (key, value).
    4, keys() -	Return a new view of the dictionary's keys.
    5, values()-Return a new view of the dictionary's values

           a = {1: 'apple', 2: 'ball',3:'go',4:499}
           
           print(a.keys())  # output : dict_keys([1, 2, 3, 4])
           print(a.values())# output : dict_values(['apple', 'ball', 'go', 499])
           print(a.items())  # output : dict_items([(1, 'apple'), (2, 'ball'), (3, 'go'), (4, 499)])

    6, fromkeys(seq[, v]) - Return a new dictionary with keys from seq and
                            value equal to v (defaults to None).
    7, get(key[,d]) - Return the value of key. If key doesnot exit, return d (defaults to None).

      a = {1: 'apple', 2: 'ball',3:'go',4:499}
      print(a.get(4)) # output : 499

        # vowels keys
      keys = {'a', 'e', 'i', 'o', 'u' }
      value = [1]

      vowels = dict.fromkeys(keys, value)
      print(vowels) # output : {'i': [1], 'a': [1], 'e': [1], 'u': [1], 'o': [1]}

      # updating the value
      value.append(2)
       print(vowels) # output : {'i': [1, 2], 'a': [1, 2], 'e': [1, 2], 'u': [1, 2], 'o': [1, 2]}

   8, pop(key[,d])  - Remove the item with key and return its value or d if key is not found.
                      If d is not provided and key is not found, raises KeyError.
   9, popitem()  - Remove and return an arbitary item (key, value).
                  Raises KeyError if the dictionary is empty.

        a = {1: 'apple', 2: 'ball',3:'go',4:499,5:'welcome'}

        a.pop(2)
        print(a) # output: {1: 'apple',3:'go',4:499,5:'welcome'}

        a.popitem()
        print(a) # output: {1: 'apple',3:'go',4:499}
        
                  
   10, setdefault(key[,d]) -If key is in the dictionary, return its value. 
                           If not, insert key with a value of d and return d (defaults to None).'''

            a = {1: 'apple', 2: 'ball',3:'go',4:499,5:'welcome'}
            b=a.setdefault('colour','red')
            print(b) # output : red
                      
  11, update([other]) -	Update the dictionary with the key/value pairs from other, overwriting
                        existing keys.

          d = {1: "one", 2: "three"}
          d1 = {2: "two"}

          # updates the value of key 2
          d.update(d1)
          print(d)

          d1 = {3: "three"}

         # adds element with key 3
         d.update(d1)
         print(d)

.....................................................................................................         

      
 

   



        





        

        
         




     
     
      
      
      




    













 






      
      
      













   
  
