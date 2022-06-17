#Faça um programa que leia duas matrizes A e B 2x2 de inteiros e imprima a matriz C que é a soma
#das matrizes A e B.
a = [78, 87]
b = [52, 25]
c = a[0] + a[1] + b[0] + b[1]
print(f'O números de A são: {a}'.replace(",", '').replace("[", '').replace("]", ''))
print(f'Os números de B são: {b}'.replace(",", '').replace("[", '').replace("]", ''))
print('A soma de A e B é = ', c)