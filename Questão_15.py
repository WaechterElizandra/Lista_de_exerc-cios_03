#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de
#caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def posinegativo(n):
    if n > 0:
        print('Positivo')
    elif n == 0:
        print('Nulo')
    else:
        print('Negativo')
n = int(input('digite um número: '))
print('O número que você digitou é ', end=' ')
posinegativo(n)