students={}

while True:
  name=input("Enter the name of the students and if you are done enter done:")
  if name=="Done":
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
        print(f"{name}={grade}")
        
else:
    print("No student's data is found")