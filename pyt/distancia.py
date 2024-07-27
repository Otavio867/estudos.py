import math

num_x1=float(input("Digite o valor de x1: "))
num_y1=float(input("Digite o valor de y2: "))
num_x2=float(input("Digite o valor de x2: "))
num_y2=float(input("Digite o valor de y2: "))

distância=math.sqrt((num_x2-num_x1)**2+(num_y2-num_y1))

if distância>=10:
    print("longe")
else:
    distância<10
    print("perto")