# Write a program that would ask the user to
# input 10 numbers and store them into a one-dimensional array.
# Compute each array element into its square and cube equivalent and
# display the result. Name your program Mid_Activity1.py
import array as arr

store = list()
for i in range(10):
    n = input("Input a number:")
    store.append(int(n))

print("Square of the numbers")
for x in store:
    print(x ^ 2)

print("")
print("Cube of the numbers: ")
for y in store:
    print(y ^ 3)
