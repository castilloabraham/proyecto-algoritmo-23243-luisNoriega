class Client():
    def __init__(self, name, age, dni):
        self.name = name
        self.age = age
        self.dni = dni
        self.balance = 0
        self.type_tickets = None
        self.tickets = []

    def show(self):
        return f"""
            name: {self.name}
            age: {self.age}
            dni: {self.dni}
            balance: {self.balance}
            type_tickets: {self.type_tickets}
            tickets: {self.tickets}"""