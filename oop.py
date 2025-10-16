# pak smazat

class Phone:
    def __init__(self, brand, model, battery):
        self.__brand = brand
        self.__model = model
        self.__battery = battery

    def call(self, number):
        if self.__battery >= 10:
            print(f"Phone {self.__brand}, {self.__model} calls number {number}!")
            self.__battery -= 10
        else:
            print(f"Low battery ({self.__battery}%), please charge!")
            
    def info(self):
        print(f"{self.__brand} - {self.__model} has {self.__battery}% battery!")
    
    def charge(self):
        self.__battery = 100
        print(f"{self.__model} battery is full - {self.__battery}%!")
        
    def set_battery(self, value):
        self.__battery = value
        
    def get_battery(self):
        print(f"Battery is {self.__battery} %")
        return self.__battery
    
    @property
    def brand(self):
        print(f"Phone brand is {self.__brand}")
        return self.__brand
    
    @brand.setter
    def brand(self, name):
        if not name:
            print("Brand name cannot be empty!")
        else:
            self.__brand = name
            print(f"Phone brand was set to: {self.__brand}!")
            
    @property
    def model(self):
        print(f"Your phone model is {self.__model}")
        return self.__model
    
    @model.setter
    def model(self, name):
        if not name:
            print("Model name cannot be empty!")
        else:
            self.__model = name
            print(f"Model was set to: {self.__model}")

class SmartPhone(Phone):
    def __init__(self, brand, model, battery, camera, size, color):
        super().__init__(brand, model, battery)
        self.camera = camera
        self.size = size
        self.color = color

    def take_photo(self):
        print(f"{self.model} has taken a photo by {self.camera} camera!")
        
    def info(self):
        print(f"{self.brand} {self.model} - Battery: {self.battery}% | Camera: {self.camera} | Size: {self.size} | Color: {self.color}")
    

nokia = Phone("Nokia","3310", 40)
#nokia.call("34")
nokia.info()
#nokia.charge()
nokia.info()
nokia.set_battery(10)
nokia.get_battery()
nokia.brand
nokia.brand = "Samsung"
nokia.brand
nokia.model
nokia.model = "5110"
nokia.model


# iphone = SmartPhone("Apple", "iPhone", 45, "Zeis 100MPx", "128GB", "Silver")
# iphone.info()
# iphone.charge()
# iphone.take_photo()
# iphone.info()


class Animal:
    def __init__(self, type):
        self.type = type
        
    def make_sound(self):
        print(f"{self.type} makes some noice!")
        

class Dog(Animal):
    def __init__(self, type):
        super().__init__(type)
        
    def make_sound(self):
        print(f"{self.type} is haf, haf!")
        
class Cat(Animal):
    def __init__(self, type):
        super().__init__(type)
        
    def make_sound(self):
        print(f"{self.type} is meow, meow!")
        
animal = Animal("Animal")
dog = Dog("Rex")
cat = Cat("Elizabeth")

for animal in (animal, dog, cat):
    animal.make_sound()