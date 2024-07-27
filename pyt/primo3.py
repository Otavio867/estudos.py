import math

num = int(input("Digite um número inteiro: "))

if num <= 1:
    print("não primo")
else:
    primo = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            primo = False 
            break
    if primo:
        print("primo")
    else:
        print("não primo")
