class Product:
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        if self.quantity >= quantity:
            return True
        else:
            return False

    def buy(self, quantity=1):
        if self.check_quantity(quantity):
            self.quantity -= quantity
            print(f'Покупка {self.name} в количестве {str(quantity)}')
        else:
            raise ValueError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        if remove_count is None or remove_count > self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total = 0
        for i in self.products:
            total += self.products[i] * i.price
        return total

    def buy(self):
        products_to_remove = list(self.products.items())
        for product, quantity in products_to_remove:
            if product.check_quantity(quantity):
                product.buy(quantity)
                self.remove_product(product)
            else:
                raise ValueError('Товара не хватает на складе')