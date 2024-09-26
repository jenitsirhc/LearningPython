# function that adds two numbers
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

# calling function with two values
result = add_numbers(5, 4)
print('Sum: ', result)

# function that squares a number inside a list
def get_square(num):
    return num * num

for i in [1,2,3,4,5,6,7,8,9]:
    # function call
    result = get_square(i)
    print('Square of',i, '=',result)
