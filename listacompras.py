def menu():
    print('=======================')
    print('1-Adicionar produto')
    print('2-Remover produto')
    print('3-Pesquisar produto')
    print('4-Mostrar lista de compras')
    print('5-Sair do programa')
    print('=======================')

def lista_funcoes():
    lista_compras = {}
    while True:
        menu()
        opcao=input('Selecione uma opção: ')
        if opcao == '1':
            produto = input('\nQual produto você deseja adicionar? ')
            lista_compras.append(produto)
            print(f'\n{produto} foi adicionado à lita de compras.')
        elif opcao == '2':
            produto = input('\nQual produto você deseja remover? ')
            if produto in lista_compras:
                lista_compras.remove(produto)
                print(f'\n{produto} foi removido da lista de compras')
            else:
                print(f'\n{produto} não foi encontrado na lista de compras')
        elif opcao == '3':
            produto = input('\nQual produto você deseja encontrar na lista? ')
            if produto in lista_compras:
                print(f'\n{produto} está na lista de compras.')
            else:
                print(f'\n{produto} não está na lista de compras.')
        elif opcao == '4':
            if lista_compras:
                print('\nLista de compras: ')
                for produto in lista_compras:
                    print(f'\n-{produto}')
            else:
                print('\nA lista de compras está vazia.')
        elif opcao == '5':
            print('\nSaindo do programa')
            break
        else:
            print('\nOpção inválida! Por favor, escolha uma opção válida.')
    print('\nPrograma encerrado')

lista_funcoes()