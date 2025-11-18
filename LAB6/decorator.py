def round_result(digits):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Перевіряємо, чи результат числовий
            if isinstance(result, (int, float)):
                return round(result, digits)
            return result
        return wrapper
    return decorator
