import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызывается {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} завершен")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Приветствует пользователя."""
    print(f"Привет, {name}!")

@my_decorator
def calculate_sum(a, b):
    """Вычисляет сумму двух чисел."""
    return a + b

say_hello("Мир")
result = calculate_sum(5, 10)
print(result)