# 📘 Python Day 5 Notes

## Name: Sahil Shantaram Tarle
## Topic: Strings
## Day: 05

---

# 1. What is a String?

A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

Strings are used to store text data.

### Example

```python
name = "Sahil"
city = 'Nashik'

print(name)
print(city)
```

---

# 2. Why Do We Use Strings?

Strings are used to store text such as:

- Name
- Address
- Email
- Password
- Phone Number
- Messages

Almost every Python program uses strings.

---

# 3. Creating Strings

### Single Quotes

```python
language = 'Python'
```

### Double Quotes

```python
language = "Python"
```

### Triple Quotes

```python
text = """Python is
easy to learn."""
```

---

# 4. String Indexing

Each character in a string has an index.

Example

```
P  Y  T  H  O  N
0  1  2  3  4  5
```

Negative Index

```
P  Y  T  H  O  N
-6 -5 -4 -3 -2 -1
```

Example

```python
language = "Python"

print(language[0])
print(language[3])
print(language[-1])
```

Output

```
P
h
n
```

---

# 5. String Slicing

String slicing is used to extract a part of a string.

### Syntax

```python
string[start:stop]
```

Example

```python
language = "Python"

print(language[0:3])
print(language[2:6])
```

Output

```
Pyt
thon
```

---

# 6. String Length

The `len()` function returns the total number of characters.

Example

```python
name = "Sahil"

print(len(name))
```

Output

```
5
```

---

# 7. String Methods

## upper()

Converts all characters to uppercase.

```python
name = "sahil"

print(name.upper())
```

Output

```
SAHIL
```

---

## lower()

Converts all characters to lowercase.

```python
name = "SAHIL"

print(name.lower())
```

Output

```
sahil
```

---

## capitalize()

Capitalizes the first letter.

```python
name = "sahil"

print(name.capitalize())
```

Output

```
Sahil
```

---

## title()

Capitalizes the first letter of every word.

```python
text = "python programming"

print(text.title())
```

Output

```
Python Programming
```

---

## strip()

Removes extra spaces from the beginning and end.

```python
name = "   Sahil   "

print(name.strip())
```

Output

```
Sahil
```

---

## replace()

Replaces one word with another.

```python
text = "Hello Python"

print(text.replace("Python","World"))
```

Output

```
Hello World
```

---

## find()

Returns the index of the first occurrence.

```python
text = "Python"

print(text.find("t"))
```

Output

```
2
```

---

## count()

Counts how many times a character appears.

```python
text = "banana"

print(text.count("a"))
```

Output

```
3
```

---

## split()

Splits a string into a list.

```python
text = "Python SQL Pandas"

print(text.split())
```

Output

```
['Python', 'SQL', 'Pandas']
```

---

## join()

Joins list elements into a string.

```python
languages = ["Python","SQL","ML"]

print("-".join(languages))
```

Output

```
Python-SQL-ML
```

---

## startswith()

Checks whether a string starts with a specific character or word.

```python
text = "Python"

print(text.startswith("P"))
```

Output

```
True
```

---

## endswith()

Checks whether a string ends with a specific character.

```python
text = "Python"

print(text.endswith("n"))
```

Output

```
True
```

---

# 8. String Operators

## Concatenation

Used to join two strings.

```python
first = "Sahil"

last = "Tarle"

print(first + " " + last)
```

Output

```
Sahil Tarle
```

---

## Repetition

```python
print("Python "*3)
```

Output

```
Python Python Python
```

---

## Membership Operator

```python
text = "Python"

print("P" in text)
```

Output

```
True
```

---

# 9. Escape Characters

## New Line

```python
print("Hello\nWorld")
```

Output

```
Hello
World
```

---

## Tab Space

```python
print("Python\tSQL")
```

---

## Double Quotes

```python
print("He said \"Hello\"")
```

---

# 10. String Formatting

Using f-string

```python
name = "Sahil"

print(f"My name is {name}")
```

Output

```
My name is Sahil
```

---

# 11. Real-Life Applications

Strings are used in:

- Login Systems
- Chat Applications
- Email Validation
- Search Engines
- Data Analysis
- Machine Learning
- Password Checking
- Text Processing

---

# 12. Sample Programs

### Reverse String

```python
name = "Python"

print(name[::-1])
```

---

### Count Vowels

```python
name = input("Enter Name: ")

count = 0

for i in name:

    if i.lower() in "aeiou":

        count += 1

print(count)
```

---

### Palindrome Check

```python
word = input("Enter Word: ")

if word == word[::-1]:

    print("Palindrome")

else:

    print("Not Palindrome")
```

---

# 13. Keywords Learned Today

- String
- Indexing
- Slicing
- len()
- upper()
- lower()
- capitalize()
- title()
- strip()
- replace()
- find()
- count()
- split()
- join()
- startswith()
- endswith()

---

# 14. Interview Questions

### Q1. What is a string?

**Answer:**
A string is a sequence of characters enclosed in quotes.

---

### Q2. How do you create a string in Python?

**Answer:**
Using single quotes, double quotes, or triple quotes.

---

### Q3. What is indexing?

**Answer:**
Indexing is used to access individual characters of a string.

---

### Q4. What is slicing?

**Answer:**
Slicing is used to extract a portion of a string.

---

### Q5. What does len() do?

**Answer:**
It returns the total number of characters in a string.

---

### Q6. Difference between upper() and lower()?

**Answer:**

- upper() converts text to uppercase.
- lower() converts text to lowercase.

---

### Q7. What does replace() do?

**Answer:**
It replaces one word or character with another.

---

### Q8. What does split() do?

**Answer:**
It converts a string into a list.

---

### Q9. What is concatenation?

**Answer:**
Joining two or more strings together.

---

### Q10. What did you learn today?

**Answer:**
Today I learned about Python strings, indexing, slicing, string methods, string operators, escape characters, string formatting, and real-life applications of strings.

---

# 15. Summary

Today I learned how to work with strings in Python. I practiced indexing, slicing, string methods, string operators, and formatting. I also learned how to reverse strings, count vowels, check palindromes, and manipulate text using built-in functions.

---

# 🎯 Key Points to Remember

- Strings store text data.
- Indexing starts from 0.
- Negative indexing starts from -1.
- Slicing extracts part of a string.
- Strings are immutable.
- String methods return a new string.
- len() returns string length.
- split() converts a string into a list.
- join() combines list elements into a string.

---

# 📌 Common Mistakes

❌ Incorrect

```python
name = Python
```

✅ Correct

```python
name = "Python"
```

---

❌ Incorrect

```python
print(name[10])
```

(Produces IndexError)

---

✅ Correct

```python
print(name[0])
```

---

# 🚀 Revision Points

✅ What is a String?

✅ String Indexing

✅ Negative Indexing

✅ String Slicing

✅ String Methods

✅ String Operators

✅ Escape Characters

✅ String Formatting

✅ String Programs
