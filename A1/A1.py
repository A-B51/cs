# Assignment 1

# A simple calculator
print('')
print('*************************************************************')
print('')
print('                  [ THE SIMPLE CALCULATOR ]                  ')
print('')
print('INSTRUCTIONS:')
print('Choose between [add/subtract/multiply/divide]')
print('If you want to exit the calculator, type "end"')
print('')
print('*************************************************************')
print('')

# create a list
l = []

# start counting
i = 0

while(i<1000):
    operator = input('Please enter operator [add/subtract/multiply/divide]: ')

    if (operator == 'add'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = int(num1) + int(num2)
        print(result)
        hist = f"({i}) {operator} / {num1} / {num2} -> {result}"
    elif (operator == 'subtract'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = int(num1) - int(num2)
        print(result)
        hist = f"({i}) {operator} / {num1} / {num2} -> {result}"
    elif (operator == 'multiply'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = int(num1) * int(num2)
        print(result)
        hist = f"({i}) {operator} / {num1} / {num2} -> {result}"
    elif (operator == 'divide'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = int(num1) / int(num2)
        print(result)
        hist = f"({i}) {operator} / {num1} / {num2} -> {result}"
    elif (operator == 'end'):
        break
    elif (operator == 'history'):
        print(*l, sep = '\n')
        hist = f"({i}) {operator}"
    else:
        print('Please enter a valid statement')
    i = i + 1
    l.append(hist)
