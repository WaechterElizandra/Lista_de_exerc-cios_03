#Faça um programa para imprimir:
#1
#1 2
#1 2 3
#.....
#1 2 3 ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
numero = int(input("digite um numero: "))
numero_for = []
for i in range(numero):
    numero_for.append(i + 1)
    print(f'{numero_for}'.replace("[", '').replace("]", '').replace(",", ' '))

