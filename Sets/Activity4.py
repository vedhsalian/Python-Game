print("ONLINE GAME FRIENDS LIST MANAGER\n")
friends=set()

while True:
    print("\nChoose an option:\n1. Add a friend\n2. Remove a friend\n3. View friends list\n4. Exit\n")
    choice=input("Enter your choice: ")
    if choice=="1" or choice=="Add a friend":
        friend=input("Enter the persons username: ")
        friends.add(friend)
    elif choice=="2" or choice=="Remove a friend":
        unfriend=input("Enter the persons username: ")
        if unfriend in friends:
            friends.remove(unfriend)
    elif choice=="3" or choice=="View friends list":
        print("Friends List:")
        for i in friends:
            print(i)
    elif choice=="4" or choice=="Exit":
        print("Thank you for using the friends list manager!")
        break
    else:
        print("Invalid Input!")