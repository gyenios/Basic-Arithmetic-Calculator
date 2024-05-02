import operator

# op is a list containing the actual operator names as defined in the operator module
op = ['add','sub','mul','truediv']

def calc(operator,x,y):
    
    # The getattr function converts op into an actual operator defined by the operation function 
    operation = getattr(operation, operator)
    return operation(x,y)

def menu():
    print('''
    BASIC CALCULATOR OPERATIONS
    [1] Add
    [2] Subtract
    [3] Multiply
    [4] Divide
    ''')

    a = 0
    while a == 0:
        n = int(input('Enter a number to pick an operation '))
        if n in range(5):
            while True:
                try:
                    x = int(input('Operand 1: '))
                    y = int(input('Operand 2: '))
                    break
                except ValueError:
                    print('Enter an integer')
            a = 1
        else:
            print('Invalid Input')
    return [n,x,y]

n,x,y = menu()
operator = op[n-1]
print(calc(operator,x,y))

