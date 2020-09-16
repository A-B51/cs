# Assignment 1

import time

# A simple calculator
print('')
print('*************************************************************')
print('')
print('                  [ THE SIMPLE CALCULATOR ]                  ')
print('')
print('INSTRUCTIONS:')
print('Choose between [add/subtract/multiply/divide]')
print('If you want to exit the calculator, type "end"')
print('To view previous calculations, type "history"')
print('')
print('*************************************************************')
print('')

# create a list
l = []

# start counting
i = 1

# calculations
while True:
    operator = input('Please enter operator [add/subtract/multiply/divide]: ')

    if (operator == 'add'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = f"{int(num1)} + {int(num2)} = {int(num1) + int(num2)}"
        print(result)
        res = int(num1) + int(num2)
        hist = f"[{i}] {result}"
    elif (operator == 'subtract'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = f"{int(num1)} - {int(num2)} = {int(num1) - int(num2)}"
        print(result)
        res = int(num1) - int(num2)
        hist = f"[{i}] {result}"
    elif (operator == 'multiply'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = f"{int(num1)} * {int(num2)} = {int(num1) * int(num2)}"
        print(result)
        res = int(num1) * int(num2)
        hist = f"[{i}] {result}"
    elif (operator == 'divide'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        if (int(num2) == 0):
            print('ERROR: Division by zero')
            continue
        result = f"{int(num1)} / {int(num2)} = {int(num1) / int(num2)}"
        print(result)
        res = int(num1) / int(num2)
        hist = f"[{i}] {result}"
    elif (operator == 'end'):
        print('*')
        time.sleep(0.5)
        print('*')
        time.sleep(0.5)
        print('*')
        time.sleep(0.5)
        print('Program has finished')
        print('')
        break
    elif (operator == 'history'):
        print(*l, sep = '\n')
        hist = f"[{i}] {operator}"
    elif (operator == 'M'):
        print(*m, sep = '\n')
    else:
        print('Please enter a valid statement')
        hist = f"[{i}] invalid"
    i = i + 1
    l.append(hist)
