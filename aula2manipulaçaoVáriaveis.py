# variveis (a,b) vão pedir ao usuário um número inteiro
a = int(input('Entre com primeiro valor: '))
b = int(input('Entre com segundo valor: '))

#fazendo operações com os números que usuário informou
soma = a + b
subtraçao = a - b
multiplicaçao = a * b
divisao = a / b
resto = a % b
potencia = a ** b
divisaoInteira = a // b

#Imprimindo operações com quebra de linha \n, formatação por parametro
print('Soma: {soma} \nSubtração: {subtraçao} \nMultiplicação: {multiplicaçao} '
      '\nDivisão: {divisao} \nResto da divisão: {resto} '
      '\nPotenciação: {potencia} \nDivisão inteira: {divisaoInteira}'
      .format(soma=soma,subtraçao=subtraçao,multiplicaçao=multiplicaçao,divisao=divisao,resto=resto,
                                                       potencia=potencia,divisaoInteira=divisaoInteira))