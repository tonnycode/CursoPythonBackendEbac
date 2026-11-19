nome = input('digite seu nome: ').strip()
nota1 = float(input('digite sua nota: '))
nota2 = float(input('digite sua nota: '))
nota3 = float(input('digite sua nota: '))
nota4 = float(input('digite sua nota: '))

soma_notas = nota1 + nota2 + nota3 + nota4

media = soma_notas / 4

print(media)

if media >= 7: 
    print('{} voce foi aprovado'.format(nome))
elif media >= 5:
    print('{} voce passou por pouco'.format(nome))
else: 
    print('{} voce foi reprovado'.format(nome))