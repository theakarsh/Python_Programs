# Delay in Execution

import time
count = int(input("Enter CountDown : "))
print("CountDown Begins ")
for i in range(count, 0, -1):
    print(i)
    time.sleep(1)
print("Hello, The Akarsh!")