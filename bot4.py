import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
from my_handlers import greet_user, guess_number, planet, send_cat_picture, talk_to_me, user_coordinates, error_callback


def main():
    PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    logging.basicConfig(filename='bot.log', level=logging.INFO)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(CommandHandler('guess',guess_number))
    dp.add_handler(CommandHandler('planet',planet))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_error_handler(error_callback)

    logging.info("Bot has just started")
    mybot.start_polling()
    mybot.idle()



if __name__ == "__main__":
    main()