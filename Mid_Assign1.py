# Create a two-dimensional array for multiplication table.

rows, cols = (10, 11)

arr = [[i*j for i in range(1, rows+1)] for j in range(1, cols)]

for row in arr:
    for inner in row:
        print("%6d" % inner, end=" ")
    print()