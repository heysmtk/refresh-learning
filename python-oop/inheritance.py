# Třída může "zdědit" vlastnosti a metody jiné třídy

# Proč?
# Neopakuju kód - DRY!
# Například všichni "Animal" mají metodu speak(), ale každý druh si ji může přepsat

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"
    
class Dog(Animal):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
    
dog = Dog("Rex", "Wolf")
cat = Cat("Garfield")

print(dog.name, dog.type, dog.speak())
print(cat.name, cat.speak())