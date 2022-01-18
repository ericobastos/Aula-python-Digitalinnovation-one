import shutil
#Escreve e cria arquivo
def escrever_arquivo(texto):
    diretorio = ('C:/Users/7/PycharmProjects/Introduçao_basica_python/teste.txt')
    arquvio = open(diretorio, 'w')
    arquvio.write(texto)
    arquvio.close()

# Método para atualizar um arquivo
def atualizar_arquivio(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

# Método para ler um arquivo
def ler_arquivo(nome_arquvio):
    arquvio = open(nome_arquvio, 'r')
    texto = arquvio.read()
    print(texto)

# Método tirar media
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_nota = x.split(',')
        aluno = lista_nota.pop(0)
        media = lambda notas: sum([int(i) for i in lista_nota]) / 4
        lista_media.append({aluno: media(lista_nota)})
    return lista_media

# Método para copiar um arquivo
def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/7/PycharmProjects/Introduçao_basica_python')

# Método para mover o arquivo
def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '')

# lista = media_notas('notas.txt')
# print(lista)
# ler_arquivo('notas.txt', )
# copia_arquivo()
# escrever_arquivo('teste.txt')
# atualizar_arquivio('teste.txt', '\nTerceira linha')

