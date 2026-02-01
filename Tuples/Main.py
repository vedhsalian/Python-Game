#packing
address=('225','Seagull Apartment','Mankhool','Umm Al Quwain','817928')
for i in address:
    print(i,end=" ")

house_no, apart_name, community, emirate, pincode=address

print("\nHouse Number is",house_no)
print("Apartment is",apart_name)
print("Community is",community)
print("Emirate is",emirate)
print("Pincode is",pincode)

nested_tuple=("healthy",["Apple","Mango","Orange"],"unhealthy",["Chips","Softdrinks","Noodles"])
print(nested_tuple[3][1])
print(nested_tuple[2])

t=(0,10,20,30,40,50,60,70,80,90,100)

print(t[-3])
print(t[4])
print(t[1:4])
print(len(t))

for i in t:
    print(i)

print(120 in t)
print(50 in t)

t2=(1,2,3)
t3=(4,5,6)

t4=t2+t3

print(t4*3)

t5=t4*2

print(t5.count(2))

print(t5.index(6))