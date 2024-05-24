import json

def ler_arquivo():
    #Abrindo o arquivo Credenciais e retornando o arquivo em forma de dicionario
    with open("credenciais.json", 'r') as arquivo_json:
        dados_json = json.load(arquivo_json)

    return dados_json