# Indexing in Strings
str1 = "Akarsh"
print("Length of", str1, "is", len(str1))
print(str1[0] + str1[5])

# slicing
str = "Akarsh Singh"
print(str[0:6])
print(str[:5])
print(str[7:])
str = input("Enter your favourite food :")
mid = len(str)//2  # '//' is used when we dont want decimal part after dividing
print(str[mid-1 : mid+2])
print(str[-2])