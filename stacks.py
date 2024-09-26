stack = []

stack.append("Holy")
stack.append("Angel")
stack.append("Univ")

size = len(stack)

for x in range(size-1, -1, -1):
    print(stack[x])


print('=======================================')
stack2 = []
size = int(input("Input size of stacks: "))

for x in range(size):
    y = int(input("Push item in the stack[{0:d}]: ".format(x)))
    stack2.append(y)

for x in range(size-1, -1, -1):
    print(stack2[x])

print('=======================================')

stack3 =[]

stack3.append("Holy")
stack3.append("Angel")
stack3.append("Univ")
stack3.append("HAU")
stack3.append("City")

size2 = len(stack3)

for x in range(size2-1, -1, -1):
    print(stack3[x])
print(">>Item to remove<<")
print(stack3.pop())

print()
print(">>Items in stack<<")

size2 = len(stack3)

for x in range(size2-1, -1, -1):
    print(stack3[x])

