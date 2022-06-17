from telegram.ext import *
import response as r

import os

TOKEN = "5412632814:AAGwPC39OmMf0CfY6MjluroUO6dOv_xhI7c"


def start_command(update, context):
    yourname = update.message.from_user.first_name
    msg = "Hi " + yourname + "! Welcome to Rock app bot"
    context.bot.send_message(update.message.chat.id, msg)
    msg_2 = "Select your choice (rock/Paper/scissors)."
    context.bot.send_message(update.message.chat.id, msg_2)


def help_command(update, context):
    update.message.reply_text("Clear the history to start freshly.")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.rock_paper(text)
    update.message.reply_text(response)
    update.message.reply_text("Select your choice (rock/Paper/scissors).")
    print(response)


def quit_command(update, context):
    update.message.reply_text("Bye!! See you next time")


def error(update, context):
    print(f" Error caused by {update} in {context}.")


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("quit", quit_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_webhook(listen="0.0.0.0", port=os.environ.get("PORT", 443),
                          url_path=TOKEN,
                          webhook_url="https://rock-paper-01.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
