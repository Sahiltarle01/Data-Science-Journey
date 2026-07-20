# Dictionary

# Q.1 Create a dictionary with your Name, Age, College, and Branch. Print all key-value pairs.
dict = {
    "name":"Sahil",
    "age": 20,
    "college":"Sanjivani University",
    "branch":"AIDS"           
    }
print(type(dict))
print(dict)

# Q.2 Add a new key "City" with your city name and print the updated dictionary.
dict["city"]="Nashik"
print(dict)

# Q.3 Update your Age in the dictionary.
dict["age"]=19
print(dict["age"])

# Q.4 Delete the "City" key from the dictionary.
dict.pop("city")
try:
    print(dict["city"])
except KeyError:
    print("The item/key not present in dictonary")
    
# Q.5 Print all keys and all values separately.
print(dict.items())

# Q.6 Check whether a given key exists in the dictionary.
if "name" in dict:
    print("Value is found")
else:
    print("Value not found")
    
# Q.7  Create the dictionary of students and their marks. Find the student with the highest marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eva": 88
}
highest_scorer = max(student_marks, key=student_marks.get)
print(f"The highest scorer is {highest_scorer} with {student_marks[highest_scorer]} marks.")

# Q.8 Calculate the average marks of all students in the dictionary.
average_marks = sum(student_marks.values()) / len(student_marks)
print(f"The average mark of the class is {average_marks}.")

# Q.9 Count the frequency of each character in a string using a dictionary.
text = "hello world"
char_counts = {}
for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1
print(char_counts)

# Q.10 Count the frequency of each word in a sentence using a dictionary.
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.lower().split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)

