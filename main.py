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


def newProduct(name: str, price: int, data: str):
    return Product(name, price, data)


products = {
    "11111": newProduct('Яблоко', 50, "01.10.2022"),
    "22222": newProduct('Молоко', 63, "03.10.2022"),
    "33333": newProduct('Сыр', 120, "25.09.2022")
}

x = list(products.keys())

print(x)
