import pytest
from Inventory.Inventory import Inventory, Product


@pytest.fixture
def setup_create_sample_inventory():
    inventory = Inventory()
    product1 = Product("Laptop", 1000, 3)
    product2 = Product("Phone", 500, 5)
    inventory.add_product(product1)
    inventory.add_product(product2)
    return inventory
