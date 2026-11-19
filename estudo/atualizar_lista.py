
produtos = [
{'nome': 'Mouse', 'estoque': 10},
{'nome': 'Teclado', 'estoque': 5},
{'nome': 'Monitor', 'estoque': 3}
]
def atualizar_estoque(produtos, nome, quantidade):

    for i in produtos:
        if nome == i['nome']: 
            i['estoque'] += quantidade
            return produtos
        
        return 'esse produto n existe'

print(produtos)
print()
print('os produtos foram atualizados para:')
resultado = atualizar_estoque(produtos,'Mouse', 5)
print(resultado)