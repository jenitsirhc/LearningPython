sel_list = [36, 43, 39, 20, 45, 29, 52, 54, 18, 12]

print("Original order  : ", sel_list)

def selectionSort(sel_list):
    size = len(sel_list)

    for i in range(size):
        minimum = i

        for j in range(i+1, size):

            if (sel_list[j] < sel_list[minimum]):
                minimum = j

            temp = sel_list[i]
            sel_list[i] = sel_list[minimum]
            sel_list[minimum] = temp

    return sel_list


print("Ascending order : ", selectionSort(sel_list))


def selectionSort2(sel_list):
    size = len(sel_list)

    for i in range(size):
        maximum = i

        for j in range(i + 1, size):

            if (sel_list[j] > sel_list[maximum]):
                maximum = j

            temp = sel_list[i]
            sel_list[i] = sel_list[maximum]
            sel_list[maximum] = temp

    return sel_list


print("Descending order: ", selectionSort2(sel_list))
