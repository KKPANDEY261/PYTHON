#Arithmatic operator
#addition
a=5+5
print(a)
#Subtraction
b=10-3
print(b)
#Multiplication
c=5*5
print(c)
#Division
d=5/2
print(d)
#Floor Division
e=5//2
print(e)
#Modulus
f=5%2
print(f)
#Exponentiation
g=5**2
print(g)

#Comparision operator
#Equal to
a=5==5
print("equal to",a)
#Not equal to
b=5!=6
print(b)
b=5!=5
print(b)

#Greater than

print('Greater than',5>6)

print('Greater than',5>4)

#less than

print('less than',5<3)

print('less than',5<6)

#Greater Than or equal

print('Greater Than or equal',5>=5)
print('Greater Than or equal',5>=4)
print('Greater Than or equal',5>=3)


#Lessthan or equal

print('Lessthan or equal',5<=5)
print('Lessthan or equal',5<=3)
print('Lessthan or equal',5<=6)

#Assignment operator

#Assignment 

a=10
print('Assignment:-',a)
a+=10
print('Add and Assign:-',a)
a-=5
print('Subtract and assign:-',a)
a*=5
print('Multiply and assign:-',a)
a/=4
print('Divide and assign:-',a)
a//=2
print('Floor divide and assign:-',a)
a%=2
print('Modulus and assign:-',a)
a**=3
print('Exponent and assign:-',a)

(y:=len("welcome"))
print('Walrus operator:-',y)

#Logical operator
a=5>3
b=3<4
print('Logical and :-',a and b)
c=5>3
d=5<3
print('Logical or :-',c or d)

print('Logical not:-',not c)

#Identity Operator
#identity, is operator
e=[1,2,3,4,5,6,7,8,9]
b=e
print("identity, is  operator:- ",e is b)
f=[1,2,3,4,5,6,7,8,9]
print("identity, is operator:-",e is f)

#identity, is not operator

print ("identity, is not :-",e is not b)
print("identity, is not operator:-", e is not f)

#membership operator

#membership, in operator 

g={"apple","banana","mango"}
print("membership, in operator:-","apple" in g)
print ("membership , not in operator:-","apple" not in g)


#bitwise operator
#and
print("Bitwise and:-",5&6)
print("Bitwise or :-",5|6)
print ("Bitwise not :-",~5)
print("Bitwise xor:-", 5^6)
print ("Bitwise left shift :-",5<<2)
print("Bitwise left shift:-",-5<<2)
print ("Bitwise right shift:-",10>>2)
print("Bitwise right shift:-",-5>>2)

#Ternary operator
x=5
y='Even Number' if x%2 == 0 else 'Odd number'
print(y)


