#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses
#três argumentos.
def somar(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))

print('A soma dos números digitados é = ', somar(n1, n2, n3))