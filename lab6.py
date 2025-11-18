from decorator import round_result

# Використовуємо декоратор з параметром digits
@round_result(3)
def divide(a, b):
    return a / b

# Інша функція з іншим рівнем округлення
@round_result(1)
def multiply(a, b):
    return a * b

# Точка входу
if __name__ == "__main__":
    print("Результат ділення:", divide(10, 3))
    print("Результат множення:", multiply(5.678, 3.4))