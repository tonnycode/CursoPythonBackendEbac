print('---MENU---')
print('digite a nota pra saber qaunto vc precisa pra passar, voce pode escolhe os bimestres, \n' \
'lembrando que sao 4 bismetres e a nota vai ate 10')

bimestre = int(input('digite quantos bimestres ja passaram: '))

certo = 'errado'

while certo == 'errado':
    if bimestre >= 4 or bimestre < 1: 
        print('erro')
        bimestre = int(input('digite quantos bimestres ja passaram: '))
    else: 
        print('certo')
        certo = 'certo'

dicionario_materias = {}

confirmar = 'sim'

while confirmar in ['sim','s']:
    print()
    print('escolha a materia que vc quer colocar suas notas: ')
    print()
    print('matematica = 1 \nportugues = 2 \nhistoria = 3')
    print()

    opcao = int(input('digite uma opcao: '))

    while opcao not in [1,2,3]:
            print('erro, opcao invalida')
            opcao = int(input('digite uma opcao: '))

    if opcao == 1: 
        materia = 'matematica'
    elif opcao == 2: 
        materia = 'portugues'
    else: 
        materia = 'historia'

    if materia in dicionario_materias: 
        print('materia ja cadastrada')
        continue
    else: 
        dicionario_materias[materia] = [] 

    soma = 0

    for i in range(1, bimestre + 1): 
        notas = float(input(f'digite a nota do {i} bimestre da materia de {materia}: '))
        soma += notas
        dicionario_materias[materia].append(notas)

    media = sum(dicionario_materias[materia]) / len(dicionario_materias[materia])

    print(f'na materia {materia} sua nota é {media:.2f}')
    if media < 6: 
        print(f'falta {6 - media:.2f} para passar ')
    else: 
        print('voce passou')

    if bimestre < 4: 
        pontos_faltantes = 24 - sum(dicionario_materias[materia])
        bimestre_faltantes = 4 - len(dicionario_materias[materia])

        nota_necessaria = pontos_faltantes / bimestre_faltantes

        if nota_necessaria <=0:
            print('voce n precisa de pontos')
        elif nota_necessaria <= 10: 
            print(f'voce precisa de {nota_necessaria:.2f} para passar')
        else: 
            print('nao é possivel mais atingir a nota 6')

    else:
        if media >= 6: 
            print('voce passou')
        else:
            print('voce n atingiu a media necessaria')
            
    acesso = input('deseja acessar qual materia?: ')

    while acesso not in dicionario_materias:
        print('materia n encontrada')
        acesso = str(input('tente novamete: ')).lower().strip()

    print(dicionario_materias[acesso])

    print('deseja continuar? ')
    confirmar = input('digite sim/nao: ').lower().strip()
    if confirmar in ['sim', 's']: 
        print('entao vamos la')
    else: 
        break 