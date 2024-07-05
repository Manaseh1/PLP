#So what I have learnt is that you can invoke stuff using the __init__(self) kwa classes

class House:
    _number_of_rooms = 10 #Protected variable
    __space = [] # Private variable signified by double undersccore
    def __init__(self):
        rooms = ['bedroom','living room','dining room','toilet']
        description = 'House description'
        print(rooms,'\n',description)
myhouse = House()

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent

class PentHouse(House):
    justsuper = super(House)
    
myPentHouse = PentHouse()