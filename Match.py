class Match():
    def __init__(self, id, number, home, away, date, group, stadium):
        self.id = id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium = stadium
        self.tickets_vip = []
        self.tickets_general = []
        self.attendance = 0

    def show(self):
        return f"""
            id: {self.id}
            number: {self.number}
            home: {self.home.name}
            away: {self.away.name}
            date: {self.date}
            group: {self.group}
            stadium: {self.stadium.name}"""
        