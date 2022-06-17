#Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal principal
#da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação.
m_1 = [1, 2, 3]
m_2 = [4, 5, 6]
m_3 = [7, 8 , 9]
produto = m_1[0]* m_2[1] * m_3[2]
produto_1 = m_1[2]* m_2[1] * m_3[0]
print('O produto da 1ª diagonal é: ', produto)
print('O produto da 2ª diagonal é: ', produto_1)
