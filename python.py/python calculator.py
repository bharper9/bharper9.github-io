import math
import os
import sys


def addition(x,y):
    print(x+y)
def subtraction(x,y):
    print(x-y)
def Multiply(x,y):
    print(x*y)
def Divison(x,y):
    print(x/y)
def restart_script():
        print("Restarting script...")
        os.execv(sys.executable, ['python'] + sys.argv)
        
        
print("Welcome to the Python Calculator \n")
number1 = input(f"Please type in the first number \n")
x = int(number1)
number2 = input(f"Please type in the second number \n")
y = int(number2)

z = input("What type of operation would you like to do Add,Subtract,Multiply or Division \n")
if z == "Add":
    addition(x,y)
elif z == "Subtract":
    subtraction(x, y)
elif z == "Multi":
    Multiply(x, y)
elif z == "Divide":
    Divison(x, y)
elif z == "/":
    restart_script()
    
    
    