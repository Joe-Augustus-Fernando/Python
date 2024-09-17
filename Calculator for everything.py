my_password="Joe"

password=""

while password!=my_password:
    password=input("Enter a Password:")
    if password==my_password:
        print("Entered password is correct")
    else:
        print("Incorrect password,Please try it again")
print("Access granted !")

calculator=input("Enter the type of calculator you need like-Math,Bmi,Perimeter,Area,Celsius to fahrenheit,Fahrenheit to celsius,Table,Mark,Highest and lowest(Please enter it as it is in this text.):")

if(calculator=='Math'):
    a = input("your 1st no is:")
    b = input("your 2nd no is:")
    operator = input("specific operators as +,-,*,/,//,%,**a,**b:")

    #prints the input

    print("1st no=",a)
    print("2nd no=",b)
    print("selected operator is:",operator)

    #prints the result

    if(operator=='+'):
     print(int(a)+int(b))
 
    elif(operator=='-'):
     print(int(a)-int(b))
 
    elif(operator=='*'):
     print(int(a)*int(b))
 
    elif(operator=='/'):
     print(int(a)/int(b))
 
    elif(operator=='//'):
     print(int(a)//int(b))
 
    elif(operator=='%'):
     print(int(a)%int(b))

    elif(operator=='**a'):
     print(int(a)*int(a))
 
    elif(operator=='**b'):
     print(int(b)*int(b))

    else:
     print("invalid")

elif(calculator=='Bmi'):

    height=float(input("Enter your height in m:",))
    weight=float(input("Enter your weight in kg:"))
    BMI=weight/height**2
    print("Your BMI is:",BMI)

    if(BMI<18.5):
     print("underweight")
    elif(BMI>=18.5 and BMI<25):
     print("normal")
    elif(BMI>=25 and BMI<30):
     print("overweight")
    else:
     print("obese")

elif(calculator=='Perimeter'):

    def calculate_perimeter(l,b):
        perimeter=l*b
        return perimeter

    l=int(input("Enter the length: "))
    b=int(input("Enter the breath: "))
    print ("The perimeter of the given land: ",calculate_perimeter(l,b),"Cm")

elif(calculator=='Area'):

    def calculate_area(l,b):
        area=l*b
        return area

    l=int(input("Enter the length: "))
    b=int(input("Enter the breath: "))
    print ("The area of the given land: ",calculate_area(l,b),"Cm^2")

elif(calculator=='Volume'):

    def calculate_volume(l,b,h):
        volume=l*b*h
        return volume

    l=int(input("Enter the length: "))
    b=int(input("Enter the breath: "))
    h=int(input("Enter the height: "))
    print ("The area of the given land: ",calculate_volume(l,b,h),"Cm^3")

elif(calculator=='Celsius to fahrenheit'):

    def celsius_to_fahrenheit(c):
        F=( 9/5 )*c +32
        return F

    c=int(input("Enter the temperature in Celsius"))
    print("Fahrenheit :",celsius_to_fahrenheit(c),"F")

elif(calculator=='Fahrenheit to celsius'):
    
    def fahrenheit_to_celsius(f):
        C=( f - 32 )* 5/9
        return C
    f=int(input("Enter temperature in Farenheit"))
    print("Celsius :",fahrenheit_to_celsius(f),"C")
    
elif(calculator=='Table'):
    n=int(input("Enter a no:"))
    for i in range(1,11):
        print(n,"x",i,"=",n*i)

elif(calculator=='Mark'):
    name= input("your name:")
    a= input("1st mark=")
    b= input("2nd mark=")
    c= input("3rd mark=")
    d= input("4th mark=")
    e= input("5th mark=")
    f= input("6th mark=")
    g= input("7th mark=")
    h= input("8th mark=")
    i= input("9th mark=")
    j= input("10th mark=")

    answer=int(a)+int(b)+int(c)+int(d)+int(e)+int(f)+int(g)+int(h)+int(i)+int(j)/10
    print(answer)

    if(answer>600):
     print("passed")

    else:
     print("failed")

elif(calculator=='Highest and lowest'):
       students={}

       while True:
        name=input("Enter the name of the students and if you are done enter done:")
        if name=="done":
          break
        grade=float(input("Enter the grade of the students:"))
        students[name]=grade
  
       if students:
        avg=sum(students.values())/len(students.values())
        highest=max(students.values())
        lowest=min(students.values())
  
        print(f"Average :{avg}")
        print(f"Highest grade :{highest}")
        print(f"Lowest grade :{lowest}")
  
        for name,grade in students.items():
            print("Enter student's name with marks:",f"{name}={grade}")
        
       else:
        print("No student's data is found")

else:
    print("Couldn't find what you entered! Please try again")

    permission=input("Enter if you want to play a game or not:")

    if permission=='yes':    
         import random as rd
         var=rd.randint(1,6)
         v=int(input("Enter a no from 1 to 6:"))

         if var==v:
             print("You\'ve guessed it correctly")
    
         else:
             print("Better luck next time")
    
         print(var)

    elif permission=='no':
         print("Goodbye!")

    else:
         print("invalid")
