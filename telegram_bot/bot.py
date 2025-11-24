import telebot
from config import TOKEN

from handlers.start import register_start_handlers
from handlers.profile import register_profile_handlers
from handlers.recommendations import register_recommendation_handlers
from handlers.callbacks import register_callback_handlers

bot = telebot.TeleBot(TOKEN)

# реєстрація хендлерів
register_start_handlers(bot)
register_profile_handlers(bot)
register_recommendation_handlers(bot)
register_callback_handlers(bot)

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()