class Restaurant():

    def __init__(self, name, products):
        self.name = name
        self.products = products

    def show(self):
        return f"""
            name: {self.name}
            products: {self.products}"""        
