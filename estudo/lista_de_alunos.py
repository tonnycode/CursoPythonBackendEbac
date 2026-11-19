alunos = [
    {'nome': 'João', 'nota': 8},
    {'nome': 'Maria', 'nota': 5},
    {'nome': 'Pedro', 'nota': 9},
    {'nome': 'Ana', 'nota': 4}
]

aprovados = []
recuperacao = []
reprovado = [] 

quantidade = len(alunos)

total = 0

for i in alunos:
    total += i['nota']
    if i['nota']>= 7:
        aprovados.append(i['nome'])
    elif i['nota'] >= 5:
        recuperacao.append(i['nome'])
    else:
        reprovado.append(i['nome'])

media = total/quantidade

print('os aprovados foram: {}'.format(aprovados))
print()
print('os de recuparacao foramm: {}'.format(recuperacao))
print()
print('os reprovados foram: {}'.format(reprovado))
print()
print('a media da sala foi: {}'.format(media))