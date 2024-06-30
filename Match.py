class Match():
    def __init__(self, id, number, home, away, date, group, stadium):
        self.id = id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium = stadium

    def show(self):
        return f"""
            id: {self.id}
            number: {self.number}
            home: {self.home}
            away: {self.away}
            date: {self.date}
            group: {self.group}
            stadium: {self.stadium}"""
        