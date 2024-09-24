class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self) -> float:
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_name: str):
        self.products = [p for p in self.products if p.name != product_name]

    def get_product(self, product_name: str) -> Product:
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def total_inventory_value(self) -> float:
        return sum(product.total_value() for product in self.products)
