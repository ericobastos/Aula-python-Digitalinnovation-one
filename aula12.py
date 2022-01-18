#Se não tem pip install requests
#Importa modulo requests
import requests
#passa a url
def retorna_dados_cep(cep):
    reponse = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    #Retorna 200 é que esta certo
    print(reponse.status_code)
    #Retorna url passada em json (dict)
    print(reponse.json())
    #adiciona objetos do dict a dados_cep
    dados_cep = reponse.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return  dados_cep
#Método retorna objetos pokemon
def retorna_dados_pokemon(pokemon):
    #pega dados da url json
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    #traz em json
    dados_pokemon = response.json()
    #retorna os dados
    return dados_pokemon
#Busca dados pela url
def retorna_dados(url):
    #recebe a url
    response = requests.get(url)
    #retorna html da pagina
    return response.text

if __name__ == '__main__':
    #Passo o cep retorna informações
    # retorna_dados_cep('01001000')

    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon)
    # print(dados_pokemon['sprites'], 'front_shiny')
    # response = retorna_dados('https://web.dio.me/browse')
    # print(response)