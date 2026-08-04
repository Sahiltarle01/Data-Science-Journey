# Iterators & Generators

numbers=[10,20,30,40]
it=iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Using Iterator in a Loop
numbers=[1,2,3,4,5]
it=iter(numbers)
for i in it:
    print(i)
    
# Generator
# A Generator is a special function that returns values one at a time using the yield keyword.
def numbers():
    yield 1
    yield 2
    yield 3
g=numbers()
print(next(g))
print(next(g))
print(next(g))

# yield Keyword
def demo():
    yield "Python"
    yield "Data Science"
g=demo()
for i in g:
    print(i)
    
# Generator vs Return
# 1. Using return
def add():
    return 10
print(add())

# 2. Using yield
def add():
    yield 10
g=add()
print(next(g))

#Generator Expression
square=(x*x for x in range(1,6))
for i in square:
    print(i)
    
    