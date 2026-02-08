words=set()

while True:
    print("Choose an option:\n1. Add a word\n2. Stop\n")
    choice=int(input("What do you wish to do? "))
    if choice==1:
        word=input("Enter the word: ")
        words.add(word)
    elif choice==2:
        break
    else:
        print("Invalid input!")

for i in words:
    print("The words are:\n",i)