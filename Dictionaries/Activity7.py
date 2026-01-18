numbers=[]

length=int(input("How long do you want the list to be?"))

for i in range(length):
    number=int(input("Enter the number: "))
    numbers.append(number)

def top_n_frequent(lst,n):
    dict={}
    for n in lst:
        if n in dict:
            dict[n]+=1
        else:
            dict[n]=1
    return dict

dict=top_n_frequent(numbers,number)

print (dict)