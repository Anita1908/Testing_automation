
from smartphone import Smartphone 

# Список смартфонов
catalog = [
    Smartphone(brand='Apple', model='iPhone 13 Pro Max', phone_number='+79991234567'),
    Smartphone(brand='Samsung', model='Galaxy S22 Ultra', phone_number='+79167654321'),
    Smartphone(brand='Xiaomi', model='Redmi Note 10', phone_number='+79265556677'),
    Smartphone(brand='Huawei', model='P40 Lite', phone_number='+79033334455'),
    Smartphone(brand='Google', model='Pixel 6a', phone_number='+79999876543')
]

# Цикл для вывода каталога телефонов
for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')