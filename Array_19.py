# Write a Python program to get the number of occurrences of a specified element in an array.

c = [10, 11, 15, 13, 17, 19, 13]
print("Original array :")
for i in c:
    print(i, end=" ")


print("\nNumber of occurrences of the number 13 : " + str(c.count(13)))
