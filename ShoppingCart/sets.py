#Sets

my_set = {1, 2, 3, 4, 5}
print(my_set)


my_set.add(6)  #Adding a vaule no Set
print(my_set)

my_set.add(3)  #Remove a vaule on Set
print(my_set)

#Operators for set
set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union
union_set = set1.union(set2)     
print(union_set)

#intersection
inter_set = set1.intersection(set2)

#Difference
diff_set =set1.difference(set2)
print(diff_set)   