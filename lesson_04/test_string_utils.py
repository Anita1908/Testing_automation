import pytest
from string_utils import StringUtils

# Положительные случаи
def test_capitalize_positive_case():
    utils = StringUtils()
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("python") == "Python"
    assert utils.capitalize("") == ""

# Негативные случаи
def test_capitalize_negative_case():
    utils = StringUtils()
    assert utils.capitalize(None) == None  # Некорректный ввод (None)
    assert utils.capitalize(123) == "123"  # Передача числа вместо строки
    assert utils.capitalize([1, 2]) == "[1, 2]"  # Неправильный тип данных (список)

# Положительные случаи
def test_trim_positive_case():
    utils = StringUtils()
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("\tskypro") == "\tskypro"  # Табуляция не считается пробелом
    assert utils.trim("no_spaces_here") == "no_spaces_here"

# Негативные случаи
def test_trim_negative_case():
    utils = StringUtils()
    assert utils.trim(None) == ""  # Некорректный ввод (None)
    assert utils.trim([]) == ""  # Недопустимый тип данных (список)
    assert utils.trim("    ") == ""  # Строка, состоящая только из пробелов

# Положительные случаи
def test_contains_positive_case():
    utils = StringUtils()
    assert utils.contains("SkyPro", "S") == True
    assert utils.contains("SkyPro", "k") == True
    assert utils.contains("", "") == True  # Пустой символ содержится в пустой строке

# Негативные случаи
def test_contains_negative_case():
    utils = StringUtils()
    assert utils.contains("SkyPro", "U") == False
    assert utils.contains("SkyPro", "Pro") == False  # Поиск целого слова, а не отдельного символа
    assert utils.contains("", "a") == False  # Отсутствие символа в пустой строке

# Положительные случаи
def test_delete_symbol_positive_case():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("Python", "on") == "Pyth"

# Негативные случаи
def test_delete_symbol_negative_case():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"  # Символ отсутствует в строке
    assert utils.delete_symbol("", "a") == ""  # Удаляем символ из пустой строки
    assert utils.delete_symbol("SkyPro", None) == "SkyPro"  # Некорректный ввод (None)

    