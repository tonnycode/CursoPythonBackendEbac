import random

print('---Menu---')
print()
print('jogo papel, pedra e tesoura')
print()

def regras_do_jogo():
    print('regras do jogo:')
    print('papel > pedra')
    print('pedra > tesoura')
    print('tesoura > papel')
    print('adendos: ')
    print('se obejo igual a o objeto q o adversario escolheu, dara empate')
regras_do_jogo()

print()
print('deseja proseguir? ')
continuar = input('continuar sim/nao: ').lower()
print()

total_robo = 0 
total_jogador = 0

if continuar in ['sim','s']: 
    
    opcao = 'sim'
    while opcao in ['sim','s']: 
        
        lista_jogo = ['pedra','tesoura', 'papel']

        robo = random.choice(lista_jogo)
        escolha_robo = robo

        jogador = input('selecione um pra jogar: ').lower()
        escolha_jogador = jogador

        while escolha_jogador not in lista_jogo: 
            print('invalido')
            jogador = input('selecione um pra jogar: ').lower()
            escolha_jogador = jogador
#empate
        if escolha_robo == escolha_jogador: 
            print('empate')
#pontos para o jogador
        elif escolha_robo == 'pedra' and escolha_jogador == 'papel': 
            total_jogador += 1
            print('jogador ganhou essa rodada ')
        elif escolha_robo == 'tesoura' and escolha_jogador == 'pedra': 
            total_jogador += 1
            print('jogador ganhou essa rodada ')
        elif escolha_robo == 'papel' and escolha_jogador == 'tesoura': 
            total_jogador += 1
            print('jogador ganhou essa rodada ')
#pontos para o robo
        else: 
            total_robo += 1
            print('robo ganhou essa rodada')

        print()
        print('o robo escolheu {} '.format(escolha_robo))
        print('o jogador escolheu {} '.format(escolha_jogador))
        print()

        print('pontos atuais dos participantes: ')
        print('robo: {}'.format(total_robo))
        print('jogador: {}'.format(total_jogador))
        print()
        retornar = input('gostaria de ver as regras do jogo novamente? : ').lower()

        if retornar in ['sim', 's']: 
            regras_do_jogo()
        print()
        opcao = input('deseja continuar jogando? sim/nao: ')
else:
    print('encerrou o jogo ')