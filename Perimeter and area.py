def calculate_area(l,b):
    area=l*b
    return area

l=int(input("Enter the length: "))
b=int(input("Enter the breath: "))
print ("The area of the given land: ",calculate_area(l,b),"Cm^2")

def calculate_perimeter(l,b):
    perimeter=l*b
    return perimeter

l=int(input("Enter the length: "))
b=int(input("Enter the breath: "))
print ("The perimeter of the given land: ",calculate_perimeter(l,b),"Cm")
