# __init__ (konstruktor) je specialní metoda, která se spustí při vytvoření objektu
# self = je odkaz na samotný objekt (bez toho byPython nevěděl, komu patří data)

# Proč to tak je?
# Potřebujeme nastavit defaultní hodnoty (atributy). Když vytvoříš psa, musíš mu dát jméno a věk..

class Dog:
    def __init__(self, name, age):
        self.name = name  # atribut name patřící konkrétnímu psovi
        self.age = age
        
dog1 = Dog("Easy", 12)
print(dog1.name, dog1.age)  # Easy 12