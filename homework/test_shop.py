import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    cart = Cart()
    return cart


@pytest.fixture
def not_empty_cart(cart, product):
    cart.add_product(product)
    return cart


class TestProducts:

    def test_product_check_quantity(self, product):
        assert product.check_quantity(1000) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        exp_quantity = product.quantity - 1
        product.buy(1)
        assert product.quantity == exp_quantity

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            assert product.buy(1001)
            assert product.buy(99999)


class TestCart:

    def test_add_product_to_empty_cart(self, cart, product):
        cart.add_product(product)

        assert product in cart.products
        assert cart.products[product] == 1

    def test_add_product_to_not_empty_cart(self, cart, product):
        cart.add_product(product)
        cart.add_product(product, 2)

        assert product in cart.products
        assert cart.products[product] == 3

    def test_remove_product_if_count_is_none(self, not_empty_cart, product):
        not_empty_cart.remove_product(product)
        assert not_empty_cart.products == {}

    def test_remove_product_if_count_is_more(self, not_empty_cart, product):
        not_empty_cart.remove_product(product, 99)
        assert not_empty_cart.products == {}

    def test_remove_product_if_count_is_less(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 2)
        assert cart.products == {product: 8}

    def test_clear(self, not_empty_cart):
        not_empty_cart.clear()
        assert not_empty_cart.products == {}

    def test_get_total_price(self, cart, product):
        eat = Product('eat', 25, 'cool eat', 15)
        water = Product('water', 10, 'liquid', 20)
        coffee = Product('coffee', 5, 'energizing coffee', 100)

        cart.add_product(eat, 4)
        cart.add_product(water, 10)
        cart.add_product(coffee, 20)
        assert cart.get_total_price() == 300

    def test_buy_all_product_in_cart(self, cart, product):
        eat = Product('eat', 25, 'cool eat', 15)
        water = Product('water', 10, 'liquid', 20)
        coffee = Product('coffee', 5, 'energizing coffee', 100)

        cart.add_product(eat, 4)
        cart.add_product(water, 10)
        cart.add_product(coffee, 20)
        cart.buy()

        assert cart.products == {}
        assert eat.quantity == 11
        assert water.quantity == 10
        assert coffee.quantity == 80

    def test_buy_product_in_cart(self, cart, product):
        exp_quantity = product.quantity - 1
        product.buy()

        assert product.quantity == exp_quantity

    def test_buy_all_quantity_product_in_cart(self, cart, product):
        exp_quantity = product.quantity - 100
        product.buy(quantity=100)

        assert product.quantity == exp_quantity

    def test_buy_more_product_than_are_in_stock(self, cart, product):
        with pytest.raises(ValueError):
            assert product.buy(quantity=1003)
