"""
file handling 
a=open("hello.txt")  

file modes (r,w,x,a,rt,b,+)

"r" means open a file in mode .
"w" means open a file in write mode (truncate). if file does not exist then create it.
"x"means open a file exclusive creation. if file already exist then operation fails.
"a" means open a file in appending mode at the end of file without truncating. create a new file if doesn't exist.
"b" open in binary mode.
"+" open a file for updating.
"t" means define a file is text mode.
"""
f=open("function.py","r")
a=f.read()
print(a)
f.close()

file = open("example.txt", "w")
file.write("New conten")
file.close()

file = open("newfile.txt", "x")
file.write("Content")
file.close()


file = open("example.txt", "a")
file.write("\n Appended content")
file.close()

file = open("function.py","rt")  
a=file.read()
print(a)
file.close()

file = open("newfile.txt","")  
file.write(b'\x68\x65\x6C\x6C\x6F')
a=file.read()
print(a)
file.close()



