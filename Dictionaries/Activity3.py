Fruits={}

for i in range(5):
    favorite=input("Enter your favorite fruit")
    if favorite in Fruits:
        Fruits[favorite]+=1
    else:
        Fruits[favorite]=1

for key,value in Fruits.items():
    print (key,": ",value)
    