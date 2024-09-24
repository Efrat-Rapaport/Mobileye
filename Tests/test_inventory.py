import pytest

from Inventory.Inventory import Product


def test_add_product(setup_create_sample_inventory):
    product = Product("Tablet", 300, 2)
    setup_create_sample_inventory.add_product(product)
    assert setup_create_sample_inventory.get_product("Tablet") is not None


def test_remove_product(setup_create_sample_inventory):
    setup_create_sample_inventory.remove_product("Laptop")
    assert setup_create_sample_inventory.get_product("Laptop") is None


def test_total_inventory_value(setup_create_sample_inventory):
    assert setup_create_sample_inventory.total_inventory_value() == (1000 * 3 + 500 * 5)


@pytest.mark.parametrize("name, price, quantity", [
    ("GameBoy", 200, 3),
    ("PC", 4000, 5),
])
def test_add_product_parametrize(setup_create_sample_inventory, name, price, quantity):
    product = Product(name, price, quantity)
    setup_create_sample_inventory.add_product(product)
    assert setup_create_sample_inventory.get_product(name) is not None


@pytest.mark.skip(reason="Skipping this test because it's still not in development")
def test_add_product_price_negative():
    assert False


def test_get_non_existent_product(setup_create_sample_inventory):
    product = setup_create_sample_inventory.get_product("NonExistent")
    assert product is None


def test_get_existing_product(setup_create_sample_inventory):
    product = setup_create_sample_inventory.get_product("Phone")
    assert product.name == "Phone"
    assert product.price == 500
    assert product.quantity == 5


def test_total_inventory_value_after_remove(setup_create_sample_inventory):
    setup_create_sample_inventory.remove_product("Phone")
    assert setup_create_sample_inventory.total_inventory_value() == (1000 * 3)


def test_product_total_value():
    product = Product("Watch", 200, 5)
    assert product.total_value() == 1000
