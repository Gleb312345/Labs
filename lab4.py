products = {
    "хліб": 25.50,
    "молоко": 38.00,
    "вино": 150.00,
    "сир": 50.00
}

def format_price(price):
    return f"ціна: {price:.2f} грн"

def check_availability(*items):
    available = {}
    for item in items:
        if item in products:
            available[item] = True
        else:
            available[item] = False
    return available

def make_order():
    cart = input("Введіть товари через кому: ").split(",")
    cart = [item.strip().lower() for item in cart]

    availability = check_availability(*cart)

    if not all(availability.values()):
        print("Не всі товари є в наявності:")
        for item, is_available in availability.items():
            if not is_available:
                print(f" - {item} немає в магазині")
        return

    total = sum(products[item] for item in cart)
    print(f"Усі товари є в наявності. Загальна {format_price(total)}")

    action = input("Введіть 'купити' або 'переглянути ціну': ").lower()
    if action == "купити":
        print("Дякуємо за покупку!")
    elif action == "переглянути ціну":
        for item in cart:
            print(f"{item}: {format_price(products[item])}")
    else:
        print("Невідома команда.")

if __name__ == "__main__":
    make_order()