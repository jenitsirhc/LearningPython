def shell_sort(list):

    gap = len(list) // 2

    while gap > 0:

        for i in  range(gap,len(list)):

            temp = list[i]

            j = i



            while j >= gap and list[j - gap] > temp:

                list[j] = list[j - gap]

                j = j-gap

            list[j] = temp

  

  

        gap = gap // 2



list = [20,56,1,98,100,165,3,50,4,90]

list2 = [2,3,7,8,5,11,20,24,26,31]



shell_sort(list)

shell_sort(list2)

print(list)

print(list2)