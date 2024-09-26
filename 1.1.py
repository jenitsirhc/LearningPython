#1======================================

print("Given #1")
print("")

int1 = [2,5,7,9,10,11,12,14,15]

print("List of integers:")
print(int1)

print("Square of every number in the list:")
square = list(map(lambda x: x ** 2, int1))
print(square)

print("Cube of every number in the list:")
cube = list(map(lambda x: x ** 3, int1))
print(cube)

print("")
print("")
#2======================================

intA =[1,2,3,4,5]
intB =[6,7,8,9,10]

print("Given #2")
print("")

print("1st list of integers:")
print(intA)
print("2nd list of integers:")
print(intB)

sum = map(lambda x, y: x + y, intA, intB)
print("\nResult: after adding two lists")

print(list(sum))

print("")

#3======================================

listOfWords = ["I", "think", "therefore","I", "am"]

print("Original words: ", listOfWords)
print("")

reversed = list(map(lambda x : x[::-1], listOfWords))
print("Reverse words: ", reversed)
print("")

counter = list(map(lambda a : len(a),listOfWords))
print("Count per word: ", counter)
