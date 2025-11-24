from telebot.types import CallbackQuery
from handlers.profile import user_profiles
from keyboards.inline import game_info_kb
from handlers.recommendations_data import GAMES
from handlers.memory import shown_games
import random


def register_callback_handlers(bot):

    @bot.callback_query_handler(func=lambda c: c.data.startswith("why_"))
    def explain(cb: CallbackQuery):
        game_id = cb.data.split("_", 1)[1]

        for g in GAMES:
            if g["id"] == game_id:
                bot.answer_callback_query(
                    cb.id,
                    show_alert=True,
                    text=g["reason"]
                )
                return

        bot.answer_callback_query(cb.id, text="Інформацію не знайдено.")

    @bot.callback_query_handler(func=lambda c: c.data == "again")
    def again(cb: CallbackQuery):
        uid = cb.from_user.id
        profile = user_profiles.get(uid)

        if not profile:
            bot.answer_callback_query(cb.id)
            bot.send_message(cb.message.chat.id, "Спочатку створи профіль через 👤 Мій профіль.")
            return

        suitable_games = [
            g for g in GAMES
            if g["genre"] == profile["genre"]
            and g["mode"] == profile["mode"]
            and g["difficulty"] == profile["difficulty"]
        ]

        if uid not in shown_games:
            shown_games[uid] = []

        remaining = [
            g for g in suitable_games
            if g["id"] not in shown_games[uid]
        ]

        if not remaining:
            bot.answer_callback_query(cb.id)
            bot.send_message(
                cb.message.chat.id,
                "Це всі ігри, які я можу тобі порадити ❤️\n"
                "Можеш змінити жанр, режим або складність, щоб отримати нові рекомендації!"
            )
            return

        game = random.choice(remaining)
        shown_games[uid].append(game["id"])

        bot.answer_callback_query(cb.id)
        bot.send_message(
            cb.message.chat.id,
            f"Ось ще одна гра для тебе 🎮\n*{game['name']}*",
            parse_mode="Markdown",
            reply_markup=game_info_kb(game["id"])
        )
