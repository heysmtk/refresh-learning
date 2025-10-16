# Data
default_prices = "Adults: 250,- | Kids: 100,-"
default_hours = "9:00 - 18:00"

           
class Animal:
    def __init__(self, name, type, age, size, weight):
        self.name = name
        self.type = type
        self.age = age
        self.size = size
        self.weight = weight
        
    def __str__(self):
        return f"{self.name} ({self.type}), {self.age} let, {self.size:.2f}m, {self.weight:.1f}kg"
    
    def eat(self):
        self.weight += 0.5
        self.size += 0.03
        print(f"{self.name} se najedl a nabral na váze a velikosti!")
        
    def sleep(self):
        self.weight -= 0.4
        self.size -= 0.02        
        print(f"{self.name} se vyspinkal, během spánku něco zhubnul!")
        
    def about(self):
        print(f"{self.name} je typu: {self.type} a má {(self.age):.1f} rok/ů, je velký {(self.size):.2f}m a váží {(self.weight):.2f}kg !")
    
    def make_sound(self):
        print(f"{self.name} makes some noice!")
        

class Tiger(Animal):
    def make_sound(self):
        print(f"{self.name} is Rooaarrr!")
        
    
class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} is Tůůůůůtůůůů!")
        
        
class Zoo:
    def __init__(self, 
                 opening_hours=default_hours, 
                 pricing=default_prices):
        self.__opening_hours = opening_hours
        self.__pricing = pricing
        self.__animals_list = []
    
    def info(self):
        print(f"Otevírací doba: {self.__opening_hours} | Ceník: {self.__pricing}")
        
    def add_animal(self, animal):
        self.__animals_list.append(animal)
    
    def animals(self):
        print("Zvířata v ZOO:")
        for animal in self.__animals_list:
            print(f" - {animal}")

 
        
zoo_lesna = Zoo()
tiger = Tiger("Alex", "Tigr Usurijský", 4, 1.62, 182)

zoo_lesna.info()
tiger.about()
tiger.eat()
tiger.about()
tiger.sleep()
tiger.about()
tiger.make_sound()
zoo_lesna.add_animal(Animal("Ele", "Elephant", 6, 5.5, 550))
zoo_lesna.animals()