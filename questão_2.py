#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os
#números.
numeros = [7, 45, 12, 36, 94]
soma = multi = 0
for i in range(len(numeros)):
    if i < 1:
        soma += numeros[i]
        multi += numeros[i]
    elif i >= 1:
        soma += numeros[i]
        multi *= numeros[i]
print(f'Dados os valores: {numeros}'.replace("[", '').replace("]", ""))
print('A soma dos valores é: ',soma)
print('O produto dos valores é: ',multi)