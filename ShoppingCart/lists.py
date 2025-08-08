#Basic of lists
fruits = ["apple", "banana", "cherry"]

print(fruits[0])

fruits[1] = "blueberry"

print(fruits)


#Adding Items on lists
fruits =["apple", "banana", "cherry"]

fruits.append("kiwi")
print(fruits)

fruits.insert(1 , "organge") # Adding a vaule
print(fruits)


#Removing items on lists
fruits.remove("kiwi")
print(fruits)


#sort method to sort items in the list
fruits.sort()   #arranges the items in ascending order
print(fruits)

fruits.sort(reverse=True)   #arranges the items in descending order
print(fruits)


