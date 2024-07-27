n=int(input("Digite um número inteiro: "))

div1=n%10
div2=n//10
soma=0

while n!=0:
  if div1>=0:
    div1=n%10
    n=n//10
    soma=soma+div1
if div1<=0:
  n=n//10
  div1=n%10
  div2=(n-div1)//10
  soma=soma+div1+div2

print(soma)