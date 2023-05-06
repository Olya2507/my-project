from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)

info = types.KeyboardButton("Информация")
stats = types.KeyboardButton("Статистика")
razrab = types.KeyboardButton("Разработчик")
lit = types.KeyboardButton("Python литература")
user_id = types.KeyboardButton("Покажи пользователя")
add_photo = types.KeyboardButton("Добавить фото")
show_photo = types.KeyboardButton("Показать фото из галереи")
start.add(stats, info)
start.add(lit, razrab)
start.add(add_photo, show_photo)
start.add(user_id)
