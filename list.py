# Lists are Mutable
food = ["Chole Bhature", "Choco Waffle", "Samosa", "Pizza"]
print("Length of Food List :", len(food))
print("Food at index 0 :", food[0])
print("Food at index 1 :", food[1])
print("Food at index 2 :", food[2])
print("Food at index 3 :", food[3])

Student = ["Akarsh Singh", 20, "BCA", "Amity Noida"]
print(Student)

# Methods in List
marks = [98, 100, 95, 80, 75]
marks[2] = 85
print(marks)
print("Max value:", max(marks), "Min value:", min(marks))
marks[2:] #slicing
marks.append(88)
print(marks)
marks.insert(4, 99)
print(marks)
marks.remove(75)
print(marks)
marks.pop(4)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)