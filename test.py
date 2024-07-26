# Função para imprimir as opções do menu
def imprimir_menu():
    print("\n==============================")
    print("Bem-vindo à Lista de Compras")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Pesquisar produto")
    print("4 - Mostrar lista de compras")
    print("5 - Sair do programa")
    print("==============================")

# Função principal da aplicação
def main():
    lista_compras = {}  # Dicionário para armazenar os produtos e suas quantidades

    while True:
        imprimir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # Opção 1 - Adicionar produto
            produto = input("Digite o nome do produto que deseja adicionar: ")
            if produto in lista_compras:
                lista_compras[produto] += 1  # Incrementa a quantidade se o produto já existe
            else:
                lista_compras[produto] = 1  # Adiciona o produto com quantidade 1
            print(f"{produto} foi adicionado à lista de compras.")

        elif escolha == "2":
            # Opção 2 - Remover produto
            produto = input("Digite o nome do produto que deseja remover: ")
            if produto in lista_compras:
                if lista_compras[produto] > 1:
                    lista_compras[produto] -= 1  # Decrementa a quantidade se houver mais de um
                else:
                    del lista_compras[produto]  # Remove o produto se houver apenas um
                print(f"{produto} foi removido da lista de compras.")
            else:
                print(f"{produto} não encontrado na lista de compras.")

        elif escolha == "3":
            # Opção 3 - Pesquisar produto
            produto = input("Digite o nome do produto que deseja pesquisar: ")
            if produto in lista_compras:
                print(f"{produto} está na lista de compras ({lista_compras[produto]} unidades).")
            else:
                print(f"{produto} não encontrado na lista de compras.")

        elif escolha == "4":
            # Opção 4 - Mostrar lista de compras
            if lista_compras:
                print("\nLista de Compras:")
                for produto, quantidade in lista_compras.items():
                    print(f"- {produto}: {quantidade} unidades")
            else:
                print("\nLista de compras está vazia.")

        elif escolha == "5":
            # Opção 5 - Sair do programa
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    print("Programa encerrado.")

# Executar a função principal
if __name__ == "__main__":
    main()
