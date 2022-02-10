import functools


# Criando lista de 1 a 90
lista = list(range(1, 91))
# Exibindo a lista na tela
print('Lista de 1 a 90: ', lista)
# Pulando linha
print()
# Função lambda para filtrar os elementos divisiveis por 2 e 10
pares = list(filter(lambda n: (n % 2 == 0) and (n % 10 == 0), lista))
# Exibindo a lista 'pares'
print('Números pares e multiplos de 10: ',pares)
# Pulando linha
print()
# Filtrando da lista 'pares' os elementos divisiveis por 3
d3 = list(filter(lambda n: n % 3 == 0, pares))
print('Divisiveis por 3', d3)
# Pulando linha
print()
# Somando os elementos de d3
soma = functools.reduce(lambda a, b: a + b, d3)
print('Soma dos divisíveis por 3: ', soma)
