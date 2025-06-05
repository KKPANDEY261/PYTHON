




try:
 a=(input("enter your value :-"))
 for e in range(1,11):
    print(int(a)*e)
except Exception as b:
 print(b)

print("welcome")
print("hello")


















































"""Main Exception Categories
1. System Exit Related Exceptions
SystemExit - Raised when sys.exit() is called

KeyboardInterrupt - Triggered when user presses Ctrl+C

2. Standard Errors
Exception - Base class for all built-in, non-system-exiting exceptions

3. Common Built-in Exceptions
a) Arithmetic Errors
ZeroDivisionError - Division or modulo by zero

OverflowError - Result too large to be represented

FloatingPointError - Floating point operation fails

b) Value/Type Errors
ValueError - Invalid value (e.g., int('abc'))

TypeError - Operation on wrong type (e.g., '5' + 5)

AttributeError - Attribute reference fails

c) Sequence/Collection Errors
IndexError - Sequence index out of range

KeyError - Dictionary key not found

StopIteration - Iterator has no more items

d) File/IO Errors
FileNotFoundError - File doesn't exist

IOError - I/O operation fails

PermissionError - No permission to access resource

e) Memory/System Errors
MemoryError - Out of memory

OSError - OS system call fails

f) Other Important Exceptions
ImportError - Module import fails

IndentationError - Incorrect indentation

NameError - Undefined variable used

NotImplementedError - Abstract method not implemented

RuntimeError - Generic runtime errors"""