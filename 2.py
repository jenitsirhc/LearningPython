from random import randint
from math import sin, pi

for i in range(10):
    print('hello')
print('The loop is done')

print('A')
print('B')
for i in range(5):
    print('C')
    print('D')
print('E')


x = randint(1, 10)
print('A random number between 1 and 10: ', x)


print('Pi is roughly', pi)
print('sin(0) =', sin(0))


num = randint(1, 10)
guess = eval(input('Enter your guess: '))
if guess == num:
    print('You got it!')
else:
    print('Sorry! The number is', num)

grade = eval(input('Enter your score: '))
if grade >= 90:
    print('A')
if grade >= 80 and grade < 90:
    print('B')
if grade >= 70 and grade < 80:
    print('C')
if grade >= 60 and grade < 70:
    print('D')
if grade < 60:
    print('F')

grade = eval(input('Enter your score: '))
if grade >= 90:
    print('A')
if grade >= 80:
    print('B')
if grade >= 70:
    print('C')
if grade >= 60:
    print('D')
else:
    print('F')
