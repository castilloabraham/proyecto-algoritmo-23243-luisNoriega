class Team():
    def __init__(self, id, code, name, group):
        self.id = id
        self.code = code
        self.name = name
        self.group = group

    def show(self):
        return f"""
            id: {self.id}
            code: {self.code}
            name: {self.name}
            group: {self.group}"""
