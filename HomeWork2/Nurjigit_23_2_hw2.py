class Balance:
    def __init__(self, name_file):
        self.name_file = f'{name_file}.txt'

    def current_balance(self, money):
        try:
            with open(self.name_file, "r+") as cm_file:
                current_balance = cm_file.read()
                if current_balance:
                    self.current_money = int(current_balance)
                    self.current_money += money
                    return self.current_money
                else:
                    cm_file.write('0')
        except FileNotFoundError:
            with open(self.name_file, "w+") as cm_file:
                cm_file.write('0')
                self.current_money = 0

    def write_balance(self, money):
        with open(self.name_file, mode="w+") as cm_file:
            cm_file.write(str(money))

    def collection(self):
        if self.current_balance(0) > 0:
            self.current_money = 0
            self.write_balance(0)
        else:
            print(f"Операция невозможна")

    def __str__(self):
        return f'На балансе {self.current_money}'


class Product:
    def __init__(self, name, price, packed_date):
        self.name = name
        self.price = price
        self.packed_date = packed_date


buys = list()

products = {
    '11111': Product("Яблоко", 50, '01.10.2022'),
    '22222': Product("Кефир", 60, '03.10.2022'),
    '45243': Product("Cыр", 100, '01.08.2022'),

}

while True:
    sh_code = input()
    balance = Balance('balance')

    if sh_code == "0":
        print("Смена окончена")
        print(buys)
        break
    elif sh_code == '1':
        balance.collection()
        print(f'Касса была аннулирована')
        break
    try:
        price = products[sh_code].price
        name = products[sh_code].name
        packed_date = products[sh_code].packed_date
        buys.append([name, price, packed_date])
        print(f"Вы купили {name} за {price} сом")

        balance.current_balance(price)
        balance.write_balance(balance.current_money)
        print(f"На кассе {balance.current_balance(0)} сом")

    except:
        print(f'Такого товара не имеется на складе')
