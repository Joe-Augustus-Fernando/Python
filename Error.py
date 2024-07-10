# IndexError if the user enters an index that is out of range.
try:
    list=[1,2,3,4,5,6,7,8,9,0]
    index = int(input("Enter the Index of an element"))
    print(list[index])
except IndexError:
    print("Use of index out of Range")
except ValueError:
    print("Enter a valid index")
except Exception as e:
    print(f"Error:{e}")
    print(index,list)
    print("Code Compeleted Succesfully ")