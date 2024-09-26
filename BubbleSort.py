bubblelist = [55, 12, 18, 25, 63, 42, 20, 6]


def bubbleSort(bubblelist):
    numloop=1

    for passnum in range(len(bubblelist)-1, 0, -1):
        print("Loop %d" % numloop)

        for i in range(passnum):
            if bubblelist[i] > bubblelist[i+1]:
                temp = bubblelist[i]
                bubblelist[i] = bubblelist[i+1]
                bubblelist[i+1] = temp

                print(bubblelist)

        print()
        numloop = numloop +1

bubbleSort(bubblelist)
