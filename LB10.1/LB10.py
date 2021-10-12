class StrDelRev:    
    __slots__=['str1', 'str', 'str2']

    def __init__(self, str):
        self.str=str
        print(str)
       

    def joinStr(cls, str):
        str2=str.split()
        print(str2)
        str3=" ".join(word[1:] for word in str2)
        print(str3)


    joinStr=classmethod(joinStr)
   

    def Rev(cls, str):
        str2=str.split()
        print(str2)            
        res=" ".join(i[0]+i[4]+i[2]+i[3]+i[1] for i in str2)
        print(res)

    rev=classmethod(Rev)