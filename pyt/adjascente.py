def tem_digito_adjacente_igual(numero):
    num_str = str(numero)
    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            return True
    return False
def main():
    numero = int(input("Digite um número inteiro: "))
    if tem_digito_adjacente_igual(numero):
        print("sim")
    else:
        print("não")
if __name__ == "__main__":
    main()
