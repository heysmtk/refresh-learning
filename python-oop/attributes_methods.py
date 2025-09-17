# atributy = jsou data uložená v objektu (např. name, age)
# metody = jsou funkce uložené v objektu (např. stekot())

# Proč to tak je?
# Spojuješ data a chování dohromady. Pes má vlastnosi jako (jméno a věk) a chování (štěká)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):  # metoda = funkce uvnitř třídy
        return f"{self.name} say woof!"  # pes štěká
    
dog1 = Dog("Rex", 10)
print(dog1.bark())