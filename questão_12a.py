#Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes (os
#elementos devem ser inteiros). Se as matrizes forem de tamanhos compatíveis para multiplicação,
#multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da multiplicação.
p = int(input('Digite a dimensão p da matriz: '))
q = int(input('Digite a dimensão q da matriz: '))
a = [ ]
b = [ ]
produto = [ ]
n= 0
k=0
for i in range (p):
    n +=1
    a.append(int(input(f"Digite o {n}º número de A: ")))
for j in range(q):
    k +=1
    b.append(int(input(f'Digite o {k}º número de B: ')))
print(f'O conteúdo de A é: {a}'.replace(",", '').replace("[", '').replace("]", ''))
print(f'O conteúdo de B é: {b}'.replace(",", '').replace("[", '').replace("]", ''))
if len(a) == len(b):
    print(produto)
else:
    print('Os tamanho das duas matrizes não são iguais')