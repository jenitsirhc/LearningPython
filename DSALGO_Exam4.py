# Write a Python class named Student with two attributes student_name, and student_grade.
# Create an init() method that will instantiate the attributes.
# Also, create an instance method that will identify whether the student grade is "passed" or "failed".
# The grade is passed if it is 70 to 100. Create two objects that will test the Student class.
# Upload a screenshot of your code and the output.


class Student:
    def __init__(self, student_name, student_grade):
        self.student_name = student_name
        self.student_grade = student_grade

    def __int__(self):

        if self.student_grade >= 70:
            return f"Passed"

        elif self.student_grade < 70:
            return f"Failed"

    def desc(self):
        return f"{self.student_name} has a grade of {self.student_grade} and has {self.__int__()}."


Anna = Student("Anna", 90)
Beth = Student("Beth", 60)
print(Anna.desc())
print(Beth.desc())
