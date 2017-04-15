import platform, os
from stack import stack

def menu(stack):
    clear()
    stackPrint(stack)
    print('1. push')
    print('2. pop')
    print('3. exit')
    x = int(input('select: '))
    return x

def stackPrint(stack):
    print('stack now:')
    stack.printStack()
    print('')

def clear():
    name = platform.system()
    os.system('clear' if name == 'Linux' else 'cls')
