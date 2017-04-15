import platform, os
from queue import queue

def menu(queue):
    clear()
    queuePrint(queue)
    print('1. insert')
    print('2. out')
    print('3. exit')
    x = int(input('select: '))
    return x

def queuePrint(queue):
    print('queue now:')
    queue.printQueue()
    print('\n')

def clear():
    name = platform.system()
    os.system('clear' if name == 'Linux' else 'cls')
