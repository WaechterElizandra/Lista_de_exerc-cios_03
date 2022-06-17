#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato
#de escada.
nome = str(input("Digite seu nome: ").upper().replace(" ", ''))
nome_for = []
for i in range(len(nome)):
    nome_for.append(nome[i])
    print(f'{nome_for}'.replace("['", '').replace("']", '').replace("', '", ''))