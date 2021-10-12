from LB10 import StrDelRev

__metaclass__=type

class StrRev(StrDelRev):
    def __init__(self, str):
        super (StrRev, self).__init__(str)
        print('[строка добавлена: %s]' % (str))

    
                   


