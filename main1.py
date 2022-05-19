import telebot;

bot = telebot.TeleBot('5366002265:AAEynoO8D4Czkb9hA9wB4JriZABauzb2Hdo')

num1 = { "Спа" : "7028", 
         "Спорт" : "7024"
       }

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?')
    elif message.text == 'Спа':
        bot.send_message(message.from_user.id, 'Номер СПА', num1["Спа"])
    elif message.text == 'Спорт':
        bot.send_message(message.from_user.id, 'Номер Спорт-Центра-7024')
    elif message.text == 'Ресторан':
        bot.send_message(message.from_user.id, 'Номер Ресторана - я и сам не знаю')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')

bot.polling(none_stop=True, interval=0)