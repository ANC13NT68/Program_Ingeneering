def add_two_and_number():
    try:
        user_input = input("Введите число: ")
        result = 2 + float(user_input)
        print(f"Результат сложения: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


if __name__ == '__main__':
    add_two_and_number()
    add_two_and_number()
    add_two_and_number()
    add_two_and_number()