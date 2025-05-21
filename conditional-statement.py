# if  statement
age=18
if age>=18:
    print("you are eligible for vote")





#if-else statement

age=17
if age >=18:
    print("you are eligible for vote")
else:
    print ("you cannot vote yet")





#if- elif-else satatement
marks=95
if marks >=90:
    print("Grade A++")
elif marks>=80:
    print("Grade A+")
elif marks>=60:
    print("Grade A")
elif marks>=50:
    print("Grade B")
elif marks>=33:
    print("Grade C")
else:
    print("Fail")







#neasted if statement

age =18
nationality="indian"
if age>=18:
    print("you are eligible for vote")
    if nationality=="indian":
        print("You can vote in Indian elections.")

    else:
        print("You must be an Indian citizen to vote.")
else:
    print("you are not eligible for vote")




#ternary operator (conditional statement)

age=16
a="Adult" if age>=18 else "minor"
print(a)