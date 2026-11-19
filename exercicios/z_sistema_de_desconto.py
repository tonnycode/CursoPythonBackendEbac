nome = input('digite seu nome: ').strip()
valor_total_compra = float(input('digite o valor da compra: '))

#desconto
op1 = valor_total_compra / 15
op2 = valor_total_compra / 10

if valor_total_compra >= 200: 
    print('voce obteve um desconto de {}R$ foi para {}R$ !!!'.format(valor_total_compra, valor_total_compra - op1))
elif valor_total_compra >= 100:
    print('voce obteve um desconto de {}R$ foi para {}R$ !!!'.format(valor_total_compra, valor_total_compra - op2))
else:
    print('o valor foi de {}R$ '.format(valor_total_compra))