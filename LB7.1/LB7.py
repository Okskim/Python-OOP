import math

class ListRange:
    __slots__=('args', 'args1', 'k', 'j') 
    
    def __init__(self):
        self.args=list(range(0,0))       
        print("список: ", self.args)   

    def __call__(self, k, j):               
        for i in range(k,j):
            self.args.append(i)
        print("список: ",self.args)

    def enumeration(self, args, args1):         
        for i in args:
             args1.append((5*i+math.pow(math.cos(i),2))/2.35)
        print("список: ",args1)

    def enumeration1(self, args, args1):
        for i in args:
            args1.append(0.13*(math.pow(i,3))-2.5*i+8)
        print("список: ",args1)

    def negativeNumbers(self, args):
        for i in args:
            if i < 0:
               print(i)      
        print("Отрицательные числа отсутствуют")