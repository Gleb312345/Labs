import random
from handlers.profile import user_profiles
from keyboards.inline import game_info_kb
from handlers.memory import shown_games
from handlers.recommendations_data import GAMES


def register_recommendation_handlers(bot):

    @bot.message_handler(func=lambda m: m.text == "🎮 Підібрати гру")
    def recommend_game(msg):
        uid = msg.from_user.id
        profile = user_profiles.get(uid)

        if not profile:
            bot.send_message(
                msg.chat.id,
                "Спочатку створи профіль через 👤 Мій профіль 😊"
            )
            return

        matches = [
            g for g in GAMES
            if g["genre"] == profile["genre"]
            and g["mode"] == profile["mode"]
            and g["difficulty"] == profile["difficulty"]
        ]

        if not matches:
            bot.send_message(
                msg.chat.id,
                "Поки що у мене немає підходящих ігор під цю комбінацію 😢"
            )
            return

        game = random.choice(matches)

        if uid not in shown_games:
            shown_games[uid] = []

        if game["id"] not in shown_games[uid]:
            shown_games[uid].append(game["id"])

        bot.send_message(
            msg.chat.id,
            f"Я підібрав гру для тебе 🎮\n\n*{game['name']}*",
            parse_mode="Markdown",
            reply_markup=game_info_kb(game["id"])
        )
