#Gatuz,Jna ; ICT - 101

#Write a program containing a list of 15 float values.
# The user will enter each value from the keyboard.
# Valid values are from 1.0 - 200,000.0 only.
# Include a method to sort and display the values.
# Prompt the user whether to view the list in ascending or descending order.
# Do not forget to validate the user input and ask the user whether to quit or
# enter another set of 15 values. Name your program FinalsLabActual2.py


def main():

    print("Please input 15 values ranging from [1 - 200,000] in value.")
    numbers = []

    for i in range(1,16):
        x = float(input("Enter : "))
        if 1 > x > 200000:
            break
        numbers.insert(i,x)
    sort(numbers)


def sort(numbers):
    print("Please choose")
    print("[1] - Ascending")
    print("[2] - Descending")
    choice = input("Enter your choice:")

    if choice == 1:
        print("Ascending Order: ", sorted(numbers))

    elif choice == 2:
        print("Descending Order: ", sorted(numbers, reverse=True))


main()
