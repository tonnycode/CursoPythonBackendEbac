#calculadora

# sistema loop - verifica uma informacao de continuidade do programa
continuar = 'sim'
while continuar == 'sim':

# menu 
    print('calculadora')

    print('1: soma')
    print('2: subtracao')
    print('3: multiplicacao')
    print('4: divisao')

# variaveis - adere valores ou nomes a um variavel 
    opcao = input('digite uma opcao: ')
    num1 = float(input('digite um numero: '))
    num2 = float(input('digite outro numero: '))

# sistema de condicoes - verifica as codicoes usando(if,elif,else)
    if opcao == '1':
        print('resultado:', num1 + num2) 
    elif opcao == '2':
        print('resultado:', num1 - num2)
    elif opcao == '3': 
        print('resultado:', num1 * num2)
    elif opcao == '4': 
        if num2 == 0: 
            print('errado')
        else:
            print('resultado:', num1 / num2)
    else: 
        print('invalido')

#confirmacao do loop
    print('deseja continuar [sim/nao]')
    continuar = input('resposta:' )

print('obrigado volte sempre ')