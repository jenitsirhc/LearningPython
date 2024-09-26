# Gatuz, Jna ;NW - 201

insert_sort = [36,43,39,20,45,29,52,54,18,42]

def insertionSort(insert_sort):

    for i in range(1, len(insert_sort)):
        key = insert_sort[i]

        j = i-1
        while j >= 0 and key< insert_sort[j]:
            insert_sort[j+1]= insert_sort[j]
            j-=1
        insert_sort[j+1]= key

print("Original array:",insert_sort)
insertionSort(insert_sort)
print("Sorted array is: ")
for i in range(len(insert_sort)):
    print("%d" % insert_sort[i])

