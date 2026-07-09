# List
# Mutable(can be changed)
fruits = ["Apple", "Banana", "Mango"]
print(fruits)

# Create List
#1. Integer List
numbers = [10,20,30,40]

#2. String List
names = ["Sahil","Rahul","Amit"]

#3. Mixed List
data = [101,"Sahil",89.5,True]

#Acess element
names=["Sahil", "Mayank", "Piyush", "Sarthak"]
print(names[0])

#Slicing
names=["Sahil"]
print(names[-1])
print(names[0:4])

# Change List Items
names = ["Sahil","Rahul","Amit"]
names[1] = "Rohan"
print(names)

# Methods
#1. append()
#Adds an item to the end.
fruits = ["Apple","Banana"]
fruits.append("Mango")
print(fruits)

#2. insert()
#Adds an item at a specific position.
fruits.insert(1,"Orange")

#3. remove()
#Removes a specific item.
fruits.remove("Banana")

#4. pop()
#Removes an item by index.
fruits.pop(1)

#5. sort()
#Sorts the list.(Ascending Order 1,2,3)
numbers = [5,2,8,1]
numbers.sort()
print(numbers)

#6. reverse()
numbers.reverse()

#7. len()
numbers = [10,20,30]
print(len(numbers))

# Loop Through List
fruits = ["Apple","Banana","Mango"]
for fruit in fruits:
    print(fruit)
    
# Membership Operator
fruits = ["Apple","Banana","Mango"]
print("Apple" in fruits)

#Nested List
students = [["Sahil",90],["Rahul",85],["Amit",95]]
print(students[1][0]) # Rahul