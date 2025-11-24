# set is a collection of unique & unordered items
# sets automatically remove duplicate elements

food = {"paneer", "chole bhature", "sandwich", "pizza"}
print(type(food))
print(food)
food.add("Chocolate")
print(food)
food.add("pizza")  # duplicate, will not be added
print(food)
food.remove("sandwich")
print(food)

# empty set creation
emptySet = set()
print(type(emptySet))
print(emptySet)