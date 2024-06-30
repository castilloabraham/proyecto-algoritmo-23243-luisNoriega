class Product():
    def __init__(self, name, quantity, price, adicional, stock):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.adicional = adicional
        self.stock = stock

    def show(self):
        return f"""
            name = {self.name}
            quantity = {self.quantity}
            price = {self.price}
            adicional = {self.adicional}
            stock = {self.stock}
            """