
# Handling Construtor while inheriting

class Dad:
    def __init__(self,car,flat):
        self.car = car
        self.flat = flat
    def display_dad(self):
        print(f"Flat : {self.flat}\nCar : {self.car}")

class Son(Dad):
    def __init__(self,phone,bike,car,flat):
        super().__init__(car,flat)
        self.phone = phone
        self.bike = bike
    def display_son(self):
        print(f"Phone : {self.phone}\nBike : {self.bike}")

son_obj = Son("Iphone",'Enfield','Audi','2BHK')
son_obj.display_son()
son_obj.display_dad()
    
        