total = 0

count = 0

salary = 0

print('Enter a set of salary values and type negative to stop:\n')

try:

    while salary >= 0:

        salary = float(input(''))

        if salary >= 0:

            total += salary

            if salary > 0:
                count += 1

    if count > 0:

        average = total / count

        print('Average salary is: {:,.2f}'.format(average))

    else:

        print('No data was entered')



except ValueError:

    print('Please enter a valid set of values.')