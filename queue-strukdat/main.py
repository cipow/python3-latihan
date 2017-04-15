from menu import *
from queue import queue

queue = queue([])
loop = True

while loop:
    try:
        select = menu(queue)
        if select == 1:
            print('')
            value = int(input('value to insert: '))
            queue.insert(value)
        elif select == 2:
            queue.out()
        elif select == 3:
            loop = False
        else:
            raise Exception('no found\n')
    except Exception as e:
        print(e)
