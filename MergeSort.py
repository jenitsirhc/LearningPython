# Gatuz, Jna ; NW - 201

merge = [24, 56, 53, 37, 67, 51, 55, 31]


def mergeSort(merge):
    print("Splitting", merge)
    if len(merge) > 1:
        mid = len(merge)//2
        lefthalf = merge[:mid]
        righthalf = merge[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                merge[k] = lefthalf[i]
                i = i+1

            else:
                merge[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            merge[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            merge[k] = righthalf[j]
            j = j+1
            k = k+1

    print("Merging", merge)


mergeSort(merge)
print(merge)
