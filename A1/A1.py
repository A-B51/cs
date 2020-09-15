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

i=0

while True:
    operator = input('Please enter operator [add/subtract/multiply/divide]: ')

    if (operator == 'add'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = int(num1) + int(num2)
        print(result)
    elif (operator == 'subtract'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = int(num1) - int(num2)
        print(result)
    elif (operator == 'multiply'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = int(num1) * int(num2)
        print(result)
    elif (operator == 'divide'):
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        result = int(num1) / int(num2)
        print(result)
    elif (operator == 'end'):
        break
    else:
        print('Please enter a valid statement')  
