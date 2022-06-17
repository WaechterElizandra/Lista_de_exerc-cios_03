#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
#quadrados dos elementos do vetor.
a = [ 1, 2, 3, 78, 22, 7, 5, 8, 25, 6 ]
soma = 0
for x in range ( 10 ):
     soma = soma + (a [len(a)-1]**2)
print("A soma dos quadrados é " + str(soma))