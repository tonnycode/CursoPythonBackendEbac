
lista_alunos = [] 

quantidade = int(input('quantos alunos deseja cadastrar? : '))
print()

for i in range(quantidade):

    aluno = input('digite o nome do aluno: ')
    nota = float(input('digite a nota do aluno:'))
    print()

    dados_alunos = {
        "nome": aluno,
        "nota": nota
    }
    lista_alunos.append(dados_alunos)

passou = 0
recuperacao = 0
repetiu = 0 

print(lista_alunos)

for alunos in lista_alunos:
    if alunos["nota"] >= 7:
        print('o aluno(a) {} foi aprovado(a)'.format(alunos["nome"]))
        passou += 1
    elif alunos["nota"] >= 5:
        print('o aluno(a) {} esta de recuperacao'.format(alunos["nome"]))
        recuperacao += 1
    else:
        print('o aluno(a) {} nao passou'.format(alunos["nome"]))
        repetiu += 1

print() 
print("---Total---")
print()
print("passaram: ", passou)
print("recuperacao: ", recuperacao)
print("repetiu: ", repetiu)