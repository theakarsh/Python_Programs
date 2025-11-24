# Dictionary is a built-in data type in Python that stores key-value pairs.
# Dictionaries are mutable, unordered & dont allow duplicate keys.
# If you create same key multiple times the last occurence of that key and its value will replace values of previous occurences.

student = {
    "name" : "Akarsh Singh",
    "age" : 20,
    "course" : "BCA",
    "city" : "Noida"
}
print(type(student))
print(student["name"])
print(student)
student["course"] = "B.Tech"
print(student)
student["favSubject"] = "Computer Science"
print(student)
student.pop("age")
print(student)
print(student.keys())
print(student.items())