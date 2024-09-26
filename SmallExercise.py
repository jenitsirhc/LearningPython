# Write a python program that gets 10 numbers from the user and counts how many of those numbers are greater than 10

count = 0
for i in range(10):
    n = float(input(f"Enter number {i+1}: "))
    if n > 10:
        count = count+1


print(f"{count} numbers are greater than 10.")

# 10 numbers, average

val = 0
ctr = 0
num = 0
for i in range(10):
    num = int(input('Enter number: '))
    val += num
    ctr += 1
avg = val/num
print(avg)
