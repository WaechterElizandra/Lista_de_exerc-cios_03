def somaImposto(taxaImposto, custo):
    return (1 + taxaImposto/100)*custo
venda = somaImposto(float(input('Digite a taxa de imposto: ')), float(input('Digite o custo: ')))
print('Valor com imposto:', venda)