# ********* In The Nmae Of God ***********
#  Student ID: 401130443
#  Student Name: Mohammad Saleh Sohrabi
#  Fundamental of Computers and Programming (python)
#  Hamedan University of Technology, Hamedan, Iran.

# ***************** Class Package *****************

class Simple_Package:       

    def __init__(self, numPackage, weight, destination, beginning):
        self.name = "Simple_Package"
        self.numPackage = numPackage
        self.weight = weight
        self.destination = destination
        self.beginning = beginning

class Breakable_package(Simple_Package):     
    def __init__(self, numPackage, weight, destination, beginning ):
        super().__init__( numPackage, weight, destination, beginning)
        self.name = "Breakable_package"

class Cold_Package(Simple_Package):
    def __init__(self, numPackage, weight, destination, beginning, min_temperature):
        super().__init__(numPackage, weight, destination, beginning)
        self.min_temperature = min_temperature
        self.name = "Cold_Package"

# ***************** Class Continer *****************
class Simple_Continer:
    def __init__(self, numContiner, weight, max_pack):
        self.numContiner = numContiner
        self.weight = weight
        self.max_pack = max_pack

class FreezerContainer(Simple_Continer):
    def __init__(self, numContiner, weight, max_pack, refrigerator_min_temperature ):
        super().__init__(numContiner, weight, max_pack)
        self.name = "FreezerContainer"
        self.refrigerator_min_temperature = refrigerator_min_temperature
        self.list_packs_FreezerContainer = []

class Breakable_Package_Container(Simple_Continer):
    def __init__(self, numContiner, weight, max_pack, max_speed):
        super().__init__(numContiner, weight, max_pack)
        self.name = "Breakable_Package_Container"
        self.max_speed = max_speed
        self.list_packs_Breakable_Package_Container = []

# ***************** Class Car *****************

class Simple_Car:
    def __init__(self, numCar, weight):
        self.numCar = numCar
        self.weight = weight

class CarRoom(Simple_Car):
    def __init__(self, numCar, weight, max_pack ):
        super().__init__(numCar, weight)
        self.name = "CarRoom"
        self.max_pack = max_pack
        self.list_packs_simple = []
    
class CarContiner(Simple_Car):
    def __init__(self, numCar, weight, max_Continer):
        super().__init__(numCar, weight)
        self.name = "CarContiner"
        self.max_Continer = max_Continer
        self.list_continers_car = []

# f = open("Users.txt", "a")
# username = "amir"
# f.write(username)
# f.close()

# f = open("Users.txt", "r")
# listusername = f.readlines()

