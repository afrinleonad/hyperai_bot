import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

openai.api_key = "<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>"
bot = telegram.Bot(token="<5894205012:AAHXBxSMCGOMCS_tWpjUdcrrXwRqghyOneE>")

def chatgpt_response(update, context):
    user_input = update.message.text
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=user_input,
        max_tokens=2048
    )
    response_text = response["choices"][0]["text"]
    update.message.reply_text(response_text)

def start(update, context):
    update.message.reply_text("Hi! How can I help you today?")

def main():
    updater = Updater(token="<5894205012:AAHXBxSMCGOMCS_tWpjUdcrrXwRqghyOneE>", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, chatgpt_response))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
