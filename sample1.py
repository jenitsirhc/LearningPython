
def printCategory(age):
    if age >= 18 and age <65:
        print('Adult')
    elif age >= 65:
        print('Senior Citizen')
    else:
        print('Child')

printCategory(70)
printCategory(10)

