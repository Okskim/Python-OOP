import math

class ListNum:
    __slots__=('args', 'k', 'j')
   
    def __init__(self):        
        self.args=list(range(0,0))
        print('[список: %s]' % (self.args))


    def __call__(self, k, j):
        for i in range(k, j):
            if i % 2 != 0:
                self.args.append(math.pow(i,2)+1)
            elif i % 2 == 0:
                self.args.append(2*i-1)         
        print(self.args)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index=self.index-1
        return self.args[self.index]

