
#Pede um número ao usuário
print('Digite um número para verificar se é primo!')
a = int(input('Entre com um número:'))

#Laço de repetição
div = 0
for x in range(1, a+1):
    resto = a % x
    if resto == 0:
        div += 1
if div == 2:
    print('Número {} é primo'.format(a))
else:
    print('Número {} não é primo'.format(a))
print('-'*30)
#Exemplo: digito 3 o laço vai percorrer 1,2,3
#e cada número que ele passa vai fazer uma divisão e pegar o resto
#e o resto sendo 0 a divisão ta correta
#div+1 concatena, toda vez que a divisão for por 2 números vai ser primo
#ou seja por 1 e por ele mesmo

#pede ao usuário que digite um número
print('Digite um número e veja todos os números primos')
a = int(input('Digite um número:'))

#laço dentro de laço de repetição
for x in range(a+1):
    div = 0
    for i in range(1, x+1):
        resto = x % i
        if resto == 0:
            div += 1
    if div == 2:
        print(end='{},'.format(i))
#x vai percorrer até o número digitado
#i vai percorrer um por um
#Exemplo: digito 3, vai percorrer 1,1,2,1,2,3
#pega o resto da divisão de cada vez que passar
#Se o resto foi == a zero
#Adiciona em div+1
#Se div for igual a 2
#dividido por 1 e por ele mesmo
#adiciono na lista de primos
