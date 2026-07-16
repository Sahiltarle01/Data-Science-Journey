# Day 5 Strings

# Q21. Check whether a string is a palindrome
text = input("Enter a string: ")
rev = ""
for ch in text:
    rev = ch + rev
if text == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Q22. Count vowels and consonants in a string
text = input("Enter a string: ")
vowels = 0
consonants = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)

# Q23. Reverse a string without using slicing
text = input("Enter a string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed String =", reverse)

# Q24. Count the occurrence of each character in a string
text = input("Enter a string: ")
count = {}

for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

for key in count:
    print(key, "=", count[key])

# Q25. Check whether two strings are anagrams
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagram")
else:
    print("Not an Anagram")