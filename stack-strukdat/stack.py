class stack:
    def __init__(self,stack):
        self.stack = stack

    def push(self,value):
        self.stack.insert(0,value)

    def pop(self):
        top = self.stack[0]
        self.stack.remove(top)

    def printStack(self):
        x = len(self.stack)-1
        if x < 0:
            print('empty stack')
        else:
            for i in self.stack:
                print('|',i,'|')
