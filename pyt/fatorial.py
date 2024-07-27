import math
n=int(input("Digitev o valor de n: "))
if n<0:
    n=False
else:
    print(math.factorial(n))