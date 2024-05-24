from Navegacao import Navegacao
from ler_arquivo_json import ler_arquivo as LA

#Cria o objeto da navegação passando como parametro os atributos quebrados do dicinario retornado da classe ler_arquivo_json
#e em seguida chama a função que abre o navegador
navegar = Navegacao(LA().get('url'), LA().get('login'), LA().get('senha'))
navegar.abrir_navegador()