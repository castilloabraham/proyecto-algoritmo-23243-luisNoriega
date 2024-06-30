class Ticket():
    def __init__(self, id, dni, tipo_boleto, asiento, partido):
        self.id = id
        self.dni = dni
        self.tipo_boleto = tipo_boleto
        self.asiento = asiento
        self.partido = partido
        self.attendance = False

    def show(self):
        return f"""
            id: {self.id}
            dni: {self.dni}
            tipo_boleto: {self.tipo_boleto}
            asiento: {self.asiento}
            partido: {self.partido}"""