from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def game_info_kb(game_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("❓ Чому саме ця гра?", callback_data=f"why_{game_id}"))
    kb.add(InlineKeyboardButton("🔁 Інша рекомендація", callback_data="again"))
    return kb