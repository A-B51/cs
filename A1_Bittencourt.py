# Interactive Calculator

# index
i = 1

# empty list for history
lists = []

# empty list for result in M
listM = []

while True:
    operator = input('Please enter operator [add/subtract/multiply/divide/end/history]: ')

    # function to select result from history
    def M(index):
    # correct the function with the minus 1 cuz THE FIRST NUMBER OF THE LIST IS 0
        return(listM[index - 1])

    if (operator == 'add'):
        num1 = input('Enter the first number (Mi for result from i-th position in history): ')
        num2 = input('Enter the second number (Mi for result from i-th position in history): ')
        # f syntax: if we dont use it, we just get the appended strings.
        ## Also: dont forget to convert strings to integers with the int() function
        ### To print operation, just put the numbers in brackets equals the whole operation in brackets
        result = f'{int(num1)} + {int(num2)} = {int(num1) + int(num2)}'
        re = f'{int(num1) + int(num2)}'
        print('Result: ', result)
        h = f'[{i}] {result}'
        m = f'{re}'
    
    elif (operator == "subtract"):
        num1 = input('Enter the first number (Mi for result from i-th position in history) ')
        num2 = input('Enter the second number (Mi for result from i-th position in history) ')
        # Form demanded in assignment description:
        result = f'{int(num1) - int(num2)}'
        re = f'{int(num1) - int(num2)}'
        print('Result: ', result)
        # we need to put the nums in brackets, otherwise we just print "num1" and "num2" (in red) 
        res = f'subtract {num1} {num2} -> {int(num1) - int(num2)}'
        h = f'[{i}] {res}'
        m = f'{re}'
    
    elif (operator == "multiply"):
        num1 = input('Enter the first number (Mi for result from i-th position in history) ')
        num2 = input('Enter the second number (Mi for result from i-th position in history) ')
        result = f'{int(num1)} * {int(num2)} = {int(num1) * int(num2)}'
        re = f'{int(num1) * int(num2)}'
        print('Result: ', result)
        h = f'[{i}] {result}'
        m = f'{re}'
    
    elif (operator == "divide"):
        num1 = input('Enter the first number (Mi for result from i-th position in history) ')
        num2 = input('Enter the second number (Mi for result from i-th position in history) ')
        re = f'{int(num1) / int(num2)}'
        result = f'{int(num1)} / {int(num2)} = {int(num1) / int(num2)}'
        print('Result: ', result)
        h = f'[{i}] {result}'
        m = f'{re}'

    elif (operator == "end"):
        # break command: breaks the code and puts you back to the terminal
        break

    elif (operator == "history"):
        print(*lists, sep = '\n')
        continue
    # appending the calculated result to the empty list
    lists.append(h)
    listM.append(re)
    print(m)
    print(listM)

# add one in the index at the end of each operation
## IMPORTANT! Put it inside the "while level", otherwise it wont sum by each operation
    i = i + 1
