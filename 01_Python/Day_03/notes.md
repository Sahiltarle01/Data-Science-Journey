# 📘 Python Day 3 Notes

## Name: Sahil Shantaram Tarle
## Topic: Conditional Statements (if, elif, else)
## Day: 03

---

# 1. What are Conditional Statements?

Conditional statements allow a program to make decisions based on conditions.

If the condition is **True**, one block of code executes.
If the condition is **False**, another block may execute.

### Example

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

---

# 2. Why Do We Use Conditional Statements?

Conditional statements are used when we want a program to make decisions.

### Real-Life Examples

- If it is raining, carry an umbrella.
- If marks are greater than 35, the student passes.
- If age is 18 or above, the person can vote.

---

# 3. Types of Conditional Statements

1. if Statement
2. if-else Statement
3. if-elif-else Statement
4. Nested if Statement

---

# 4. if Statement

The `if` statement executes a block of code only when the condition is True.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

---

# 5. if-else Statement

The `if-else` statement executes one block if the condition is True and another block if the condition is False.

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Example

```python
marks = 30

if marks >= 35:
    print("Pass")
else:
    print("Fail")
```

---

# 6. if-elif-else Statement

Used when multiple conditions need to be checked.

### Syntax

```python
if condition:
    statement

elif condition:
    statement

else:
    statement
```

### Example

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")
```

---

# 7. Nested if Statement

A Nested if means writing one if statement inside another if statement.

### Example

```python
age = 20
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to Vote")

    else:
        print("Not a Citizen")

else:
    print("Not Eligible")
```

---

# 8. Comparison Operators Used in Conditions

| Operator | Meaning |
|----------|---------|
| == | Equal To |
| != | Not Equal To |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal To |
| <= | Less Than or Equal To |

---

# 9. Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning |
|----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses the condition |

### Example

```python
age = 20

print(age >= 18 and age <= 60)
```

---

# 10. Indentation in Python

Python uses indentation (spaces) to define blocks of code.

Incorrect indentation causes an error.

### Correct Example

```python
if True:
    print("Hello")
```

---

# 11. Difference Between '=' and '=='

| = | == |
|---|----|
| Assignment Operator | Comparison Operator |

### Example

```python
x = 10

print(x == 10)
```

---

# 12. Real-Life Applications

- ATM Machine
- Login System
- Voting Eligibility
- Student Result
- Online Shopping Discount
- Traffic Signal System

---

# 13. Sample Program

```python
age = int(input("Enter Your Age: "))

if age >= 18:
    print("Eligible to Vote")

else:
    print("Not Eligible")
```

---

# 14. Grade Calculator

```python
marks = int(input("Enter Marks: "))

if marks >= 75:
    print("Distinction")

elif marks >= 60:
    print("First Class")

elif marks >= 50:
    print("Second Class")

elif marks >= 35:
    print("Pass")

else:
    print("Fail")
```

---

# 15. Interview Questions

### Q1. What is a conditional statement?

**Answer:**
A conditional statement is used to make decisions in a program based on conditions.

---

### Q2. What are the types of conditional statements?

**Answer:**

- if
- if-else
- if-elif-else
- Nested if

---

### Q3. When do we use if?

**Answer:**
We use if when we want to execute code only if a condition is True.

---

### Q4. What is the difference between if and if-else?

**Answer:**

- if executes only when the condition is True.
- if-else executes one block for True and another block for False.

---

### Q5. What is elif?

**Answer:**
elif is used to check multiple conditions.

---

### Q6. What is a Nested if?

**Answer:**
A Nested if is an if statement inside another if statement.

---

### Q7. Why is indentation important?

**Answer:**
Indentation defines the block of code in Python.

---

### Q8. What is the difference between '=' and '=='?

**Answer:**

'=' assigns a value.

'==' compares two values.

---

### Q9. Name three real-life examples of conditional statements.

**Answer:**

- ATM Machine
- Login System
- Voting Eligibility

---

### Q10. What did you learn today?

**Answer:**
Today I learned conditional statements in Python. I learned if, if-else, if-elif-else, nested if, comparison operators, logical operators, indentation, and decision-making programs.

---

# 16. Summary

Today I learned how Python makes decisions using conditional statements. I practiced using if, if-else, elif, and nested if statements. I also learned about indentation, comparison operators, logical operators, and real-life decision-making programs like voting eligibility, student grading, and login systems.

---

# 🎯 Key Points to Remember

- Python uses indentation instead of curly braces.
- if checks one condition.
- else executes when the if condition is False.
- elif is used for multiple conditions.
- Nested if is an if inside another if.
- Comparison operators return True or False.
- Logical operators combine multiple conditions.

---
