import telebot
import _sqlite3
from telebot import types

bot = telebot.TeleBot('5626925606:AAGYU4B_jjdZw435CGAl4wpsgY3mDHFp2ok')

@bot.message_handler(commands=['start', 'main', 'Hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')




@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Удалить фото", callback_data='delete')
    markup.row(btn1)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)





bot.polling(none_stop=True)