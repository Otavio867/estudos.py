n = int(input("Digite o valor de n: "))

cont_impar = 0
numero = 1

while cont_impar < n:
    if numero % 2 != 0:
        print(numero)
        cont_impar += 1
    numero += 1
