class City:
    def __init__(self, name, mayor, year):
        self.name = name
        self.mayor = mayor
        self.year = year
        self.buildings = list()

    def add_building(self, new_building):
        self.buildings.append(new_building)
    
    def list_buildings(self):
        for building in self.buildings:
            print(f"{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories") 