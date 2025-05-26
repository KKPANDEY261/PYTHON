#for loop
#for loop with range
for i in range(10):
  print("for loop in range:-",i) 

for i in range(1,10):
  print("for loop in range with start point:- ",i)

ind=0
for i in range(1,10):
  if i==5:
   print("find index in range:- ",ind)
  ind+=1


for i in range(1,10,2):
  print("for loop in range with start point and step:- ",i)

for i in range(10,1,-2):
  print ("for loop in range with start and negative step:- ",i)


#for loop with list
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
  print ("for loop in list:-",i)


# for loop with list 
for i in list:
  print ("for loop with else:-",i)
else:
  print ("for loop with else:-","end")


# for loop with string 

str="Welcome"
for i in str:
  print(i)


ind=0
for i in str:
  if i=="o":
    print("o is found:- ",ind)
    break
  ind+=1

for i in str:
  if i=="o":
    continue
  print(i)

# for loop with maping type 
#for loop  print key
karan={"name":'pandey','address':'howrah','mobile':7388847685} 

for a in karan:
  print ("print key:-",a)


# for loop print value

for b in karan.values():
  print("print values:-",b)

# for loop print all data 
for a,b in karan.items():
  print(f"print all data:-{a}:{b}")


# for loop for table 
n=5
#n=int(input("Enter your number:-"))
for i in range(1,11):
  print (n*i)


# while loop 

a=1
while a<=5:
  print("print string :-","Welcome")
  a+=1

#print number 
a=1
while a<=100:
  print ("print number:-",a)
  a+=1

a=100
while a>=1:
  print("print number :-",a)
  a-=1

#while loop for table
n=23
a=1
while a<=10:
  print("print table :-",n*a)
  a+=1


# while loop in list

b=[1,2,3,4,5,6,7,8,9,10]

ind=0
while ind < len(b):
  print(ind)
  ind+=1

#print element using while loop 
ind=0
b=[1,2,3,4,5,6,7,8,9,10]
while ind<len(b):
  print(b[ind])
  ind+=1


# find element in list using while loop 
ind=0
while ind<len(b):
  if b[ind]==8:
    print(ind)
  ind+=1

#break statement in while loop
ind=0
while ind<len(b):
  if b[ind]==8:
    print("index number for break statement:-",ind)
    break
  else:
    print ("finding")
  ind+=1
  

# continue statement in while loop

i=0
while i<=10:
  if (i==6):
    i+=1
    continue
  print(i)
  i+=1
    

