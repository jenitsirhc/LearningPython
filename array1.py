import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])
print(a)


b = arr.array('i', [2, 5, 4, 6, 3, 7, 1, 9])
print('=======================================')
print("First Element : ", b[0])
print("? Element : ", b[3])
print("Last Element : ", b[-1])


arr_list = [5, 25, 10, 3, 14, 6, 20, 7, 15]
num_arr = arr.array('i', arr_list)
print('=======================================')
print(num_arr[1:6])
print(num_arr[:-5])
print(num_arr[3:])
print(num_arr[:-3])


num = arr.array('i', [2, 5, 3, 4, 1, 6])
num.append(8)
print('=======================================')
print("Appended: ", num)
num.extend([1, 2, 3])
print('=======================================')
print("Extended: ", num)

print('=======================================')
num_array = list()
print("Enter numbers in array: ")
num_elements = input("Enter the number of elements you want: ")

for i in range(int(num_elements)):
    n = input("number: ")
    num_array.append(int(n))
print("ARRAY: ", num_array)

print('=======================================')
print("Deleting an item in the array")
num_array2 = arr.array('i', [2, 4, 5, 7, 3, 6])
del num_array[2]
print(num_array2)

print('=======================================')
del num_array2
print(" Deleting the array and printing it out would cause an error")

print('=======================================')
num_array3 = arr.array('i', [2, 4, 5, 7, 3, 6])
num_array3.remove(7)
print(num_array3)

print('=======================================')
num_array4 = arr.array('i', [2, 4, 5, 7, 3, 6])
print(num_array4.pop(4))
print(num_array)

print('=======================================')
num_array5 = arr.array('i', [2, 4, 5, 7, 3, 6])
new_array = []

X = num_array5[0]+num_array5[1]
new_array.append(X)
print(new_array)

print('=======================================')
X2 = num_array5[3]-num_array5[5]
new_array.append(X2)
print(new_array)

print('=======================================')
X3 = num_array5[2]*num_array5[4]
new_array.append(X3)
print(new_array)

print('=======================================')
X4 = num_array5[2]/num_array5[4]
new_array.append(X4)
print(new_array)

print('=======================================')
X5 = num_array5[0]^num_array5[4]
new_array.append(X5)
print(new_array)

print('=======================================')
X6 = num_array5[1]%num_array5[3]
new_array.append(X6)
print(new_array)

print('=======================================')
num_arrayA = [2, 4, 5, 7, 3, 6]
new_arrayB = [1, 3, 5, 7, 1, 6]
num_arrayC = []
num_arrayD = []

num_elements =int(input("Enter size of array: "))

for x in range(num_elements):
    if num_arrayA[x] > new_arrayB[x]:
        num_arrayC.append(num_arrayA[x] + 5)

    else:
        num_arrayC.append(new_arrayB[x]*2)

print("num_arrayC: ")
print(num_arrayC)

print('=======================================')
for x in range(num_elements):
    if(num_arrayC[x] % 2 == 0):
        num_arrayD.append(num_arrayA[x])

    else:
        num_arrayD.append(new_arrayB[x])

print("num_arrayD: ")
print(num_arrayD)

TDim = [[3, 1, 5, 6], [2, 4, 9, 7], [3, 4, 6, 9], [5, 4, 6, 9]]

print(TDim[1])
print(TDim[2][1:3])
print(TDim[1][2])
print(TDim[3][0])
print(TDim[0][2])

print('=======================================')
for main in TDim:
    for inner in main:
        print(inner, end=" ")
    print()

print('=======================================')

TDim2 = [[3, 1, 5, 6], [2, 4, 9, 7], [3, 4, 6, 9], [5, 4, 6, 9]]

TDim2.insert(2, [2, 2, 2, 2])

for main in TDim2:
    for inner in main:
        print(inner, end=" ")
    print()

print('=======================================')
TDim3 = [[3, 1, 5, 6], [2, 4, 9, 7], [3, 4, 6, 9], [5, 4, 6, 9]]

del TDim[3]
print(TDim3)
del TDim3[0][0]

for main in TDim:
    for inner in main:
        print(inner, end=" ")
    print()

print('=======================================')
main = int(input("input"))

TDim = []
for row in range(main):
    TDim3.append([int(inner)for inner in input().split()])
print(TDim3)

print('=======================================')
TDim4 = [[3, 1, 5, 6], [2, 4, 9, 7], [3, 4, 6, 9], [5, 4, 6, 9]]

X = TDim4[0][0] + TDim[1][2]
print(X)

X = TDim4[2][1] + TDim[3][0]
print(X)

s = 0
for main in range(len(TDim4)):
    for inner in range(len(TDim[main])):
        s += TDim[main][inner]

    print(s)
    s = 0

# NODE

# Creating a Node
class Node:
    def __init__(self, item):
        self.item = item          # Assigning value to a node
        self.next = None          # Assigning the initial value of a linked list
# Creating a class for a linked list
class LinkedList:
    def __init__(self):
        self.head = None
# reference variable to linked list
linked_list = LinkedList()

# Instantiation
# Assigning the head of a linked list
linked_list.head = Node(1)

# Assign values to nodes
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

# Connect the Linked Lists Node
linked_list.head.next = second      # point the head node to the second node
second.next = third                 # point the second node to the third node
third.next = fourth
fourth.next = fifth

# Display the Connected Nodes of a Linked Lists
while linked_list.head is not None:
    print(linked_list.head.item, end=" ")
    linked_list.head = linked_list.head.next


# LINKED LIST!!!

class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, a):
        self.a = a
        return self.a + self.mileage

    def __str__(self):
        return f"The {self.color} car has {self.drive(100)} miles"


car1 = Car("blue", 0)
car2 = Car("red", 10)
car3 = Car("purple", 20)

print(car1)
print(car2)
print(car3)

print()

