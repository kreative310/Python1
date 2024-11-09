#create a set using curly braskets

#my set = {1,2,3}

#print (my_set)

#create a set from the list using the set() function

#my_set = ([4,5,6])
#print(my_set)

#Create an empty set using the set() function
#my_set = set()
#print(my_set)

my_set = {1,1,1,2,3,3,4,5,3,2,2}
print(my_set) #set will automatically remove duplicates


######

set1 = {1,2,3}
set2 = {3,4,5}

#union between set1 and set2 using the union() method

union_method = set1.union(set2)

#compute an union between set1 and set2 using the | operator

union_operator = set1 | set2

print("Union of set1 and set2 using method: ", union_method)
print("Union of set1 and set2 using operator: ", union_method)

#compute intersection between set1and set2 using the intersection() method

intersection_method = set1.intersection(set2)

#computing intersection between set1 and set2 using & operator

intersection_operator= set1 & set2

print("intersection of set1 and set2 using intersection method", intersection_method)
print("intersection of set1 and set2 using intersection operator", intersection_operator)

#computing the elements that are unique to set1 using the diference method
difference_method = set1.difference(set2)

#computing elements that are unique to set1 using the - operator
difference_operator = set1 - set2

print("Difference of set 1 and set2 using the difference method", difference_method)
print("Difference of set 1 and set2 using the - operator", difference_operator)

#computing the elements that are in set1 and inset2 but not in their iintersection
symmetric_difference_method = set1.symmetric_difference(set2)

#computing the elements that are in set1 and in set2 but not in the intersection using the^ operator
symmetric_difference_operator = set1 ^ set2

print("Symetric difference methord of set1 and set2 using the symetric difference method", symmetric_difference_method)
print("Symetric difference methord of set1 and set2 using the symetric difference operator", symmetric_difference_operator)


#set methods

#create a set

my_set = {1,2,3}

#add number 7 at the end of the set

my_set.add(7) #add method

#remove number 3 from my set

my_set.remove(3) #remove method

#removing 8 from a set withot throwing an error if 8 is not on the set

my_set.discard(8)
print(my_set)

#removing all numbers from set
my_set.clear()

print(my_set)

#remove duplications from that list

#create a list that contains duplications

my_list = [1,2,2,2,3,4,4,4,5,6]

#convert this list to a set to remove duplications
unique_set = set(my_list)

print(unique_set)

#convert this set to a list
unique_list = list(unique_set)
print(unique_list)

#checking for common elements

blertas_interest = {"music", "movies", "travel"}
drilonis_interests = {"movies","games", "skiing"}

common_interests = blertas_interests.intersection(driloni_interests)
print(common_interests)

#in operator

colors = {"red", "green", "purple", "yellow", "black", "blue"}
color = "blue"
print(color in colors)
