from building import Building 
from city import City

# Create a new city instance and add your building instances to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.

gotham = City("Gotham", "Mayor Pete", "1985")
 

# Create 5 building instances

building_1 = Building("1500 S Wacker", 25)
building_2 = Building("Elysian Fields", 47)
building_3 = Building("Versailles", 20)
building_4 = Building("Brokedown Palace", 2)
building_5 = Building("shack", 1)
# Have each one get purchased by a real estate magnate
# After purchased, construct each one
# print(building_1.name)

building_1.purchase("some rich guy")
building_1.construct()
building_2.purchase("Rich Uncle Pennybags")
building_2.construct()
building_3.purchase("Warren Buffet") 
building_3.construct()
building_4.purchase("Patti Lapone")
building_4.construct()
building_5.purchase("Patti LaBelle")
building_5.construct()

# Create a new city instance and add your building instances to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.
# Awesome code here
gotham.add_building(building_1)
gotham.add_building(building_2)
gotham.add_building(building_3)
gotham.add_building(building_4)
gotham.add_building(building_5)
# print(gotham)
 
gotham.list_buildings()  
