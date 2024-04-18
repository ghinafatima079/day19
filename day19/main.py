"""Then, write a Python script named main.py that imports the math_operations module and demonstrates the usage of each function and the PI constant."""
import math_operations as mo
a=float(input("Enter a number:"))
b=float(input("Enter a number:"))
print("You can perform the following operations- \n 1.add \n 2.subtract \n 3.multiply \n 4.divide")
choice=input("Enter your choice:")
if choice.isalpha():
    choice=choice.lower()
match(choice):
    case '1'|'add':
        print(f"{a}+{b}={mo.add(a,b)}")
    case '2'|'subtract':
        print(f"{a}-{b}={mo.subtract(a,b)}")
    case '3'|'multiply':
        print(f"{a}*{b}={mo.multiply(a,b)}")
    case '4'|'divide':
        print(f"{a}/{b}={mo.divide(a,b)}")
    case _:
        print("invalid input")
print(f"The value of pi is {mo.PI}")