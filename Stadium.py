class Stadium():
    def __init__(self, id, name, city, capacity, restaurants):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = restaurants

    def show(self):
        return f"""
        id: {self.id}
        name: {self.name}
        city: {self.city}
        capacity: {self.capacity}
        restaurants: {self.restaurants}"""
    

