
from mailing import Mailing  # Импортируем класс Mailing
from address import Address  # Импортируем класс Address

# Создаем адреса отправителя и получателя
address_from = Address(index="123456", city="Москва", street="Ленинградская", house="10", apartment="15")
address_to = Address(index="654321", city="Санкт-Петербург", street="Невская", house="5", apartment="22")

# Создаем почтовое отправление
mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=500,
    track="TRACK123456789"
)

# Распечатываем отправление в необходимом формате
print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house}-{mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house}-{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")

