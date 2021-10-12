import math
from math import fabs

class CalcMath:

    def __init__(self, x, y, z):
        self.__x=x
        self.__y=y
        self.__z=z

    @property
    def x (self):
        return self.__x

    @property
    def y (self):
        return self.__y

    @property
    def z (self):
        return self.__z

    def __call__(self):
        res=math.fabs(math.cos(self.x)-math.cos(self.y))

        res1=(1+2*(math.pow(math.sin(self.y),2)))

        res3=math.pow(res,res1)

        res4=(1+self.z+(math.pow(self.z,2))/2)+((math.pow(self.z,3))/3)+((math.pow(self.z,4))/4)

        w=res3*res4

        return w
        
        

