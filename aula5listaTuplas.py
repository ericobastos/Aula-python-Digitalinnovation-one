#tupla são imutaveis
tupla = (1, 2, 5, 9)
print(tupla)
#retorna quantos objetos tem
print(len(tupla))
#consigo converte um lista em uma tupla

lista_nu = [1, 2, 3, 6, 8]
lista = ['cora', 'bela', 'meg', 'thor']

#consulta se existe lobo se não adiciona
if 'lobo' in lista:
    print('Existe um lobo na lista')
else:
    print('Não existe um lobo na lista. Lobo será incluido!')
    lista.append('lobo')
    print(lista)
print('-'*30)


#Aqui faz uma consulta na lista e verifica se existe
#nome cora
if 'cora' in lista:
    print('existe um nome cora na lista')
else:
    print('não existe esse nome na lista')
print('-'*30)

# laço x passa por cada objeto de lista_nu
# variavel soma armazena o valor
soma = 0
for x in lista_nu:
    soma += x
print(soma)
print('-'*30)

#Soma objetos de lista_nu
print(sum(lista_nu))
print('-'*30)


#Lista de nomes
lista_nomes = ['bela', 'meg', 'thor', 'cora']
#Mostra o tipo de lista
print(type(lista_nomes))
#Traz o elemento 1 da lista lembrando que começa em 0
print(lista_nomes[1])
#Traz o maior objeto por letra alfabeto
print(max(lista_nomes))
#Traz a menor objeto por letra alfabeto
print(min(lista_nomes))
#Traz ultimo objeto
print(lista_nomes.pop())
#retira objeto bela da lista
lista_nomes.remove('bela')
#ordena lista
lista_nomes.sort()
#reverte a lista
lista_nomes.reverse()
