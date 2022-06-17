#Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve
#receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e
#o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para
#valores dentro da faixa de forma elegante.

def caixa_elegante(linha, coluna):
    resp = False
    while not resp:
        if linha > 20 or linha < 1:
            linha = 20
        if coluna > 20 or coluna < 1:
            coluna = 20
        resp = True
    print('+-' + "-" * linha + '-+')
    for i in range(coluna):
        print("| " + " " * linha + " |")
    print('+-' + "-" * linha + '-+')
print(caixa_elegante(int(input("Digite a largura de sua caixa: ")), int(input('Digite a altura de sua caixa: '))))
print()
