produtos = [
    {'nome': 'Teclado', 'preco': 120.0, 'estoque': 5},
    {'nome': 'Mouse', 'preco': 80.0, 'estoque': 0},
    {'nome': 'Monitor', 'preco': 900.0, 'estoque': 3}
]
opcao = 0

while opcao != 4: 
    print('---MENU---')
    print('Escolhas as opcoes abaixo:')
    print()
    print('1 - mostrar todos os produtos: ')
    print('2 - mostrar produtos sem estoque: ')
    print('3 - mostrar produtos com preco acima de 100R$: ')
    print('4 - sair: ' )

    opcao = int(input('opcao: '))
    if opcao == 4: 
        print('obrigado pro usar o programa!!!')
        break
    elif opcao < 1 or opcao > 3: 
        print('opcao invalida')
    else: 
        for produto in produtos: 
            if opcao == 1:
                print(produto)
            elif opcao == 2: 
                if produto['estoque'] == 0: 
                    print(produto['nome'])
            elif opcao == 3:
                if produto['preco'] > 100:  
                    print(produto['nome'])