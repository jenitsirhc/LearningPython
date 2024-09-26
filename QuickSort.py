quick_list = [16, 20, 23, 15, 18, 13, 12, 21]


def quickSortHlp(quick_list, first, last):
    if first < last:
        splitpoint = partition(quick_list, first, last)

        quickSortHlp(quick_list, first, splitpoint-1)
        quickSortHlp(quick_list, splitpoint+1, last)


def quickSort(quick_list):
    quickSortHlp(quick_list, 0, len(quick_list)-1)


def partition(quick_list, first, last):
    pivotvalue = quick_list[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and quick_list[leftmark] <= pivotvalue:
            leftmark = leftmark - 1

        while quick_list[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True

        else:
            temp = quick_list[leftmark]
            quick_list[leftmark] = quick_list[rightmark]
            quick_list[rightmark] = temp

    temp = quick_list[first]
    quick_list[first] = quick_list[rightmark]
    quick_list[rightmark] = temp

    return rightmark


quickSort(quick_list)
print(quick_list)

