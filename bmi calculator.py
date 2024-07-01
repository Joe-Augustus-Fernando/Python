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
