#importar paquetes
import json
import requests

#Clases
from Client import Client
#from Order import Order
from Product import Product
from Restaurant import Restaurant
from Stadium import Stadium
from Team import Team
from Ticket import Ticket
from Match import Match

class App():
    def __init__(self):
        self.Lista_Client = []
        self.Lista_Match = []
        self.Lista_order = []
        self.Lista_Product = []
        self.Lista_Restaurant = []
        self.Lista_Stadium = []
        self.Lista_Team = []
        self.Lista_Ticket = []


    def run(self):
        self.API()

        opciones = ["Gestión de partidos y estadios", "Gestión de venta de entradas", "Gestión de asistencia a partidos", "Gestión de restaurantes", "Gestión de venta de restaurantes", "Indicadores de gestión (estadísticas)"]
        print("Bienvenido")
        
        while True:
            opcion = menu(opciones)

            if opcion == 0:
                self.modulo_1()
            elif opcion == 1:
                self.modulo_2()
            elif opcion == 2:
                self.modulo_3()
            elif opcion == 3:
                self.modulo_4()
            elif opcion == 4:
                self.modulo_5()
            elif opcion == 5:
                self.modulo_6()
            else:
                print("Hasta luego")
                break

    #Carga del apis en los objetos
    def API(self):
        self.API_Teams()
        self.API_Stadiums()
        self.API_Matches()

    #Carga del apis Teams en los objetos
    def API_Teams(self):
        api_teams = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json").json()
        
        for team in api_teams:
            new= Team(team["id"], team["code"], team["name"], team["group"])
            self.Lista_Team.append(new)
    #Carga del apis Stadiums en los objetos
    def API_Stadiums(self):
        api_stadiums = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json").json()

        #Recorrer Lista de estadios y guardar su informacion
        for stadium in api_stadiums:
            new_stadium = Stadium(stadium['id'], stadium['name'], stadium['city'], stadium['capacity'], stadium['restaurants'])
            
            #Recorrer Lista de restaurantes y guardar su informacion dentro de su estadio pertinente
            restaurants = []
            for restaurant in stadium['restaurants']:
                new_restaurant = Restaurant(restaurant['name'], restaurant['products'])


                #Recorrer Lista de productos y guardar su informacion dentro de su restaurantes pertinente
                products = []
                for product in restaurant['products']:
                    new_product = Product(product['name'], product['quantity'], product['price'], product['adicional'], product['stock'])
                    products.append(new_product)
                    self.Lista_Product.append(new_product)
                #Guardamos lista de productos dentro del restaurantes
                new_stadium.restaurants = restaurants



                restaurants.append(new_restaurant)
                self.Lista_Restaurant.append(new_restaurant)
            #Guardamos lista de restaurantes dentro del estadio
            new_stadium.restaurants = restaurants



            self.Lista_Stadium.append(new_stadium )
    #Carga del apis Stadiums en los objetos
    def API_Matches(self):
        api_matches = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json").json()

        for match in api_matches:
            new = Match(match["id"], match["number"], match["home"], match["away"], match["date"], match["group"], match["stadium_id"])

            for team in self.Lista_Team:
                if new.home["id"] == team.id:
                    new.home = team
                if new.away["id"] == team.id:
                    new.away = team

            for stadium in self.Lista_Stadium:
                if stadium.id == match["stadium_id"]:
                    new.stadium = stadium

            self.Lista_Match.append(new)

    #Gestión de partidos y estadios
    def modulo_1(self):
        opciones = ["Buscar todos los partidos de un país", "Buscar todos los partidos que se jugarán en un estadio específico", "Buscar todos los partidos que se jugarán en una fecha determinada"]
        opcion = menu(opciones)

        if opcion == 0:
            self.search_match_country()
        elif opcion == 1:
            self.search_match_stadiums()
        elif opcion == 2:
            self.search_match_date()

    def search_match_country(self):
        match_search =input("Ingresa el pais por el que desea buscar el partido: ").lower()
        find = False
        for match in self.Lista_Match:
            if match_search in match.name.lower():
                find = True
                print(match.show())
        
        if not find:
            print("No se encontraron resultados")
            
    def search_match_stadiums(self):
        match_search =input("Ingresa el stadium por el que desea buscar el partido: ").lower()
        find = False
        for match in self.Lista_Match:
            if match_search in match.stadium.lower():
                find = True
                print(match.show())
        
        if not find:
            print("No se encontraron resultados")
            
    def search_match_date(self):
        match_search =input("Ingresa la fecha por el que desea buscar el partido (Ej: 2024-06-14): ").lower()
        find = False
        for match in self.Lista_Match:
            if match_search == match.date.lower():
                find = True
                print(match.show())
        
        if not find:
            print("No se encontraron resultados")


    #Gestión de venta de entradas
    def modulo_2(self):
        cedula = input("Ingresa tu cedula (sin puntos): ")
        data_client = self.validate_dni(cedula)
        if data_client == False:
            name = input("Ingresa tu numero")
            age = input("Ingresa tu edad")

            data_client = Client(name, age, cedula)
            self.Lista_Client.append(data_client)
        
        for index, match in enumerate(self.Lista_Match):
            print(f"----------{index+1}----------")
        
        match_number = input("Ingrese el numero del partido que desea escoger: ")
        while not match_number.isnumer() or not int(match_number) in range(1, len(self.Lista_Match)+1):
            match_number = input("Ingrese el numero del partido que desea escoger: ")
        
        type_ticket = input("Ingrese el numero del tipo de entrada que desea: \n1. General \n2. VIP \n")
        while not type_ticket.isnumer() or not int(type_ticket) in range(1, 3):
            type_ticket = input("Ingrese el numero del tipo de entrada que desea: \n1. General \n2. VIP \n")

        match = self.Lista_Match[int(match_number)-1]
        match_capacity = match.capacity
        precio = 0 
        if type_ticket == "1":
            match_capacity = match_capacity[0]
            precio = 35
        else:
            match_capacity = match_capacity[1]
            precio = 75
        
        row = match_capacity//10

        seating = []
        for i in range(1, row+1):
            row_seating = []
            for j in range(1, 11):
                seat = f"{i}{j}"
                row_seating.append(seat)
            seating.append(row_seating)

        "||".join(seating)

        

    
    def validate_dni(self, cedula):
        for client in self.Client:
            if int(client.cedula) == int(cedula):
                return client
        
        return False

    #Gestión de asistencia a partidos
    def modulo_3(self):
        pass

    #Gestión de restaurantes
    def modulo_4(self):
        opciones = ["Buscar producto por nombre", "Buscar producto por tipo", "Buscar producto por rango"]
        opcion = menu(opciones)

        if opcion == 0:
            self.search_product_name()
        elif opcion == 1:
            self.search_product_type()
        elif opcion == 2:
            self.search_product_range()

    def search_product_name(self):
        product_search =input("Ingresa el nombre del producto que desea buscar: ").lower()
        find = False
        for product in self.Lista_Product:
            if product_search == product.name.lower():
                find = True
                print(product.show())
        
        if not find:
            print("No se encontraron resultados")

    def search_product_type(self):
        product_search =input("Ingresa el numero de la opcion que desee buscar: \n1. De Paquete \n2. De Plato \n3. Con Alcohol: \4. Sin Alcohol: ")
        find = True
        for product in self.Lista_Product:
            if product_search == "1" and product.adicional == "package":
                print(product.show())
            elif product_search == "1" and product.adicional == "plate":
                print(product.show())
            elif product_search == "1" and product.adicional == "alcoholic":
                print(product.show())
            elif product_search == "1" and product.adicional == "non-alcoholic":
                print(product.show())
            elif not product_search in "1234":
                find = False

        if find:
            print("Dato invalido")

    def search_product_range(self):
        product_search_min =input("Ingresa el numero minimo del precio: ")
        while not product_search_min.isnumeric():
            product_search_min =input("Ingresa el numero minimo del precio: ")
        
        product_search_max =input("Ingresa el numero maximo del pecio: ")
        while not product_search_max.isnumeric() and float(product_search_max) < float(product_search_min):
            product_search_max =input("Ingresa el numero maximo del precio: ")
        
        find = False
        for product in self.Lista_Product:
            if float(product_search_min) < product.price < float(product_search_max):
                find = True
                print(product.show())
        
        if not find:
            print("No hay resultados en este rango")

    #Gestión de venta de restaurantes
    def modulo_5(self):
        pass

    #Indicadores de gestión (estadísticas)
    def modulo_6(self):
        pass

    #Guardar informacion en Archivo.txt
    def txt(self):
        pass
