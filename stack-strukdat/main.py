from stack import stack
from menu import *

stack = stack([])
loop = True

while loop:
    try:
        select = menu(stack)
        if select == 1:
            print('')
            value = int(input('value to push: '))
            stack.push(value)
        elif select == 2:
            stack.pop()
        elif select == 3:
            loop = False
        else:
            raise Exception('no found\n')
    except Exception as e:
        print(e)
