#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de
#cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
media = [ ]
acimadamedia = 0
for x in range ( 0, 10, 1):
    soma = 0
    for y in range ( 0, 4, 1 ):
        print('Informe a ', y + 1 , 'ª nota  do ', x + 1 ,'º aluno')
        soma =+ float(input())
    media.append (soma)
    if media [ x ] >= 7.0:
        acimadamedia += 1
print('As média dos alunos são: ', media)
print('O número de alunos acima da média é: ', acimadamedia)
