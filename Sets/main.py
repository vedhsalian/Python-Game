numbers={1,2,3,4}
print(numbers)

colors=set(['red','blue','green','yellow'])
print (colors)\

#Features of sets:

#1. Sets have no duplicates
n={1,1,2,3,3,4,5,5,5}
print(n)

#2. Elements in sets have no fixed position
#Indexing cannot be done - print(n[3])

#3. Mutable - Can add or remove elements
fruits={"mango","orange"}
print(fruits)

#Adding an element
fruits.add("banana")
print(fruits)

#Removing an element
fruits.remove("mango")
print(fruits)

A={1,2,3}
B={3,4,5}

#Union - all elements
print(A|B)
print(A.union(B))
#Intersection - only the common element
print(A&B)
print(A.intersection(B))
#Difference
print(A-B)
print(B.difference(A))