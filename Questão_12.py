#Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes (os
#elementos devem ser inteiros). Se as matrizes forem de tamanhos compatíveis para multiplicação,
#multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da multiplicação.
a = [45, 13, 25, 62]
b = [85, 56, 2, 29]
print(f'O conteúdo de A é: {a}'.replace(",", '').replace("[", '').replace("]", ''))
print('A apresenta:',len(a), 'números')
print(f'O conteúdo de B é: {b}'.replace(",", '').replace("[", '').replace("]", ''))
print('B apresenta:',len(a), 'números')
if len(a) == len(b):
    produto = a[0] * a[1] * a[2] * a[3] * b[0] * b[1] * b[2] * b[3]
    print('O produto das matrizes é:', produto)
else:
    print('Os tamanho das duas matrizes não são iguais')