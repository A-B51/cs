# Assignment 1

# A simple calculator
print('INSTRUCTIONS:')
print('This is a simple calculator')
print('Choose between add/subtract/multiply/divide')
print('If you want to exit the calculator, type "end"')

while True:
    operator = input('Please enter the operation to be executed [add/subtract/multiply/divide]: ')

    if (operator == 'add'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        print(int(num1) + int(num2))
    elif (operator == 'subtract'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        print(int(num1) - int(num2))
    elif (operator == 'multiply'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        print(int(num1) * int(num2))
    elif (operator == 'divide'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        print(int(num1) / int(num2))
    elif (operator == 'end'):
        break
    else:
        print('Please enter a valid statement')

