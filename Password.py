my_password="joe18"

password=""

while password!=my_password:
    password=input("Enter a Password:")
    if password==my_password:
        print("Entered password is correct")
    else:
        print("Incorrect password,Please try it again")
print("Access granted !")
