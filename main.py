meu_arrayzinho = [1,2,3,3,4,4,5,6,7,1,2]

meu_arrayzinho.sort()

meu_dicionario = {}

for i in meu_arrayzinho:
    if i not in meu_dicionario: 
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1

for chave, valor in meu_dicionario.items(): 
    if chave == valor: 
        print('numero sortudo é {}'.format(chave))
