# Prime number or not

num = int(input('Enter a number: '))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is a prime number")

"""
===============================================

def prime(a):
  if a > 1:
    for j in range(2,int(a/2)+1):
      if (a%j)==0:
        print(a, "is not a prime number")
  else:
    print(a, "is a prime number")
    
================================================

n = int(input())
for i in range(2, n):
    if n % i == 0:
        print('it is not prime number')
        break
else:
    print('it is prime number')
    
================================================
"""