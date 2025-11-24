from telebot.types import Message
from keyboards.reply import main_menu

def register_start_handlers(bot):

    @bot.message_handler(commands=['start'])
    def start(msg: Message):
        bot.send_message(
            msg.chat.id,
            "Привіт! Я GameGuide Bot 🎮\n\n"
            "Я можу підібрати гру спеціально під твій стиль.",
            reply_markup=main_menu()
        )