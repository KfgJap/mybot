import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.environ.get('BOT_TOKEN')
WEBAPP_URL = "https://192.168.1.70/admin"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    web_app = WebAppInfo(url=WEBAPP_URL)
    markup.add(InlineKeyboardButton("Открыть панель", web_app=web_app))
    bot.send_message(message.chat.id, "Твоя панель управления:", reply_markup=markup)

print("Бот запущен...")
bot.infinity_polling()
