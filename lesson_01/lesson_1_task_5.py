# Функция, принимающая аргумент и выводящая его на экран
def print_number(num):
    print(num)

# Цикл, повторяющий вызов функции 11 раз
for _ in range(11):
    print_number(88005553535)


    # Функция, принимающая одну цифру и выводящая её на экран
def print_digit(digit):
    print(digit)

# Телефонный номер
number = '88005553535'

# Проходим по каждой цифре номера и передаем её в функцию
for digit in number:
    print_digit(digit)