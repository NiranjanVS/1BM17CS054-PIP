import string
import random

str1=string.printable;
n=int(input("n:"))
str2=""
for i in range(n):
    str2 = str2 + str1[random.randint(0,100)]
print(str2)
