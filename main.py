from LB4 import CalcMath

calc=CalcMath(x=0.4e+4, y=-0.875, z=-0.475e-3)


res=calc()

print("w=", res, "при x=", calc.x, "y=", calc.y, "z=", calc.z)