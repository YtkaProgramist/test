try:
    number = int(input("Введите число: "))

    if number >= 50:
        print("Хихи хаах больше 50!")
    else:
        print("О нет! Меньше 50!")
except ValueError:
    print("Я же сказал число!")


def get_pass():
    return 123
