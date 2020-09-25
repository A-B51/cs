# Interactive Calculator

# index
i = 1

# empty list for history
lists = []

while True:
    operator = input('Please enter operator [add/subtract/multiply/divide/end/history]: ')

    if (operator == 'add'):
        num1 = input('Enter the first number (Mi for result from i-th position in history): ')
        num2 = input('Enter the second number (Mi for result from i-th position in history): ')
        
        # Use the 'startwith' to determine what number of history you wanna retrieve after M 
        if num1.startswith('M'):

            # selecting the list element based on the number that comes after M (remember starting element of a list is 0!)
            num1 = lists[int(num1[1:]) - 1]

            # when selected, redefine the 'num1' to what comes after the string index you determine. Dont forget to transform it to
            ## a floating point! Also remember to add the 2 at the end, cuz we have the space
            num1 = float(num1[num1.index('>') + 2:])
        
        # now for number 2
        if num2.startswith('M'):
            num2 = (lists[int(num2[1:]) - 1])
            num2 = float(num2[num2.index('>') + 2:])

        # f syntax: if we dont use it, we just get the appended strings.
        ## Also: dont forget to convert strings to integers with the int() function
        ### To print operation, just put the numbers in brackets equals the whole operation in brackets
        result = f'add {num1} {num2} -> {float(num1) + float(num2)}'
        print('Result: ', result)

        # The history list for the history function
        h = f'[{i}] {result}'
    
    elif (operator == "subtract"):
        num1 = input('Enter the first number (Mi for result from i-th position in history) ')
        num2 = input('Enter the second number (Mi for result from i-th position in history) ')
        
        if num1.startswith('M'):
            num1 = lists[int(num1[1:]) - 1]
            num1 = float(num1[num1.index('>') + 2:])

        if num2.startswith('M'):
            num2 = lists[int(num2[1:]) - 1]
            num2 = float(num2[num2.index('>') + 2:])
            
        # Form demanded in assignment description:
        result = f'{float(num1) - float(num2)}'
        print('Result: ', result)
        # we need to put the nums in brackets, otherwise we just print "num1" and "num2" (in red) 
        res = f'subtract {num1} {num2} -> {float(num1) - float(num2)}'
        h = f'[{i}] {res}'
    
    elif (operator == "multiply"):
        num1 = input('Enter the first number (Mi for result from i-th position in history) ')
        num2 = input('Enter the second number (Mi for result from i-th position in history) ')

        if num1.startswith('M'):
            num1 = lists[int(num1[1:]) - 1]
            num1 = float(num1[num1.index('>') + 2:])

        if num2.startswith('M'):
            num2 = lists[int(num2[1:]) - 1]
            num2 = float(num2[num2.index('>') + 2:])

        result = f'multiply {num1} {num2} -> {float(num1) * float(num2)}'
        print('Result: ', result)
        h = f'[{i}] {result}'
    
    elif (operator == "divide"):
        num1 = input('Enter the first number (Mi for result from i-th position in history) ')
        num2 = input('Enter the second number (Mi for result from i-th position in history) ')
        
        if num1.startswith('M'):
            num1 = lists[int(num1[1:]) - 1]
            num1 = float(num1[num1.index('>') + 2:])

        if num2.startswith('M'):
            num2 = lists[int(num2[1:]) - 1]
            num2 = float(num2[num2.index('>') + 2:])

        result = f'divide {num1} {num2} -> {float(num1) / float(num2)}'
        print('Result: ', result)
        h = f'[{i}] {result}'

    elif (operator == "end"):
        # break command: breaks the code and puts you back to the terminal
        break

    elif (operator == "history"):
        print(*lists, sep = '\n')
        continue
    
    # appending the calculated result to the empty list
    lists.append(h)
    print(lists)

# add one in the index at the end of each operation
## IMPORTANT! Put it inside the "while level", otherwise it wont sum by each operation
    i = i + 1
