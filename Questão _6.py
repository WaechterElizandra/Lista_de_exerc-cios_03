#Faça um programa que leia 2 strings
# informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
nome = ("ELIZANDRA ")
sobrenome = ("WAECHETER")
diferente = [ ]
print(nome + sobrenome)
print('Seu nome tem ', len(nome), 'letras')
print('Seu sobrenome tem ', len(sobrenome), 'letras')
if nome != sobrenome:
    print("Nome e sobrenome não têm o mesmo tamanho")
else:
    print('Nome e sobrenome tem o mesmo tamanho')


