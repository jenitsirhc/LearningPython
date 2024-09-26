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
