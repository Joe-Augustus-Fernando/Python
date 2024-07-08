import random as rd

var=rd.randint(1,6)

v=int(input("Enter a no from 1 to 6:"))

if var==v:
    print("You\'ve guessed it correctly")
    
else:
    print("Better luck next time")
    
print(var)
