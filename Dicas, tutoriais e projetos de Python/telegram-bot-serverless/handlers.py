import requests
from config import OMDB_URL


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Tudo certo! Bot funcionando!"
    )


def search_movie(update, context):
    params = {"t": update.message.text, "plot": "full"}
    request = requests.get(OMDB_URL, params=params)
    response = request.json()

    if response["Response"] == "True":
        text = (
            f"Filme: {response['Title']}\n"
            f"Data de lançamento: {response['Released']}\n"
            f"Diretor(es): {response['Director']}\n"
            f"Escritor(es): {response['Writer']}\n"
            f"Atores: {response['Actors']}.\n"
            f"Enredo: {response['Plot']}\n"
            f"Gênero: {response['Genre']}\n"
            f"Link para o pôster do filme: {response['Poster']}\n"
        )
    else:
        text = "Não encontrei esse filme!"

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text,
    )


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Não sei o que fazer com esse comando.",
    )

