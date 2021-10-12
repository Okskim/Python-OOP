from LB9 import ListNum


class ListNumCopy(ListNum):
    __slots__=('i')

    def enumeration(self, k, j):        
        for i in range(k,j):
            if i < 2.5:
                self.args.append(2.5*i)
            elif i >= 2.5:
                self.args.append(i/2.5)        
        print(self.args)