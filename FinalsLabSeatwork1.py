#===SEATWORK 1

def main():  #main method
    result = calculate(15, 5)
    print("Sum = ", result[0],"Product = ", result[1])  #displays the result


def calculate(x, y):  #calculates the result
    return x + y, x * y
    #returns the x and y values after being calculated


main()


#===SEATWORK 2

values = list(range(2, 20, 2))  #list ranging from the nos. 2-20, skipping by 2
print(values) #prints the list


#===SEATWORK 3

numbers = [] #empty list
odd = 0
even = 0

#asking for input from the user
n = int(input("Enter number of elements: "))
print()

#for loop
for x in range(1, n):
    elements = int(input("Enter a number:  "))
    numbers.append(elements)
    #Odd and even checker
    if (x % 2) == 0:
        even += 1  #even counter
    else:
        odd += 1  #odd counter
print()
#printing the results and list
print(numbers)
print("Even : ", even)
print("Odd  : ", odd)


#===SEATWORK 4
numbers = []
totalInt = 0

for x in range(1, 6):
    num = input('Enter a number: ')
    numbers.append(num)

    if type(x) == int :
        totalInt += 1
    else :
        print("Enter a valid input")

print("Number of integers : ", totalInt)
