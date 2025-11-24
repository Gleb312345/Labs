from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🎮 Підібрати гру")
    kb.add("👤 Мій профіль")
    kb.add("🔄 Скинути профіль")
    return kb


def genre_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("Action", "Horror")
    kb.row("RPG", "Co-op Fun")
    kb.row("Shooter", "Story")
    kb.row("Indie", "Survival")
    kb.row("Sandbox")

    return kb

def mode_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("Solo", "Co-op")
    return kb

def difficulty_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("Casual", "Balanced", "Challenge")
    return kb

def back_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("⬅️ Назад")
    return kb
