n=int(input('Digite um número inteiro: '))

if n==2:
  print("primo")
elif n<=1 and n%2==0:
 print("não é primo")
else:
  if n%n==0 and n%1==0:
    print("primo")