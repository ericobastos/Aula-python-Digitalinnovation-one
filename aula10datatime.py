#importação modolos
from datetime import date, time, datetime, timedelta

#Métedo com comandos datetime
def trabalhando_com_datetime():
    #now traz ano,mês,dia,hora,minutos,segundos,milisegundos
    data_atual = datetime.now()
    print(data_atual)
    #convertendo data e hora para string
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    #modelo de chamada
    print(data_atual.strftime('%c'))
    print(data_atual.day)#dia
    print(data_atual.month)#mes
    print(data_atual.minute)#minutos
    print(data_atual.hour)#hora
    print(data_atual.year)#ano
    print(data_atual.date())# data
    print(data_atual.weekday())#dia da semana
    #tupla de dias da semana
    tupla = ('Segunda', 'Terça', 'Quarta','Quinta', 'Sexta', 'Sabado', 'Domingo')
    #chamando a tupla e dia atual com valor da tupla
    print(tupla[data_atual.weekday()])
    #data criada
    data_criada = datetime(2018, 6, 20, 15,30,20)
    print(data_criada)
    #converte data em string
    print(data_criada.strftime('%c'))
    #data criada em string
    data_string = ('01-01-2018 12:20:22')
    #data convertida usando strftime
    data_convertida = datetime.strptime(data_string, '%d-%m-%Y %H:%M:%S')
    print(data_convertida)
    #retirando 1 ano, 2 horas, 15 minutos
    nova_data = data_convertida - timedelta(days=365, hours=2,minutes=15 )
    print(nova_data)

#Método data
def trabalhando_com_date():
    #Traz data atual modolo datetime
    data_atual = date.today()
    #converte em string
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual))
    print(data_atual)
    print(type(data_atual_str))
    print(data_atual_str)

def trabalhando_com_time():
    #adiciona hora
    horario = time(hour=15, minute=20, second=30)
    #tipo de hora
    print(type(horario))
    print(horario)
    #converte para string
    horaio_str = (horario.strftime('%H:%M:%S'))
    print(type(horaio_str))
    print(horaio_str)
#Chamando métodos
if __name__ == '__main__':
    trabalhando_com_date()
    #trabalhando_com_time()
    # trabalhando_com_datetime()