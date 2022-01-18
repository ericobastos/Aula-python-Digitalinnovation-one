
a = 10 # Variavel (a) esta recebendo valor 10
b = 5  # Variavel (b) esta rcebendo valor 5

# Potência de (a) por (b)
potencia = a ** b

# Multiplicação de (a) por (b)
multiplicaçao = a * b

# Divisão de (a) por (b)
divisao = a / b

# Divisão inteira de (a) por (b)
divisaoInteira = a // b

# Adição de (a) por (b)
adiçao = a + b

# Subtração de (a) por (b)
subtraçao = a - b

# Resto de uma divisão de (a) por (b)
resto = a % b

#Resultados das operações formatada
print('Potencia de {}**{} = {}'.format(a,b,potencia))
print('Multiplicação de {}*{} = {}'.format(a,b,multiplicaçao))
print('Divisão de {}/{} = {}'.format(a,b,divisao))
print('Divisão inteira de {}//{} = {}'.format(a,b,divisaoInteira))
print('Adição de {}+{} = {}'.format(a,b,adiçao))
print('Subtração de {}-{} = {}'.format(a,b,subtraçao))
print('Resto de {}%{} = {}'.format(a,b,resto))

# Multiplicando por 50 (-)
print('-'*50)

# Operações formata por quebra de linha \n
print('potencia {}\nMultiplicação {}\nDivisão {}\nDivisãoInteira {}\nAdição {}\nSubtração {}\nResto {}'
      .format(potencia,multiplicaçao,divisao,divisaoInteira,adiçao,subtraçao,resto))