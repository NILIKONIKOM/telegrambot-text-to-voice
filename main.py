import telebot
import config
from telebot import types
from gtts import gTTS
import os


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def speeking_text(message):
    mytext = message.text
    language = 'en'  #You can change the language
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("message.mp3")
    audio = open('message.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎤 Translate text to audio")
    markup.add(item1)
    bot.send_message(message.chat.id, "Welcome, {0.first_name}!\n"
                                      "I - <b> {1.first_name} </b>\n"
                                      "I can:\n"
                                      "Translate text to audio".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def commands(message):
    if message.chat.type == 'private':
        if message.text == '🎤 Translate text to audio':
            bot.send_message(message.chat.id, 'Write the text to be translated into audio')
            bot.register_next_step_handler(message, callback=speeking_text)

bot.polling(none_stop=True)
