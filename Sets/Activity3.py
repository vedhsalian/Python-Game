password=input("Enter your password: ")
characters=set(password)

if len(characters)>=8:
    print("You have created a strong password!")
else:
    print("You have created a weak password, try again!")