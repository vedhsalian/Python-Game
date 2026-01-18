report={}

for i in range(5):
    subject=input("What subject would like to add?")
    marks=int(input("How many marks did you get in "+str(subject)))

    report[subject]=marks

total=sum(report.values())

average=total/5

highest=max(report.values())

print (highest)
print (average)
print (total)
print (report)