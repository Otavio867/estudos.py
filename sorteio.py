#6-Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.

from random import randint
# Transformando a quantidade de participantes de string para inteiro
n = int(input("Digite o nº de participantes do sorteio: "))
# Sorteando um número no intervalo de 1 até a quantidade de participantes
print(f"O número sorteado foi {randint(1, n)}")