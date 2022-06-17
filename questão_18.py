#Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
#formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data
#seja inválida.
def dataExtensa(dia, mes, ano):
    mes_ext = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", 'Setembro', "Outubro",
               'Novembro', 'Dezembro']
    if mes or dia > 12 or dia or mes < 1:
        return print("NULL")
    else:
        return print(f'Data: Dia {dia}, de {mes_ext[mes]} de {ano} ')
print(dataExtensa(int(input('Dia: ')), int(input('Mês: ')), int(input('Ano: '))), end='')
