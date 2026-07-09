# 📘 Python Day 6 Notes

## Name: Sahil Shantaram Tarle
## Topic: Lists
## Day: 06

---

# 1. What is a List?

A list is a collection of multiple items stored in a single variable.

Lists are one of the most commonly used data structures in Python.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

Output

```
['Apple', 'Banana', 'Mango']
```

---

# 2. Why Do We Use Lists?

Lists help us store multiple values in one variable.

Without List

```python
student1 = "Sahil"
student2 = "Rahul"
student3 = "Amit"
```

With List

```python
students = ["Sahil", "Rahul", "Amit"]
```

Lists make the code shorter, cleaner, and easier to manage.

---

# 3. Characteristics of Lists

- Ordered
- Mutable (Can be Modified)
- Allows Duplicate Values
- Can Store Different Data Types

Example

```python
data = [101, "Sahil", 89.5, True]
```

---

# 4. Creating Lists

### Integer List

```python
numbers = [10, 20, 30, 40]
```

### String List

```python
names = ["Sahil", "Rahul", "Amit"]
```

### Mixed List

```python
data = [100, "Python", 99.5, False]
```

---

# 5. List Indexing

Each element has an index.

Example

```
Apple   Banana   Mango
  0        1       2
```

Example

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[2])
```

Output

```
Apple
Mango
```

---

# 6. Negative Indexing

Negative indexing starts from the end.

```
Apple   Banana   Mango
 -3       -2      -1
```

Example

```python
print(fruits[-1])
```

Output

```
Mango
```

---

# 7. List Slicing

List slicing extracts a portion of the list.

### Syntax

```python
list[start:stop]
```

Example

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])
```

Output

```
[20, 30, 40]
```

---

# 8. Changing List Elements

Lists are mutable, so we can change their values.

Example

```python
names = ["Sahil", "Rahul", "Amit"]

names[1] = "Rohan"

print(names)
```

Output

```
['Sahil', 'Rohan', 'Amit']
```

---

# 9. List Methods

## append()

Adds an item at the end.

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

Output

```
['Apple', 'Banana', 'Mango']
```

---

## insert()

Adds an item at a specific index.

```python
fruits.insert(1, "Orange")
```

Output

```
['Apple', 'Orange', 'Banana']
```

---

## remove()

Removes a specific value.

```python
fruits.remove("Banana")
```

---

## pop()

Removes an element using its index.

```python
fruits.pop(1)
```

---

## sort()

Sorts the list in ascending order.

```python
numbers = [4,2,8,1]

numbers.sort()

print(numbers)
```

Output

```
[1,2,4,8]
```

---

## reverse()

Reverses the list.

```python
numbers.reverse()
```

---

## clear()

Removes all elements.

```python
numbers.clear()
```

---

# 10. Useful List Functions

## len()

Returns total number of elements.

```python
numbers = [10,20,30]

print(len(numbers))
```

Output

```
3
```

---

## max()

Returns largest element.

```python
marks = [75,90,80]

print(max(marks))
```

Output

```
90
```

---

## min()

Returns smallest element.

```python
marks = [75,90,80]

print(min(marks))
```

Output

```
75
```

---

## sum()

Returns total.

```python
marks = [75,90,80]

print(sum(marks))
```

Output

```
245
```

---

# 11. Loop Through List

```python
fruits = ["Apple","Banana","Mango"]

for fruit in fruits:

    print(fruit)
```

Output

```
Apple
Banana
Mango
```

---

# 12. Membership Operator

Checks whether an element exists.

```python
fruits = ["Apple","Banana","Mango"]

print("Apple" in fruits)
```

Output

```
True
```

---

# 13. Nested List

A list inside another list.

Example

```python
students = [

    ["Sahil",90],

    ["Rahul",85],

    ["Amit",95]

]

print(students[0][0])

print(students[0][1])
```

Output

```
Sahil
90
```

---

# 14. Real-Life Applications

Lists are used in:

- Student Management System
- Shopping Cart
- Banking Software
- Employee Records
- Data Science
- Machine Learning
- Music Playlist
- Contact List
- To-Do Applications

---

# 15. Sample Programs

## Print All Elements

```python
numbers = [10,20,30]

for i in numbers:

    print(i)
```

---

## Find Maximum

```python
numbers = [10,25,5,90]

print(max(numbers))
```

---

## Find Average

```python
marks = [80,90,70]

average = sum(marks)/len(marks)

print(average)
```

---

# 16. Difference Between List and Tuple

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses [] | Uses () |
| Can Modify | Cannot Modify |

---

# 17. Keywords Learned Today

- List
- append()
- insert()
- remove()
- pop()
- sort()
- reverse()
- clear()
- len()
- max()
- min()
- sum()

---

# 18. Interview Questions

### Q1. What is a List?

**Answer:**
A list is an ordered collection of items stored in a single variable.

---

### Q2. Are Lists Mutable?

**Answer:**
Yes. Lists are mutable, meaning they can be modified.

---

### Q3. What is Indexing?

**Answer:**
Indexing is used to access elements using their position.

---

### Q4. What is Negative Indexing?

**Answer:**
Negative indexing accesses elements from the end of the list.

---

### Q5. Difference between append() and insert()?

**Answer:**

append() adds an item at the end.

insert() adds an item at a specific index.

---

### Q6. Difference between remove() and pop()?

**Answer:**

remove() removes a value.

pop() removes an element using its index.

---

### Q7. What does sort() do?

**Answer:**
It sorts the list in ascending order.

---

### Q8. What is List Slicing?

**Answer:**
List slicing extracts a portion of a list.

---

### Q9. Which function returns the total number of elements?

**Answer:**
len()

---

### Q10. What did you learn today?

**Answer:**
Today I learned about Python Lists, indexing, slicing, list methods, looping through lists, nested lists, and their real-life applications.

---

# 19. Summary

Today I learned one of the most important data structures in Python called Lists. I learned how to create, access, modify, and traverse lists. I also practiced list methods such as append(), insert(), remove(), pop(), sort(), and reverse(). Lists are widely used in Data Science, Machine Learning, and many real-world applications.

---

# 🎯 Key Points to Remember

- Lists store multiple values.
- Lists are mutable.
- Lists use square brackets [].
- Indexing starts from 0.
- Negative indexing starts from -1.
- append() adds at the end.
- insert() adds at a specific position.
- remove() removes a value.
- pop() removes by index.
- sort() sorts the list.
- reverse() reverses the list.

---

# 📌 Common Mistakes

❌ Incorrect

```python
numbers = (10,20,30)
numbers.append(40)
```

(Tuples do not support append())

---

✅ Correct

```python
numbers = [10,20,30]
numbers.append(40)
```

---

❌ Incorrect

```python
print(numbers[10])
```

(IndexError if index doesn't exist.)

---

# 🚀 Revision Points

✅ What is a List?

✅ Creating Lists

✅ Indexing

✅ Negative Indexing

✅ List Slicing

✅ append()

✅ insert()

✅ remove()

✅ pop()

✅ sort()

✅ reverse()

✅ len()

✅ max()

✅ min()

✅ sum()

✅ Loop Through List
