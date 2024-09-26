# Write a Python program to reverse the order of the items in the array.
import array as arr
b = arr.array('i',[3, 9, 1, 7, 3])

print("Original Array : ")
for i in b:
    print(i, end=" ")

print("")

b.reverse()
print("Reverse the order of the items: ")
for i in b:
    print(i, end=" ")
