
"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the
number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
Need Funtion
Looping
Conditionals
math operators
"""
import math
import operator

def fizzbuzz(i):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz(100)