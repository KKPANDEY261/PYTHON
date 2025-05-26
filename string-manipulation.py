s = "Hello, World!"

# Indexing and slicing
print(s[0])      # 'H'
print(s[7:12])   # 'World'
print(s[::-1])   # Reversed string
# Common methods
print(s.lower())       # hello, world!
print(s.upper())       # HELLO, WORLD!
print(s.split(','))    # ['Hello', ' World!']
print(s.replace('H', 'J'))  # Jello, World!
print(len(s))          # 13
print("Hello" in s)   # True