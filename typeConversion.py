# Implicit Conversion(Done Automatically by Python)
x = 5
y = 10.5
z = x+y
print(z, "Data Type :", type(z))

# Explicit Conversion
# Take num as input, convert it to float & print both original & converted value with their data types
num = input("Enter num : ")
convertedValue = float(num)
print(num, type(num))
print(convertedValue, type(convertedValue))