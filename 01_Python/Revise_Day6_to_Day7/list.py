# Revision


# Q1. Create a list of five integers and print it.
list = [10,20,30,40,50]
print(type(list))
print("List of five integer is",list)

# Q2. Print the first and last element of a list.
print(list[0])
print(list[-1])

# Q3. Find the length of a list.
print(len(list))

# Q4. Add an element using append().
list.append (60)
print(list)

# Q5. Insert an element at a specific index.
list.insert(2,70)
print(list)

# Q6. Remove an element using remove().
list.remove(70)
print(list)

#Q7. Remove the last element using pop().
list.pop()
print(list)

# Q8. Sort a list in ascending order.
list.sort()
print(list)

# Q9. Sort a list in descending order.
list.reverse()
print(list)

# Q10. Find the maximum and minimum value in a list.
max_value = max(list)
min_value = min(list)
print("Max valu is:",max_value)
print("Min valu is:",min_value)