# String
# A string is a sequence of characters enclosed in quotation marks.
name="Sahil"
city="Nashik"
print(name)
print(city)

# Types to store string 
# 1.Single Quotes
name='Piyush'

# 2. Double Quotes
name="Sarthak"

# 3. Triple Quotes
name='''Mayank'''

# String Indexing
language = "Python"
print(language[0])  #P
print(language[3])  #t
print(language[-1]) #n

# String Slicing
# eg: string[start:stop]
language = "Python"
print(language[0:3])    #Pyt
print(language[2:6])    #thon

# String Length
name = "Sahil"
print(len(name))

# String Methods
#1. upper()
name = "sahil"
print(name.upper())

#2. lower()
name = "SAHIL"
print(name.lower())

#3. capitalize()
name = "sahil"
print(name.capitalize())

#4. title()
text = "python programming"
print(text.title())

#5. strip()
# Removes spaces.
name = "   Sahil   "
print(name.strip())

#6. replace()
text = "Hello"
print(text.replace("Hello","Hi"))

#7. find()
text = "Python"
print(text.find("t"))

#8. count()
text = "banana"
print(text.count("a"))

#9. split()
text = "Python SQL ML"
print(text.split())

#10. join()
words = ["Python","SQL","ML"]
print("-".join(words))

#String operators
#1. Concatenation
first = "Sahil"
last = "Tarle"
print(first + " " + last)

#2. Repetition
print("Python "*3)

#3. Membership
text = "Python"
print("P" in text)

#Escape Characters
print("Hello\nWorld")       #print in next line
print("Hello\tWorld")       #is an escape character that represents a horizontal tab
print("He said \"Python\"") #Put a backslash (\) before the inner double quotes. This tells Python to treat them as text, not code.

# String Formatting
#1. f-string
# An f-string is a Python string prefixed with f that embeds variables or expressions directly inside curly braces {} for fast, readable formatting.
name = "Sahil"
print(f"My name is {name}")

