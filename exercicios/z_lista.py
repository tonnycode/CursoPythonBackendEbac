lista = [29.0, 120, 40, 50, 70, 45, 0]

soma = 0
mais_caro = 0

for i in lista:
    soma += i
    print(i)
    if mais_caro < i: 
        mais_caro = i

print("o produto mais caro é:{} ".format(mais_caro))
print("resultado da soma: {}".format(soma))
    