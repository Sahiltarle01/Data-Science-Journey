# Python Day 5 Assignment

# Q1. Take a Name and Print It
print("Q1. Print Name")
name = input("Enter your name: ")
print("Your Name is:", name)

# Q2. Find Length of String
print("\nQ2. Length of String")
print("Length of Name:", len(name))

# Q3. Convert to Uppercase
print("\nQ3. Uppercase")
print("Uppercase:", name.upper())

# Q4. Convert to Lowercase
print("\nQ4. Lowercase")
print("Lowercase:", name.lower())

# Q5. Reverse the String
print("\nQ5. Reverse String")
reverse = name[::-1]
print("Reverse:", reverse)

# Q6. Count Vowels
print("\nQ6. Count Vowels")
vowels = "aeiouAEIOU"
count = 0
for ch in name:
    if ch in vowels:
        count += 1
print("Total Vowels:", count)

# Q7. Count Consonants
print("\nQ7. Count Consonants")
consonants = 0
for ch in name:
    if ch.isalpha() and ch not in vowels:
        consonants += 1
print("Total Consonants:", consonants)

# Q8. Palindrome Check

print("\nQ8. Palindrome Check")
word = input("Enter a Word: ")
if word.lower() == word[::-1].lower():
    print("Palindrome")
else:
    print("Not a Palindrome")

# Q9. Replace a Word

print("\nQ9. Replace Word")
sentence = input("Enter a Sentence: ")
old_word = input("Word to Replace: ")
new_word = input("New Word: ")
print("Updated Sentence:")
print(sentence.replace(old_word, new_word))

# Q10. Mini Project
# Student Information Formatter
print("\nQ10. Student Information Formatter")
student_name = input("Enter Student Name: ")
college = input("Enter College Name: ")
branch = input("Enter Branch: ")
print("\n==============================")
print("      STUDENT DETAILS")
print("==============================")
print("Name     :", student_name.title())
print("College  :", college.title())
print("Branch   :", branch.upper())
print("==============================")

# Bonus Program 1
# Count Spaces
print("\nBonus 1: Count Spaces")
text = input("Enter a Sentence: ")
print("Total Spaces:", text.count(" "))

# Bonus Program 2
# Check Starts With
print("\nBonus 2: Starts With")
text = input("Enter a Word: ")
print(text.startswith("P"))

# Bonus Program 3
# Check Ends With
print("\nBonus 3: Ends With")
text = input("Enter a Word: ")
print(text.endswith("n"))

# Bonus Program 4
# Split Sentence
print("\nBonus 4: Split Sentence")
sentence = input("Enter a Sentence: ")
words = sentence.split()
print(words)

# Bonus Program 5
# Join Words
print("\nBonus 5: Join Words")
languages = ["Python", "SQL", "Pandas", "NumPy"]
print("-".join(languages))