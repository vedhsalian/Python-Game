details=()
groups=[]
groupnumber=0

for i in range(2):
    groupnumber+=1
    groupname=input("Enter your group name: ")
    groupsize=int(input("Enter the size of you group: "))
    competitiondate=input("Enter the competition's date: ")
    venue=input("Enter the venue name: ")
    medal=input("Enter the type of medal: ")
    details=(groupnumber,groupname,groupsize,competitiondate,venue,medal)
    groups.append(details)

print("All group records are: ")
for i in groups:
    print(i)