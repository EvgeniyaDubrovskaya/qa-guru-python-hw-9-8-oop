"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product
from homework.models import Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product2():
    return Product("pen", 1.15, "This is a pen", 10)


@pytest.fixture
def cart(product):
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        assert product.buy(1001) == ValueError


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_to_card(self, cart, product):
        cart.add_product(product)
        assert cart.products[product] == 1

    def test_increase_product_quantity(self, cart, product):
        cart.add_product(product, 1)
        cart.add_product(product, 2)
        assert cart.products[product] == 3

    def test_remove_product_from_card(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product)
        assert cart.products.get(product) is None

    def test_decrease_product_quantity(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 1)
        assert cart.products[product] == 2

    def test_clear_cart(self, cart, product):
        cart.add_product(product)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product, product2):
        cart.add_product(product, 2)
        cart.add_product(product2, 3)
        assert cart.get_total_price() == 203.45

    def test_buy(self, cart, product2):
        # to_do
        cart.add_product(product2, 3)
        cart.buy()
        assert product2.quantity == 7

    def test_buy_not_enough_product(self, cart, product, product2):
        cart.add_product(product, 1000)
        cart.add_product(product2, 10)
        product2.buy(1)
        assert cart.buy() == ValueError

