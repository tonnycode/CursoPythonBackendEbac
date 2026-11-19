nome = input('digite seu nome: ').strip()
idade = int(input('digite sua idade: '))

print('')

if idade < 18:
    print('{} voce é menor de idade'.format(nome))
else:
    print('{} voce é maior de idade'.format(nome))