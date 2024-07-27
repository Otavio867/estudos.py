#5- Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

from math import pow

base = int(input("Digite a base da potência: "))
expoente = int(input("Digite o expoente da potência: "))
print(f"{base} elevado a {expoente} é igual a {pow(base, expoente)}")