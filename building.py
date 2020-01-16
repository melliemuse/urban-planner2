import datetime

# Constructor
# Define your __init__ method to accept two arguments

# address
# stories
# Once defined this way, you can send those values as parameters when you create each instance
 
class Building: 
    def __init__(self, address, stories):
        self.designer = "name"
        self.owner = "owner"
        self.date_constructed = "time" 
        self.address = address
        self.stories = stories  

    # Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    # Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.
    
    def purchase(self, purchaser):
        self.owner = purchaser



#  eight_hundred_eighth = Building("800 8th Street", 12)

# Creating Your Buildings
# Create 5 building instances

building_1 = Building("1500 S Wacker", 25)
building_1.designer = "Frank Lloyd Wright"
building_2 = Building("Elysian Fields", 47)
building_2.designer = "Frank Lloyd Wright"
building_3 = Building("Versailles", 20)
building_3.designer = "Frank Lloyd Wright"
building_4 = Building("Brokedown Palace", 2)
building_4.designer = "Frank Lloyd Wright"
building_5 = Building("shack", 1)
building_5.designer = "Frank Lloyd Wright"
# Have each one get purchased by a real estate magnate
# After purchased, construct each one

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
# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# print(f"{building_1.address} was purchased by {building_1.owner} on {building_1.date_constructed} and has {building_1.stories} stories")
# print(f"{building_2.address} was purchased by {building_2.owner} on {building_2.date_constructed} and has {building_2.stories} stories")
# print(f"{building_3.address} was purchased by {building_3.owner} on {building_3.date_constructed} and has {building_3.stories} stories")
# print(f"{building_4.address} was purchased by {building_4.owner} on {building_4.date_constructed} and has {building_4.stories} stories")
# print(f"{building_5.address} was purchased by {building_5.owner} on {building_5.date_constructed} and has {building_5.stories} stories")

# Example
# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.