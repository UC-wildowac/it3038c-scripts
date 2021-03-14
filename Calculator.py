def calculate():
    operation = input('''
What are you trying to do?:

+ to add

- to subtract

* to multiply

and / to divide
''')

    firstNumber = int(input('What is your first number?: '))
    secondNumber = int(input('What is your second number?: '))

    if operation == '+':
        print('{} + {} = '.format(firstNumber, secondNumber))
        print(firstNumber + secondNumber)

    elif operation == '-':
        print('{} - {} = '.format(firstNumber, secondNumber))
        print(firstNumber - secondNumber)

    elif operation == '*':
        print('{} * {} = '.format(firstNumber, secondNumber))
        print(firstNumber * secondNumber)

    elif operation == '/':
        print('{} / {} = '.format(firstNumber, secondNumber))
        print(firstNumber / secondNumber)

    else:
        print('You entered something wrong, try again.')

    again()

def again():
    calc_again = input('''
Wanna do another one?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Later loser.')
    else:
        again()

calculate()