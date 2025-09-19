# Různé objekty můžou mít metodu se stejným jménem, ale každý ji provádí jinak!

# Proč?
# Umožní ti psát univerzální kód. Neřeší, jestli je to kočka nebo pes, prostě zavoláš speak()!

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


animals = [Dog("Rey", "Wolf"), Animal("Animal")]
for a in animals:
    print(a.speak())