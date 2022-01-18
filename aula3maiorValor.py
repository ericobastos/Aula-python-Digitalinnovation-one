#Variaveis (a,b,c) pede ao usuário que digite um número inteiro

print('Comparando maior de 3 números')
a = int(input('Entre com primeiro número inteiro:'))
b = int(input('Entre com segundo número inteiro:'))
c = int(input('Entre com terceiro número inteiro:'))

#Essa condição faz a comparação dos números inseridos e retorna o maior número
if a > b and a > c:
    print('O valor maior é A: {}'.format(a))
elif b > a and b > c:
    print('O mairo valor é B: {}'.format(b))
elif c > a and c > b:
    print('O maior valor é C: {}'.format(c))
else:
    print('Todos números digitado são iguais')
print('-' * 30)


print('Identifica se o número inserido é par!!!')
#pede para usuário digitar um número
a = int(input('Digite um número:'))

#Faz a divisão e pega o resto
resto = a % 2

#Condicional, se resto for 0 é par, se não impar
if resto == 0:
    print('Número é {} par'.format(a))
else:
    print('Número {} não é par'.format(a))
print('-'*30)

#Pedindo ao usuário digitar 2 número inteiros
print('Descobrindo se foi digitado número par')
a = int(input('Digite um número:'))
b = int(input('Digite um número:'))

#Pegando o resto da divisão
resto_a = a % 2
resto_b = b % 2

#Condição para saber se algum dos números digitados é par
if resto_a == 0 or resto_b == 0:
    print('Um número par foi digitado')
else:
    print('nenhum número par foi digitado')
print('-'*30)

#Usuário informa as 4 notas bimestral
print('Tirando a média de notas bimestral')
a = float(input('Nota primeiro bimestre:'))
b = float(input('Nota segundo bimestre:'))
c = float(input('Nota terceiro bimestre:'))
d = float(input('Nota quarto bimestre:'))

#Tirando a média das notas
media = (a+b+c+d)/ 4

#condição da media
if media == 10:
    print('Aprovado com destinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
print('-'*30)