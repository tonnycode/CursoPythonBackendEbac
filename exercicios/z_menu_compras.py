q1 = 20 
q2 = 30
q3 = 10 
q4 = 12


produtos = {
    'banana': q1,
    'frango': q2,
    'arroz': q3,
    'ovo': q4
}
confirmar = 'sim'
while confirmar == 'sim':

    print('---MERCADO---')
    print('itens:')
    print(f"banana {produtos['banana']}")
    print(f"frango {produtos['frango']}")
    print(f"arroz {produtos['arroz']}")
    print(f"ovo {produtos['ovo']}")

    print('pegue um produto')
    usuario_pega = input('produto:').strip().lower
    item = produtos.get(usuario_pega)

    print() 

    if usuario_pega in produtos: 
        print(item)

        print()

        print('quantos vc deseja pegar?')
        quantidade = int(input('quantos vc quer:  '))

        if quantidade > item:
            print('nao tem como tem menos produtos que essa quantia')
        else:
            produtos[usuario_pega] = item - quantidade
            print('perfeito voce pegou {} e sobraram {}'.format(quantidade, item - quantidade))

    else: 
        print('produto nao encontrado, tente novamente')
    print()
    print('deseja continuar ou sair?')
    confirmar = input('repostas: ').lower()

    if confirmar == 'nao' or confirmar =='não' or confirmar == 'sair':
        print('obrigado volte sempre!!!')
        break
