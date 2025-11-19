import numpy               # Для математичних обчислень та роботи з масивами
import pandas              # Для роботи з таблицями (DataFrame)
import matplotlib.pyplot as plt  # Для побудови графіків і візуалізації даних
import requests            # Для виконання HTTP-запитів до сайтів або API
from PIL import Image      # Для роботи із зображеннями (відкриття, створення, збереження)
import pyjokes             # Для генерації програмістських жартів
import pyfiglet            # Для створення ASCII-арту з тексту
from termcolor import colored  # Для кольорового виводу тексту у консолі
from bs4 import BeautifulSoup  # Для парсингу HTML (аналіз коду сторінки)
import colorama            # Для кольорового форматування тексту в консолі


def main():
    try:
        arr = numpy.array([110, 230, 340, 480])
        print("Середнє значення (numpy):", numpy.mean(arr))
    except Exception as e:
        print("Помилка у numpy:", e)

    try:
        data = pandas.DataFrame({"Ім'я": ["Анна", "Богдан"], "Вік": [21, 30]})
        print("Таблиця з pandas:\n", data)
    except Exception as e:
        print("Помилка у pandas:", e)

    try:
        response = requests.get("https://api.github.com")
        print("Статус код відповіді (requests):", response.status_code)
    except Exception as e:
        print("Помилка у requests:", e)

    try:
        joke = pyjokes.get_joke()
        print("Жарт (pyjokes):", joke)
    except Exception as e:
        print("Помилка у pyjokes:", e)

    try:
        ascii_art = pyfiglet.figlet_format("Lab 5")
        print(colored(ascii_art, "cyan"))
    except Exception as e:
        print("Помилка у pyfiglet або termcolor:", e)


if __name__ == "__main__":
    main()
