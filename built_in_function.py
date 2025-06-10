#Built_in_function
 
#chr()
#convert ASCII VALUE 

a=0
for i in range(300):
    b=chr(i)
    print(a,":-",b)
   
    a+=1

c=ord("i")
print(c)

#cmp
#compare values beetween two dictionaries  , this function is not working after 3.0 version

"""dic1={1:100,2:200,3:300,4:400}
dic2={2:100,1:200,3:300,4:400}
dic3={1:100,2:200,3:300,4:400}
dic4={2:100,1:200,3:300,4:400}
dic5={1:100,2:200,3:300,4:400}
dic6={2:100,1:200,3:300,4:400}
y=cmp(dic1,dic2)
print(y)"""


# compile
"""compile() function in Python is a built-in function that converts 
source code into a compiled code object,
"exec" → For multiple statements (e.g., a full script).  

code = x = 10   
y = 20
print(x + y)


"eval" → For a single expression (returns a value).

"5+3+8"

"single" → For a single interactive statement.

print("hello")

"""

code = """
x = 10
y = 20
print(x + y)
"""
compiled_code = compile(code, 'sum', 'exec')
exec(compiled_code)  # output: 30


#eval

eval('print("Hello World")') 
a=eval("5+6+7+8")
print(a)




# dir
"""dir() is a built-in function that returns a list of attributes
 and methods of an object. """
import math
print(dir(math))

print(dir())




#filter
"""
filter() function in Python is a built-in function that constructs 
an iterator from elements of an iterable for which a function 
returns true.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    return num % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

values = [0, 1, False, True, None, "hello", "", "world"]
filtered_values = filter(None, values)
print(list(filtered_values))  # Output: [1, True, 'hello', 'world']

# hash
"""
hash() function in Python is a built-in function that returns a hash value 
(an integer number) for a given object.
"""


# For strings
print(hash("hello"))  # Example: -1182655621198502216

# For integers
print(hash(42))       # Will return 42 itself

# For floats
print(hash(3.14))     # Example: 322818021289917443

# For tuples
print(hash((1, 2)))   # Example: -3550055125485641917

# For lists (will raise error as lists are mutable)
# print(hash([1, 2]))  # TypeError: unhashable type: 'list'

#input
"""
input() function in Python is used to take user input
"""
name = input("Enter your name: ")  
print("Hello, " + name)  

#len
"""
len() function is a built-in Python function that returns 
the length (number of items) of an object such as a string, 
list, tuple, dictionary, etc.
"""

# Length of a string
text = "Hello"
print(len(text))  # Output: 5 (since "Hello" has 5 characters)

# Length of a list
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5

# Length of a tuple
fruits = ('apple', 'banana', 'orange')
print(len(fruits))  # Output: 3

# Length of a dictionary
person = {'name': 'Rahul', 'age': 25, 'city': 'Mumbai'}
print(len(person))  # Output: 3 (because there are 3 key-value pairs)


#locals
"""
locals() is a built-in function that returns a dictionary 
representing the current local symbol table. This dictionary 
contains the names and values of all local variables in the 
current scope.
"""
def example():
    num = 42
    text = "Hello"
    print(locals())  # output : {'num': 42, 'text': 'Hello'}

example()

num = 42
text = "Hello"
print(locals())


#long
""" 
long() was a function used in Python 2 to represent long integers
"""


#max
"""
max() function is a built-in Python function that returns 
the largest item from an iterable or from two or more arguments.
"""

numbers = [10, 20, 5, 30, 15]
largest = max(numbers)
print(largest)  # Output: 30

words = ["apple", "banana", "cherry", "date"]
longest_word = max(words, key=len)
print(longest_word)  #


#pow
"""pow() function in Python is a built-in function that calculates 
the power of a number."""


print(pow(2, 3))  # Output: 8


print(pow(5, 2))  # Output: 25


print(pow(10, 0))  # Output: 1

#range
"""range() function in Python is a built-in function that 
generates a sequence of numbers. """
 
a=range(1,10)
print(list(a))
b=range(1,20,2)
print(list(b))

#slice
"""
slice() function in Python is a built-in function that returns a
slice object. This object can be used to extract a portion (slice) 
of a sequence (such as a list, tuple, or string)."""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# slice(2, 5) means from index 2 to 4 (5 is excluded)
s = slice(2, 5)
print(my_list[s])  # Output: [3, 4, 5]

#tuple
"""
tuple() function is a built-in Python function that creates a 
tuple. Tuples are immutable (unchangeable) and ordered sequence 
data structures.
"""

# Direct tuple creation (with parentheses)
numbers = [10, 20, 30]
print(tuple(numbers))  # Output: (10, 20, 30)

# Creating tuple from dictionary
dict_data = {'a': 1, 'b': 2}
print(tuple(dict_data))  # Output: ('a', 'b') - only takes keys


#Unicode
"""
unicode() function in Python was used to convert a given 
object into a Unicode string.
"""
# Python 3 
text = "hello"
print(text)  # output : hello
#"hello" = b'\\u0928\\u092e\\u0938\\u094d\\u0924'

# vars

"""
vars() function is a built-in Python function that returns 
the __dict__ attribute of an object.
"""

x = 10
y = "Hello"
print(vars())  # Shows variables in local scope as a dictionary


