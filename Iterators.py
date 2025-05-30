# Creating an iterator
a = [1, 2, 3]
b= iter(a)

print(next(b))  # Output: 1
print(next(b))  # Output: 2
print(next(b))  # Output: 3

# Using in for loop (automatically uses iterator)
for item in a:
    print(item)
    