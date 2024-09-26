#Create a single dimensional array
# for multiple age (in years) and
# then display each age in days.
# Assuming a year has 365 days.
# Name your program Mid_Activity2.py
import array as arr
years = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("(Age)Years to days: ")
for x in years:
    print(x, " year/s to", x * 365, " days")
