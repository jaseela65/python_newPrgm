 #  capitalize() - it converts the first character to uppercase
 
a="python language"
print(a.capitalize())


#  casefold()  - it converts the string into lowercase

a="PYTHON languaGe"
print(a.casefold())


#  center()  - it returns a centered string

a="what is your name"
print(a.center(5))

#  count()  - returns the number of times a specified value occurs in a string

a="what is your name"
print(a.count("a"))

#  encode() -  returns an encoded version of the string

a="what is your name"
print(a.encode())

#  endswith()  -returns true if the string end with the specified value

a="what is your name"
print(a.endswith("r"))

#   expandtabs() - it sets the tab size of the string

a="p\ty\tt\th\to\tn"
print(a.expandtabs(6))

#  find() - searches the string for a specified value and returns the position of whereit was found

a="python"
print(a.find("h"))

# format() - formats specified values in a string

a="python"
print("This is {0} language !".format(a))
      
# format_map() - formats specified values in a string

# index() - searches the string for a specified value and returns the position of where it was found

a="python"
print(a.index("y"))

# isalnum()- returns true if all characters in the string are alphanumeric

a="python"
print(a.isalnum())

# isalpha()- returns true if all characters in the string are in the alphabet

a="PYTHON"
print(a.isalpha())

# isdecimal()- returns true if all characters in the string are decimals

a="6789"
print(a.isdecimal())

# isdigit()  - returns true if all characters in the string are digits

a="6789"
print(a.isdigit())

# isidentifier()  - returns true if the string is an identifier

a="Python"
print(a.isidentifier())

# islower()  - returns true if all characters in the string are lowercase

a="python"
print(a.islower())

# isnumeric()  - returns true if all characters in the string are numeric

a="6789"
print(a.isnumeric())

# isprintable()  - returns true if all characters in the string are printable

a="python is \n good"
print(a.isprintable())

# isspace()  - returns true if all characters in the string are white spaces

a="   "
print(a.isspace())

# istitle()  - returns true if  the string follows the rule of title

a="Hello Welcome"
print(a.istitle())

# isupper() -returns true if all characters in the string are upper case

a="NEW"
print(a.isupper())

#  join() - joints the elements of an iterable to the end of the string

a=["I","am","jaseela"]
print("@".join(a))

#  ljust() - returns  a left justified  version of the string

a="anu"
print(a.ljust(3)," writing python programming")

#  lower() - converts a string into a lowercase

a="pythON"
print(a.lower())

#  lstrip() - Returns a left trim version of the string

a="--pythON"
print(a.lstrip("-"))

#  partition() - returns a tuple where the string is parted into three parts

a="This is python"
print(a.partition( 'python'))

#  replace() - returns a string where a specified value is replaced with a specified value

a="python"
print(a.replace("t","x"))

#  rfind() -searches the string for a specified value and returns the last position of where it was found

a="python"
print(a.rfind("h"))

#  rindex() - searches the string for a specified value and returns the last position of where it was found

a="python"
print(a.rfind("p"))

#  rjust() - returns a right justified version of the string

a="python"
print(a.rjust(3))

#  rpartition() - returns a tuple where the string  is parted into three parts

a=" Anu like apple"
print(a.rpartition("like"))

#  rsplit() - splits the string at the specified separator, and returns a list

a="Anu is a programmer"
print(a.rsplit(" "))

# rstrip() - returns a right trim version  of the string

a="python--"
print(a.rstrip("-"))

# split() - splits the string at the specified separator, and returns a list

a="Anu is a programmer"
print(a.split(" "))

# splitlines - splits the string at line breakes and returns a list

a="Anu\n is a programmer"
print(a.splitlines())

# starswith() -returns true if the string starts with the specified value

a="Anu is a programmer"
print(a.startswith("A"))

#  strip() - returns a trimmed version of the string

a="   Anu    "
print(a.strip(" "))

#  swapcase() - in this lower cases becomes upper cases and vice versa

a="anu is a programmer"
print(a.swapcase())


#  title () - converts the first character of each word to upper case

a="anu is a programmer"
print(a.title())


# upper () - converts a string into upper case


a="Anu"
print(a.upper())

# zfill() - fills the string with a specified number of 0 values at the beginning

a="Anu is a programmer"
print(a.zfill(5))























































































































































































































                 
