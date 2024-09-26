# Create two-dimensional list for 5 students and their
# grades (double) for five subjects.
# Find the lowest and highest grades per student.


students = [[70, 80, 90, 76, 60], [100, 85, 91, 78, 65], [79, 82, 97, 76, 74],
            [85, 80, 90, 88, 99], [80, 95, 87, 85, 87]]

for a, i in enumerate(students):
    print("Student", (a+1), ":")
    for inner in i:
        print(inner, end=" ")
    print()

print("Student1 highest and lowest grade: ", max(students[0]), " ", min(students[0]))
print("Student2 highest and lowest grade: ", max(students[1]), "", min(students[1]))
print("Student3 highest and lowest grade: ", max(students[2]), " ", min(students[2]))
print("Student4 highest and lowest grade: ", max(students[3]), " ", min(students[3]))
print("Student5 highest and lowest grade: ", max(students[4]), " ", min(students[4]))
