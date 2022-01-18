#variavel recebe um dicionario
#seus objetos recebe funções
calculadora_lambda = {
    'soma': lambda a,b: a + b,
    'subtraçao': lambda a,b: a - b,
    'multiplicaçao': lambda a,b: a * b,
    'divisao': lambda  a,b: a / b,
    'potencia': lambda a,b: a ** b,
    'resto': lambda a,b: a % b,
}
#cada variavel recebe um objeto da lista
#e sua função
soma = calculadora_lambda['soma']
subtraçao = calculadora_lambda['subtraçao']
multiplicaçao = calculadora_lambda['multiplicaçao']
divisao = calculadora_lambda['divisao']
potencia = calculadora_lambda['potencia']
resto = calculadora_lambda['resto']

#chamando funções e passando valores e imprimindo
print('A soma é: {}'.format(soma(10,5)))
print('A subtração é: {}'.format(subtraçao(10,5)))
print('A multilicação é: {}'.format(multiplicaçao(10,5)))
print('A divisão é: {}'.format(divisao(10,5)))
print('A potência é: {}'.format(potencia(10,5)))
print('O resto da divisão é: {}'.format(resto(9,2)))

#Outra forma é essa
soma = lambda a,b: a + b

print(soma(10,5))
