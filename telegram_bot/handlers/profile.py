from telebot.types import Message
from keyboards.reply import genre_kb, mode_kb, difficulty_kb, main_menu
from states.user_states import UserStates

user_profiles = {}
user_state = {}

def register_profile_handlers(bot):

    #  ОБРОБНИК КНОПКИ "Назад"
    @bot.message_handler(func=lambda m: m.text == "⬅️ Назад")
    def go_back(msg: Message):
        uid = msg.from_user.id
        user_state.pop(uid, None)
        bot.send_message(msg.chat.id, "Повертаюся в меню!", reply_markup=main_menu())

    #  ПОКАЗАТИ ПРОФІЛЬ
    @bot.message_handler(func=lambda m: m.text == "👤 Мій профіль")
    def show_profile(msg: Message):
        uid = msg.from_user.id
        profile = user_profiles.get(uid)

        if not profile:
            bot.send_message(
                msg.chat.id,
                "У тебе ще немає профілю 📝\n"
                "Давай створимо його разом!\n\n"
                "Почнемо з головного — *який твій улюблений жанр ігор?* 🎮",
                parse_mode="Markdown",
                reply_markup=genre_kb()
            )
            user_state[uid] = UserStates.GENRE
        else:
            text = (
                "🎮 *Твій ігровий профіль:*\n"
                "Ось що я про тебе знаю:\n\n"
                f"• Улюблений жанр: *{profile.get('genre')}*\n"
                f"• Стиль гри: *{profile.get('mode')}*\n"
                f"• Бажана складність: *{profile.get('difficulty')}*\n\n"
                "Хочеш змінити? — просто скинь профіль!"
            )

            bot.send_message(msg.chat.id, text, parse_mode="Markdown")

    # 🔄 СКИНУТИ ПРОФІЛЬ
    @bot.message_handler(func=lambda m: m.text == "🔄 Скинути профіль")
    def reset_profile(msg: Message):
        uid = msg.from_user.id
        user_profiles.pop(uid, None)
        user_state.pop(uid, None)

        bot.send_message(
            msg.chat.id,
            "Готово! 🔄\n"
            "Твій профіль скинуто.\n"
            "Можемо створити новий, коли захочеш 😊",
            reply_markup=main_menu()
        )
    # ВИБІР ЖАНРУ
    @bot.message_handler(func=lambda m: user_state.get(m.from_user.id) == UserStates.GENRE)
    def choose_genre(msg: Message):
        uid = msg.from_user.id
        user_profiles.setdefault(uid, {})["genre"] = msg.text
        user_state[uid] = UserStates.MODE
        bot.send_message(
            msg.chat.id,
            "Чудово! 👍\n\n"
            "Тепер скажи мені: *як ти зазвичай граєш?* 🎮\n"
            "Соло чи з друзями?",
            parse_mode="Markdown",
            reply_markup=mode_kb()
        )
    #  ВИБІР РЕЖИМУ
    @bot.message_handler(func=lambda m: user_state.get(m.from_user.id) == UserStates.MODE)
    def choose_mode(msg: Message):
        uid = msg.from_user.id
        user_profiles[uid]["mode"] = msg.text
        user_state[uid] = UserStates.DIFFICULTY
        bot.send_message(
            msg.chat.id,
            "Добре! 🔥\n\n"
            "І останнє питання — *яку складність ігор ти надаєш перевагу?*\n"
            "Легку? Середню? Чи хочеш хардкору? 😈",
            parse_mode="Markdown",
            reply_markup=difficulty_kb()
        )

    # ️ ВИБІР СКЛАДНОСТІ
    @bot.message_handler(func=lambda m: user_state.get(m.from_user.id) == UserStates.DIFFICULTY)
    def choose_difficulty(msg: Message):
        uid = msg.from_user.id
        user_profiles[uid]["difficulty"] = msg.text
        user_state.pop(uid, None)

        bot.send_message(
            msg.chat.id,
            "Готово! ✔️\n\n"
            "Я запамʼятав твій стиль гри 😎\n"
            "Тепер можеш попросити мене підібрати гру через меню!",
            parse_mode="Markdown",
            reply_markup=main_menu()
        )

