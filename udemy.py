#to get the LCM of two numbers
num=int(input('Enter first number: '))#first number
num2=int(input("enter second number: "))#second number

import math #SELECTING FROM THE MATH LIBRARY

gcd=math.gcd(num,num2)#FINDING THE GREATEST COMMON DIVISOR
print("The greatest common divisor=", gcd) 
lcm=(num*num2)/gcd  #formula for getting LCM
print("The lowest common multiple=", lcm)
