# Day 16 - Iterators & Generators

## What is an Iterator?

An Iterator is an object that allows us to access elements of a collection one by one.

Python provides two built-in functions for iterators:

- iter()
- next()

---

# iter() Function

The `iter()` function converts an iterable object into an iterator.

### Example

```python
numbers=[10,20,30,40]

it=iter(numbers)

print(next(it))
print(next(it))
```

---

# next() Function

The `next()` function returns the next element from an iterator.

### Example

```python
numbers=[1,2,3]

it=iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

---

# Iterator Using Loop

An iterator can also be used with a loop.

### Example

```python
numbers=[10,20,30,40]

it=iter(numbers)

for i in it:
    print(i)
```

---

# What is a Generator?

A Generator is a special function that returns values one at a time using the `yield` keyword.

Unlike `return`, a generator remembers its previous state.

---

# yield Keyword

The `yield` keyword is used to produce one value at a time.

### Example

```python
def numbers():
    yield 1
    yield 2
    yield 3

g=numbers()

print(next(g))
print(next(g))
print(next(g))
```

---

# Generator Using Loop

```python
def demo():
    yield "Python"
    yield "Data Science"
    yield "Machine Learning"

g=demo()

for i in g:
    print(i)
```

---

# Generator Expression

Generator expressions are similar to list comprehensions but use parentheses.

### Example

```python
square=(x*x for x in range(1,6))

for i in square:
    print(i)
```

---

# return vs yield

### return

- Returns only one value.
- Terminates the function.

### Example

```python
def add():
    return 10

print(add())
```

### yield

- Returns one value at a time.
- Pauses the function and resumes later.

### Example

```python
def add():
    yield 10

g=add()

print(next(g))
```

---

# Advantages of Iterators

- Easy Traversal
- Saves Memory
- Efficient for Large Data
- Simplifies Looping

---

# Advantages of Generators

- Memory Efficient
- Faster Execution
- Generates Data on Demand
- Useful for Large Datasets
- Improves Performance

---

# Real-Life Applications

- Reading Large Files
- Data Science
- Machine Learning
- Data Processing
- Web Scraping
- Streaming Data
- Log Processing

---

# Important Terms

| Term | Meaning |
| ------ | --------- |
| Iterator | Object used to traverse data |
| iter() | Creates an iterator |
| next() | Returns the next element |
| Generator | Function that uses yield |
| yield | Produces one value at a time |
| Generator Expression | Generator created using parentheses |

---

# Difference Between Iterator and Generator

| Iterator | Generator |
| ---------- | ----------- |
| Uses iter() and next() | Uses yield |
| More Code | Less Code |
| Manual Creation | Automatically Created |
| Used for Traversing | Used for Generating Data |

---

# Interview Questions

### 1. What is an Iterator?

An Iterator is an object that allows sequential access to elements of a collection.

### 2. What is iter()?

The `iter()` function converts an iterable object into an iterator.

### 3. What is next()?

The `next()` function returns the next element from an iterator.

### 4. What is a Generator?

A Generator is a function that produces values one at a time using the `yield` keyword.

### 5. What is yield?

`yield` pauses the function and returns one value at a time.

### 6. Difference between return and yield?

`return` ends the function after returning one value, whereas `yield` pauses the function and can return multiple values over time.

### 7. What are the advantages of Generators?

- Memory Efficient
- Faster
- Generates values on demand
- Suitable for large datasets

---

# Key Points

- Iterator accesses elements one by one.
- iter() creates an iterator.
- next() retrieves the next element.
- Generator uses the yield keyword.
- yield returns one value at a time.
- Generator expressions use parentheses.
- Generators are memory efficient.
- return ends the function.
- yield pauses the function and resumes later.

---

# Summary

Today you learned:

- Iterator
- iter()
- next()
- Generator
- yield
- Generator Expression
- Difference between return and yield
- Advantages of Iterators
- Advantages of Generators
- Real-Life Applications

---

# Next Topic

## Day 17 - Lambda Functions, map(), filter(), reduce() & Decorators

Topics:

- Lambda Functions
- map()
- filter()
- reduce()
- Decorators
- Practical Examples
- Interview Questions
