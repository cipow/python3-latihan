class queue:
    def __init__(self,queue):
        self.queue = queue

    def insert(self,value):
        self.queue.append(value)

    def out(self):
        first = self.queue[0]
        self.queue.remove(first)

    def printQueue(self):
        x = len(self.queue)-1
        if x < 0:
            print('empty queue')
        else:
            for i in self.queue:
                print(i,'<=',end=' ')
