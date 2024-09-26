class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"\nValues are {self.num1} and {self.num2}"

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


V1 = Calculator(23, 10)
V2 = Calculator(56, 2)

print(V1)
print(f"Sum is : ", V1.addition())
print(f"Quotient is : ", V1.subtraction())

print(V2)
print(f"Product is : ", V2.multiplication())
print(f"Difference is : ", V2.division())

