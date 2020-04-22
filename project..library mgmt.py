#Library Management From User and Admin ends

#admmin add books
Python_Crash_Course={
    "Author": "Eric Matthes",
    "published": "20 November 2015",
    "Description":"Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming"
    }
Programming_with_Java={
    "Author":"E. Balagurusamy",
    "published":1998,
    "Description":"Programming with Java,4e , gives an excellent account of the fundamentals of Java Programming"
    }
books={
    "Python_Crash_Course":Python_Crash_Course,
    "Programming_with_Java":Programming_with_Java
    }
a=books["Python_Crash_Course"]
print(a)

#admin add user
a1001={
    "name":"John",
    "DOB":"12/Apr/1993"
    }
a1002={
    "name":"Tom",
    "DOB":"8/Jan/1992"
    }
a1003={
    "name":"Deepa",
    "DOB":"10/Feb/1992"
    }
user={
    "a1001":a1001,
    "a1002":a1002,
    "a1003":a1003,
    }
x=user["a1001"]
print(x)
    
