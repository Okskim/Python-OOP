from descriptor import ClassDescriptor
import math
from math import fabs

class CalcMath:
    x=ClassDescriptor("x")
    y=ClassDescriptor("y")
    z=ClassDescriptor("z")

    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __call__(self):
        res=math.log(math.pow(self.y,(-math.sqrt(math.fabs(self.x)))))

        res1=res*(self.x-self.y/2)

        res2=math.pow(math.sin(math.atan(self.z)),2)

        a=res1+res2

        return a