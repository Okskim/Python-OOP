class ClassDescriptor:
    __slots__=("args",)
    __stack={}

    def __init__(self, args):
          self.args=args

    def __set__ (self, instance, value):
          self.__stack[id(instance), self.args]=value

    def __get__ (self, instance, owner=None):
          if instance is None:
              return self
          return self.__stack[id(instance), self.args]


