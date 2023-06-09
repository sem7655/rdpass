import random
import string

def generate_password(length):
    """
    Генерирует случайный пароль указанной длины из символов строки ASCII
    """
    # Создаем строку из всех символов ASCII
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Выбираем случайный символ из строки ASCII
    password = ''.join(random.choice(all_chars) for i in range(length))

    return password

# Генерируем случайный пароль длиной 8 символов
password = generate_password(10)

print("Случайный пароль: ", password)
