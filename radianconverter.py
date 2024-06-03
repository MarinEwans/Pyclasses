import math
radian = float(input("input the radian you want to convert:"))
def Radian_Converter(radian):
   degree = radian * (180 / math.pi)
   return degree
print(Radian_Converter(radian))