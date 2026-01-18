capitals={"India":"Delhi", "USA":"Washington DC", "France":"Paris", "Sri Lanka":"Colombo"}

#Printing the value of a key if present
print (capitals["Sri Lanka"])

#Printing the value of a key if it is present or not
print (capitals.get("UK","Unknown"))

#Adding new elements to a dictionary
capitals["Afghanistan"]="Kabul"
print (capitals["Afghanistan"])

capitals["Andorra"]="Andorra La Vella"
print (capitals["Andorra"])

#Printing all keys in the dictionary
print (capitals.keys())

#Printing all values in the dictionary
print (capitals.values())

#Finding the length of the dictionary
print (len(capitals))

#Finding if a key is in the dictionary
if 'USA' in capitals:
    print ("True")
else:
    print ("False")

#Deleting a key and it's value from the dictionary
del capitals['Afghanistan']

print (capitals)

#Changing the value of a key
capitals['USA']="Florida"

print (capitals)

countries=[]
for k in capitals:
    countries.append(k)

countries.sort()
print (countries)