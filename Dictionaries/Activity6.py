def add_element(n):
    d3={}
    for i in range(n):
        key=input("Enter the key: ")
        value=int(input("Enter the value: "))
        d3[key]=value
    return d3

length1=int(input("How many elements would you like to add for dictionary 1?"))
print ("Enter the elements of the first dictionary:")
d1=add_element(length1)

length2=int(input("How many elements would you like to add for dictionary 2?"))
print ("Enter the elements of the second dictiionary:")
d2=add_element(length2)

d3=d1.copy()

for key,value in d2.items():
    if key in d3:
        d3[key]+=value
    else:
        d3[key]=value

print ("Result= ")
print (d3)