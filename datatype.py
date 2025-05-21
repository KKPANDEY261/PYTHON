# Numeric Types 
                #Integer (int)
a=10
b=-5
print("Intteger:-",a,b)
print(type(a))
print(type(b))

# Float 
c=3.14
d=5e3
print("float:-",c,d)
print(type(c))
# Complex 
e=3+4j
f=2j
g=complex(1,-1)
print(e,f,g)
print(type(e))
print(type(f))
print(type(g))
# Sequence Types
     # String
h='hello'
i="hello"
j='''welcome to nsti howrah'''
k="""welcome to nsti howrah"""
print(h,i,j,k)
print(type(h))
print(type(i))
print(type(j))
print(type(k))
# LIst
x=[1,2,3,'hello']
print(x)
print(type(x))
x[0]=10
print(x)

#Tuple
l=(1,2,3,'hello')
#l[0]=10
print(l)
print(type(l))

#Range
m=range(10)
print(list(m))
n=range(10,1,-2)
print(list(n))
print(type(n))

#maping type
karan={"name":'pandey','address':'howrah','mobile':7388847685}
print(karan)
karan['name']='karan'
print(karan)
print(type(karan))

#Set
o={1,2,3,3,4,4,5,5,6}
print(o)
o.add(7)
print(o)
print(type(o))

#Frozen set 
p=frozenset([1,2,3,4,5,6,7])
print(p)
#p.add(8)
#print(p)
print(type(p))

#boolean type
q=True
print(q)
r=False
print(r)
print(type(r))

#Binary Types
#Bytes (bytes)
s=b'hello'
print(list(s))
print(s)
#s[0]=72
#print(s)
print(type(s))

t=bytearray(b'hello')
print(t)
t[0]=72
print(t)
print(type(t))

#None Type
u=None
print(u)
print(type(u))
