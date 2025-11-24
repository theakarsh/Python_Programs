# Print sum of first n natural numbers

n = int(input("Enter num : "))
no = n
sum = 0
while n >= 1:
    sum += n
    n -= 1 # last value of n will be zero
print(f"Sum of first {no} natural numbers is {sum}")