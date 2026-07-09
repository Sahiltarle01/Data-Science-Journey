
# Python Day 6 Assignment

# Q1. Create and Print a List
print("Q1. Create and Print a List")
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Fruits:", fruits)

# Q2. Print First Element
print("\nQ2. First Element")
print("First Fruit:", fruits[0])

# Q3. Print Last Element
print("\nQ3. Last Element")
print("Last Fruit:", fruits[-1])

# Q4. Find Length of List
print("\nQ4. Length of List")
print("Length:", len(fruits))

# Q5. Add an Item (append)
print("\nQ5. Append Item")
fruits.append("Grapes")
print(fruits)

# Q6. Insert an Item
print("\nQ6. Insert Item")
fruits.insert(2, "Pineapple")
print(fruits)

# Q7. Remove an Item
print("\nQ7. Remove Item")
fruits.remove("Banana")
print(fruits)

# Q8. Pop an Item
print("\nQ8. Pop Item")
removed = fruits.pop()
print("Removed:", removed)
print("Updated List:", fruits)

# Q9. Sort List
print("\nQ9. Sort List")
numbers = [45, 12, 67, 8, 90, 23]
numbers.sort()
print(numbers)

# Q10. Reverse List
print("\nQ10. Reverse List")
numbers.reverse()
print(numbers)

# Q11. Maximum, Minimum and Sum
print("\nQ11. Max, Min and Sum")
marks = [80, 75, 92, 65, 88]
print("Maximum:", max(marks))
print("Minimum:", min(marks))
print("Total:", sum(marks))

# Q12. Average of Marks
print("\nQ12. Average")
average = sum(marks) / len(marks)
print("Average:", average)

# Q13. Membership Operator
print("\nQ13. Membership")
if "Apple" in fruits:
    print("Apple Found")
else:
    print("Apple Not Found")

# Q14. Print List using Loop
print("\nQ14. Loop Through List")
for item in fruits:
    print(item)

# Q15. Count Even and Odd Numbers
print("\nQ15. Even and Odd Count")
numbers = [10, 15, 20, 25, 30, 35, 40]
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Numbers:", even)
print("Odd Numbers:", odd)

# Bonus Project
# Student Marks Manager
print("\n========== Student Marks Manager ==========")
marks = []
for i in range(5):
    mark = float(input(f"Enter Marks of Student {i+1}: "))
    marks.append(mark)
print("\nMarks:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Total Marks:", sum(marks))
print("Average Marks:", sum(marks) / len(marks))