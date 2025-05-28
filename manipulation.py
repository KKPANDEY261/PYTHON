#string manipulation

s = "Hello, World!" 
# Indexing and slicing
print(s[0])      # 'H'
print(s[7:12])   # 'World'             
s = "Hello, World!"                    # H, e, l, l, o,,, ,w,o,r,l,  d, !
print(s[-1:-6:-1])   # Reversed string    
#print(s[start:stop:steps])
# Common methods
print(s.lower())       # hello, world!
print(s.upper())       # HELLO, WORLD!
print(s.split(','))    # ['Hello', ' World!']
print(s.replace('H', 'J'))  # Jello, World!
print(len(s))          # 13
print("Hello" in s)   # True


# list manipulation
#Creating Lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]


#Basic Operations
# Accessing elements
numbers = [1, 2, 3, 4, 5]
print( numbers[0])        # 1
print( numbers[-1])        # 5
print (nested[0][1])        #2
print (nested[1][0])          #3


# Slicing
print(numbers[1:4])     # [2, 3, 4]
print(numbers[::2]) # [1, 3, 5]

# Length
print(len(numbers))     # 5


#Modifying Lists
# Adding elements
numbers.append(6) 
print(numbers)        # [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5) 
print(numbers)   # [1, 2, 2.5, 3, 4, 5, 6]
numbers.extend([7, 8]) 
print(numbers)   # [1, 2, 2.5, 3, 4, 5, 6, 7, 8]

# Removing elements
numbers.remove(2.5)
print(numbers)       # [1, 2, 3, 4, 5, 6, 7, 8]
numbers.pop()
print(numbers)    # 8, list is now [1, 2, 3, 4, 5, 6, 7]
del numbers[0]
print(numbers)            # [2, 3, 4, 5, 6, 7]

# Modifying elements
numbers[0] = 100
print(numbers)         # [100, 3, 4, 5, 6, 7]



#Creating Tuples
#tupple manupulation

# Empty tuple
empty_tuple = ()

# Single element tuple (note the trailing comma)
single_tuple = (42,)

# Multiple elements
my_tuple = (1, 2, 3, 'a', 'b')


#Accessing Elements
t = (10, 20, 30, 40, 50)

# Indexing
print(t[0])   # 10
print(t[-1])  # 50

# Slicing
print(t[1:4]) # (20, 30, 40)


#Tuple Operations
# Concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = t1 * 3   # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership
print(2 in t1)      # True
print(7 not in t1)  # True


#Tuple Methods
t = (1, 2, 3, 2, 4, 2)

# Count occurrences
print(t.count(2))   # 3

# Get index of first occurrence
print(t.index(3))   # 2


#Unpacking Tuples
# Basic unpacking
point = (10, 20)
x, y = point
print(x, y)  # 10 20

# Extended unpacking (Python 3+)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

#Converting Between Tuples and Other Types
# List to tuple
lst = [1, 2, 3]
t = tuple(lst)  # (1, 2, 3)

# String to tuple
s = "hello"
t = tuple(s)    # ('h', 'e', 'l', 'l', 'o')

# Tuple to list
lst = list(t)   # ['h', 'e', 'l', 'l', 'o']



# set manupulation
#Creating Sets

# Set with elements
fruits = {'apple', 'banana', 'cherry'}
numbers = {1, 2, 3, 4, 5}

# Creating set from a list (removes duplicates)
colors = set(['red', 'blue', 'green', 'blue', 'red'])


#Basic Operations
# Add elements
fruits.add('orange')

# Remove elements
fruits.remove('banana')  # Raises KeyError if element doesn't exist
fruits.discard('banana')  # Doesn't raise error if element doesn't exist

# Length of set
print(len(fruits))  # Output: 3

# Check membership
print('apple' in fruits)  # Output: True

# Clear all elements
fruits.clear()


#Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (elements in either set)
print(a | b)  # {1, 2, 3, 4, 5, 6}
print(a.union(b))  # same as above

# Intersection (elements in both sets)
print(a & b)  # {3, 4}
print(a.intersection(b))  # same as above






#Dictionaries 
#Creating a Dictionary

# Dictionary with initial values
person = {
    "name": "satyam",
    "age": 30,
    "city": "kolkata"
}

# Using dict() constructor
another_dict = dict(name="amit", age=25, city="howrah")


#Accessing Values
print(person["name"])  # Output: satayam
print(person.get("age"))  # Output: 30
print(person["age"])

# Safely access with default if key doesn't exist
person = {
    "name": "satyam",
    "age": 30,
    "city": "kolkata"
}
print(person.get("occupation", "Not Found"))  # Output: Not Found


#Modifying a Dictionary
# Add new key-value pair
person["occupation"] = "Engineer"

# Update existing value
person["age"] = 31

# Update multiple items
person.update({"age": 32, "city": "howrah"})

#Dictionary Methods
# Get all keys
keys = person.keys()  
print(keys)# dict_keys(['name', 'age', 'city', 'occupation'])

# Get all values
values = person.values()
print(values)

# Get all key-value pairs
items = person.items()
print(items)

# Remove item by key
age = person.pop("age")
print(person)


# Remove last inserted item (Python 3.7+)

last_item = person.popitem()
print(last_item)
 
# Check if key exists
if "name" in person:
    print("Name exists")

# Clear dictionary
person.clear()

