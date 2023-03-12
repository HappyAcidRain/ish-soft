# для постоянной работы
import os
import sys
from requests.exceptions import ConnectionError, ReadTimeout

# прочее
import telebot

bot = telebot.TeleBot('6127536496:AAH09NmHcoUsKdLuzd0dFYoFwQxjFk6XBBI')

print("bot has been started!")


@bot.message_handler(commands=['SpamLove'])
def start(message):
    bot.send_message(message.chat.id, 'сколько?')

    @bot.message_handler(content_types=['text'])
    def spam(message):

        count = int(message.text)
        step = 0

        while step < count:
            bot.send_message(5613754332, 'Я люблю тебя!❤️')
            bot.send_message(message.chat.id, 'отправленно!!')
            print("msg has been sended!")
            step += 1

    bot.register_next_step_handler(message, spam)


@bot.message_handler(commands=['love'])
def start(message):
    bot.send_message(5613754332, 'Я люблю тебя!❤️')
    bot.send_message(message.chat.id, 'отправленно!!')
    print("msg has been sended!")


@bot.message_handler(commands=['status'])
def start(message):
    bot.send_message(message.chat.id, 'работаю!')
    print("bot is working!")


# для постоянной работы
try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except (ConnectionError, ReadTimeout) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
