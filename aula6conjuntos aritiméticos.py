conjunto = {1, 2, 3,}
conjunto1 = {1, 2, 3, 4, 5}

#Faz a união dos conjuntos
conjunto_uniao = conjunto.union(conjunto1)
print(conjunto_uniao)

#Mostra objetos repetidos
conjunto_intercçao = conjunto.intersection(conjunto1)
print(conjunto_intercçao)

#traz oque nao tem
conjunto_diferença =  conjunto1.difference(conjunto)
print(conjunto_diferença)

#traz oque não tem
conjunto_simetrico = conjunto.symmetric_difference(conjunto1)
print(conjunto_simetrico)

# cojunto e subset de conjunto1
# conjunto tem tudo oque tem no conjunto1
conjunto_subset = conjunto.issubset(conjunto1)
print(conjunto_subset)


lista = ['gato', 'cachorro', 'cachorro']

conjunto_animal = set(lista)
print(type(conjunto_animal))
print(conjunto_animal)
lista_animal = list(conjunto_animal)
print(type(lista_animal))
print(lista_animal)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = { 5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)   # union=uniao comando faz a união dos dois conjuntos
print(conjunto_uniao)
# comando union=união ele junta os conjuntos
print('uniao: {}'.format(conjunto_uniao))
conjunto_intersecçao =conjunto.intersection(conjunto2) #intersecção esse comando pega tudo que se repete
print('intersecçao: {}'.format(conjunto_intersecçao))
conjunto_diferença1 = conjunto.difference(conjunto2) #diferença entre conjuntos tudo que não tem no conjunto
conjunto_diferença2 = conjunto2.difference(conjunto)                                             #do parametro
print('diferença entre 1 e 2: {}'.format(conjunto_diferença1))
print('diferença entre 2 e 1: {}'.format(conjunto_diferença2))
conjunto_diferença_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferença simetrica: {}'.format(conjunto_diferença_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b ={1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B e superconjunto de A: {}'.format(conjunto_superset))

lista = ['gato', 'cachorro', 'lobo', 'lobo']
conjunto_animal =set(lista)
print(conjunto_animal)
lista_animal =list(conjunto_animal)
print(lista_animal)

# conjuntos são feitos com chaves
# conjunto não permite duplicidade ou seja se temm dois elementos ex: {5, 5} só um sai no print


conjunto = {1, 2, 3, 4, 4,}
conjunto.add(5) # adiciona objeto a lista
conjunto.discard(5) # discard descarta elemento indicado por parametro
print(conjunto)