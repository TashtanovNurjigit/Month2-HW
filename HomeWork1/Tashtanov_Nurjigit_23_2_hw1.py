# ДЗ 1:
# Срок до 07.10.2022
# 1) Создайте класс Product с конструктором (init), принимающий название, цену и дату упаковки (name, price, packed_date)
# 2) Создайте метод для определения даты окончания срока годности (пример был на уроке)
# 3) Создайте 3 объекта с соответсвтующий параметрами
#
# Пример кода:
# # ...
# milk = Product("Молоко", 55, "05.08.2022")
# print(milk.price) # выводит 55
# print(milk.exp_date) # выводит 15.08.2022

class Product:
    def __init__(self, name, price, packed_date):
        self.name = name
        self.price = price
        self.packed_date = packed_date

    exp_date = None

    def show_exp_date(self, best_before_date: int):
        start_day = int(self.packed_date[:2])
        start_day += best_before_date
        exp_date = f"{start_day}{self.packed_date[2:]}"
        self.exp_date = exp_date
        print(f'Товар годен до {exp_date}')


def writeFile(current_money: str):
    with open("current_money.txt", "w", encoding='UTF-8') as file:
        file.write(current_money)


def readingFile():
    try:
        with open("current_money.txt", "r", encoding='UTF-8') as file:
            return file.readline()
    except:
        with open("current_money.txt", "w", encoding='UTF-8') as file:
            file.write('2350')


def newProduct(name: str, price: int, data: str):
    return Product(name, price, data)


products = {
    "11111": newProduct('Яблоко', 50, "01.10.2022"),
    "22222": newProduct('Молоко', 63, "03.10.2022"),
    "33333": newProduct('Сыр', 120, "25.09.2022")
}
while True:
    all_sh_code = list(products.keys())
    try:
        sh_code = input(f'Для пробития имеются следующие штрих коды: {all_sh_code}\n')
        buy = products[sh_code]
        print(f'Вы купили {buy.name}, за {buy.price}')
        current_money = int(readingFile())
        current_money += buy.price
        writeFile(str(current_money))
        print(f'На кассе {readingFile()} сомов')
    except:
        print(f'Такого товара не существует')
