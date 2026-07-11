# Sets
#A Set is an unordered collection of unique elements.
numbers = {10,20,30,40}
print(numbers)

#Why Use Sets?
#Sets automatically remove duplicate values.
numbers = {10,20,20,30,30,40}
print(numbers)

#Add Elements
fruits = {"Apple","Banana"}
fruits.add("Mango")
print(fruits)

#Remove Elements
fruits.remove("Banana")

#discard() does not give an error if the element is missing.
fruits.discard("Orange")

#pop()
fruits.pop()

#clear()
fruits.clear()
#Set Operations
#1. Union
A = {1,2,3}
B = {3,4,5}
print(A | B)

#Intersection
print(A & B)

#Difference
print(A - B)

#Symmetric Difference
print(A ^ B)