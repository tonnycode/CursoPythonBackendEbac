minha_lista = {}

def adicionar_produtos():
    confirmar = 'sim'
    while confirmar in ['sim','s']:
        nome = input('digite o nome do produto: ').lower().strip()
        quantia = int(input('digite a quantiade do produto {}: '.format(nome)))
        preco = float(input('digite o preco do produto {}: '.format(nome)))

        if nome not in minha_lista: 
            minha_lista[nome] = {
                'quantidade':  quantia,
                'preco': preco
            }
            print('produto cadastrado com sucesso')
        else: 
            print('produto ja esta dentro da lista!!!')

        print()
        print('deseja continuar? ')
        confirmar = input('sim/nao: ').lower().strip()


def organizar_produtos():
    organizada = sorted(minha_lista.items())

    for nome, dados in organizada:
        print(nome, dados )


def remover_produtos():
    continuar = 'sim'
    while continuar in ['sim', 's']: 
        print('deseja remover algum produto? ')
        continuar = input('sim/nao').lower().strip()

        if continuar in ['sim','s']:
            excluir = input('digite o nome do produto na qual vc deseja retirar: ').lower().strip()

            if excluir not in minha_lista: 
                print('produto nao encontrado')
            else: 
                del minha_lista[excluir]
                print('produto escluido')


def atualizar_quantidade():
    print()
    nome = input('digite o nome do produto ja existente: ')
    if nome in minha_lista:
        nova_quantidade = int(input('nova quantidade'))
        minha_lista[nome]['quantidade'] = nova_quantidade
        print('quantidade atualizada com sucesso!!!')
    else: 
        print('produto nao encontrado')

while True:
    print('---MENU---')
    print('adicionar produtos - 1')
    print('produtos organizada - 2')
    print('remover produtos - 3')
    print('atualizar produtos - 4')
    print('sair - 5')

    opcao = int(input('escolha uma das opcoes: '))
    while opcao not in [1,2,3,4,5]:
        print('opcao invalida tente novamente')
        opcao = int(input('escolha entre \n''adicionar produto - 1\n''produtos organizados - 2\n''remover produtos - 3\n''atualizar produtos - 4\n''sair - 5'))
    if opcao == 1: 
        adicionar_produtos()
    elif opcao == 2: 
        organizar_produtos()
    elif opcao == 3:
        remover_produtos()
    elif opcao == 4: 
        atualizar_quantidade()
    else: 
        break 