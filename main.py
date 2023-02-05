def adicionar_itens_estoque():
    itens_estoque = []
    nome = input('Nome do iten: ')
    descricao = input('Descrição do iten: ')
    quantidade = int(input('Quantidade do iten: '))
    itens = {'nome':nome, 'descricao':descricao,'quantidade':quantidade}
    itens_estoque.append(itens)
    print(itens_estoque)

if __name__ =="__main__":
    print('Sistema de estoque Ultima School\n')
    opcao = 0
    while opcao != 2:
        print('Menu de opições:')
        print(30*('='))      
        print('1 - Adicionar itens')
        print('2 - Sair\n')
        opcao = int(input('Selecione uma opção: '))

        if opcao ==1:
             adicionar_itens_estoque()
        elif opcao == 2:
            print('Obrigado por usar o nosso sistema.')
        else:
            print('Opção inválida.')

