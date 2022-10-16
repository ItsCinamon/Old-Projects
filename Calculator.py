from ast import operator
import imp
from random import choice
from time import sleep


#Start of the Calculator
print("This is a Test Calculator!")
print("Press a key to continue")
input()




#Input for the calculator
print("Please Input a number: ")
num1 = input()


print("Please Input a second number: ")
num2 = input()

print("Please Input a Operator: ")

operator = input()



#Calculate the numbers based on the operator

if operator == '+':
    print("This is your output: ", float(num1) + float(num2))

elif operator == '-':
    print("This is your output: ", float(num1) - float(num2))

elif operator == '/':
    print("This is your output: ", float(num1) / float(num2))

elif operator == '*':
    print("This is your output: ", float(num1) * float(num2))

else:
    print("You have not typed a valid operator, please run the program again.")


#To make the program not closed immediately
input()