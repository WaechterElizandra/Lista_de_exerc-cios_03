# Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
n = [8, 5, 3, 7, 4, 9, 2, 1, 6, 45 ]
m = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91 ]
juntos = [ ]
for i in range(10):
    juntos.append(n [i])
    juntos.append(m [i])
print(juntos)
