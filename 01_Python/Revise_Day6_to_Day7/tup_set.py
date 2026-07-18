# Revision

# Q1. Create and print a tuple.
tuple =(10,20,30,40,50)
print(type(tuple))
print(tuple)

# Q2. Print the first and last element of a tuple.
print(tuple[0],)
print(tuple[-1])

# Q3. Find the length of a tuple.
print(len(tuple))

# Q4. Count the occurrence of an element using count().
print(tuple.count(20))

# Q5. Find the index of an element using index().
fruits = ['apple', 'banana', 'cherry', 'banana']
cherry_index = fruits.index('cherry')
print("Index of cherry:", cherry_index)
banana_index = fruits.index('banana')
print("Index of banana:", banana_index)

# Q6. Print all tuple elements using a loop.
for i in fruits:
    print(i, end=" , ")

# Q7. Create a set and print it.
set ={10,20,30,40,10,30,}
print(type(set))
print(set)

# Q8. Add an element to a set.
set.add(50)
print(set)

# Q9. Remove an element from a set.
set.remove(50)
print(set)

# Q10. Find the union of two sets.
set_1={1,2,3,4,5,}
set_2={7,8,9,6,5,}
union_method = set_1.union(set_2)
print("Union using method:", union_method)

# Q. Find the intersection of two sets.
intersect_method = set_1.intersection(set_2)
print("Intersection using method:", intersect_method)