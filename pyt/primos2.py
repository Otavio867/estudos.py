n=int(input('Digite um número inteiro: '))

x = 1 
div = 0

while x <= n:
    resto = n % x
    if resto == 0:
        div += 1 
    x += 1 
if div == 2: 
  print("primo")
else:
  print("não primo")