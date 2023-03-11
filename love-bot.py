import telegram
from telegram.ext import Updater, CommandHandler

# Задаем токен, полученный от @BotFather
bot_token = 'your_bot_token_here'

# Создаем объект бота
bot = telegram.Bot(token=bot_token)

# Функция для отправки сообщения всем подписчикам
def send_message_to_all_subscribers(bot, update):
    subscribers = bot.get_chat_members_count(chat_id=update.message.chat_id)
    message_text = "Привет всем! Это рассылка от бота."
    for subscriber in subscribers:
        bot.send_message(chat_id=subscriber.id, text=message_text)

# Создаем обработчик команды /send_all
send_all_handler = CommandHandler('send_all', send_message_to_all_subscribers)

# Создаем объект updater и регистрируем обработчик команды
updater = Updater(token=bot_token)
updater.dispatcher.add_handler(send_all_handler)

# Запускаем бота
updater.start_polling()
