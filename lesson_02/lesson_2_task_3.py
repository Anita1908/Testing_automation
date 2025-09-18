import math

# Шаг 1: определение функции для вычисления площади квадрата
def square(side):
    if not isinstance(side, int):
        side = float(side)  # преобразуем в вещественное число, если не целое
        area = math.ceil(side * side)  # Округляем вверх
    else:
        area = side * side  # Просто возводим квадрат целого числа
    
    return area

# Шаг 2: проверка функции
side_length = 5.7  # Пример стороны квадрата (нецелое число)
area_result = square(side_length)

# Шаг 3: вывод результата
print(f"Площадь квадрата со стороной {side_length} равна {area_result}.")