import math

a=float(input("Digite o vcalor de a: "))
b=float(input("Digite o vcalor de b: "))
c=float(input("Digite o vcalor de c: "))

delta=b**2-4*a*c

if delta<0:
    print("esta equação não possui raízes reais")
else:
    raiz1=(-b+math.sqrt(delta))/(2*a)
    raiz2=(-b-math.sqrt(delta))/(2*a)

    if raiz1//2==0 or raiz2//2==0:
        print("a raíz desta equação é", raiz1 or raiz2)
if delta>0:
    print("as raízers desta equação são ", raiz1, "e", raiz2)
    if raiz1>raiz2:
      print("as raízes desta equação são ", raiz1, "e", raiz2)
    else:
        raiz2>raiz1
        print("as raízes desta equação são ", raiz2, "e", raiz1)