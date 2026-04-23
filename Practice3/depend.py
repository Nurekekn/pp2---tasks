
class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"name: {self.name}, price: {self.price}, quantity: {self.quantity}"

    def total_product(self):
        return self.price * self.quantity


class DigitalProduct(Product):
    def __init__(self, name, price, filesize, quantity=1):
        super().__init__(name, price, quantity)
        self.filesize = filesize

    def info(self):
        return f"{super().info()}, filesize: {self.filesize}MB"

   
    def total_product(self):
        return super().total_product() * 0.9


class PhysicalProduct(Product):
    def __init__(self, name, price, weight, quantity=1):
        super().__init__(name, price, quantity)
        self.weight = weight

    def info(self):
        return f"{super().info()}, weight: {self.weight}g"

   
    def total_product(self):
        shipping = 500
        return super().total_product() + shipping



p = Product("phone", 2540, 2)
digital = DigitalProduct("videogame", 4939, 348, 1)
physical = PhysicalProduct("milk", 1250, 1000, 3)

print(p.info(), "TOTAL:", p.total_product())
print(digital.info(), "TOTAL:", digital.total_product())
print(physical.info(), "TOTAL:", physical.total_product())