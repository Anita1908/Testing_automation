
from user import User 

# Создаем объект класса User
my_user = User(first_name="Иван", last_name="Иванов")

# Вызываем методы объекта
my_user.print_first_name()     # Выведет: Иван
my_user.print_last_name()      # Выведет: Иванов
my_user.print_full_name()      # Выведет: Иван Иванов

