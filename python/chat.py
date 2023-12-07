import dotenv
import os
import openai

#Efetivamente carrega os valores do arquivo
dotenv.load_dotenv(dotenv.find_dotenv())

api_key = os.getenv("API_KEY")

openai.api_key = api_key

def enviar_mensagem(mensagem, lista_mensagem=[]):
    lista_mensagem.append(
        {"role": "user", "content": mensagem}
    )

    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagem
    )

    return resposta["choices"][0]["message"]

lista_mensagem = []
while True:
    texto = input("Escreva aqui sua mensagem: ")

    if texto == "sair" or texto == "Sair" or texto == "SAIR":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagem)
        lista_mensagem.append(resposta)
        print("\n----------------------------------------------------------------------\n")
        print("Zappin: ", resposta["content"])
        print("\n----------------------------------------------------------------------\n")


