# 🔹 Імпорт легких бібліотек (усі стандартні — не потрібно встановлювати!)
import math       # Для математичних обчислень
import random     # Для генерації випадкових чисел
import datetime   # Для роботи з датою і часом
import os         # Для роботи з файлами та директоріями
import sys        # Для інформації про систему
import statistics # Для підрахунків середнього, медіани тощо
import time       # Для роботи з часом і затримками
import json       # Для роботи з JSON-даними
import platform   # Для інформації про операційну систему
import string     # Для роботи з текстом і символами

# 🧩 1️⃣ Використання math
try:
    print("Корінь квадратний із 16:", math.sqrt(16))
except Exception as e:
    print("Помилка в math:", e)

# 🧩 2️⃣ Використання random
try:
    print("Випадкове число від 1 до 10:", random.randint(1, 10))
except Exception as e:
    print("Помилка в random:", e)

# 🧩 3️⃣ Використання datetime
try:
    print("Поточна дата і час:", datetime.datetime.now())
except Exception as e:
    print("Помилка в datetime:", e)

# 🧩 4️⃣ Використання os
try:
    print("Поточна директорія:", os.getcwd())
except Exception as e:
    print("Помилка в os:", e)

# 🧩 5️⃣ Використання statistics
try:
    numbers = [10, 20, 30, 40]
    print("Середнє значення:", statistics.mean(numbers))
except Exception as e:
    print("Помилка в statistics:", e)

print("Затримка 1 секунду...")
time.sleep(1)
print("Назва ОС:", platform.system())
print("Множина букв:", string.ascii_lowercase)
print("Версія Python:", sys.version)
print("JSON приклад:", json.dumps({"name": "Gleb", "age": 18}))
