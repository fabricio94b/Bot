import json
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler
from config import TELEGRAM_TOKEN
from handlers import search_movie, start, unknown


bot = Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot, None, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), search_movie))
dispatcher.add_handler(MessageHandler(Filters.command, unknown))


def lambda_handler(event, context):
    dispatcher.process_update(Update.de_json(json.loads(event["body"]), bot))
    return {"statusCode": 200}
