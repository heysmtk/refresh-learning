# Co to je dunder methods?
# - metody se dvěma podtržítky "__" např.: __str__m __len__, __eq__

# K čemu to je?
# Umožní mi aby se objekt choval jako zabudované typy (list, string atd...)

class Dog:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Dog named {self.name}"
    
dog = Dog("Easy")    

print(dog)


class Kennel:
    def __init__(self, dogs):
        self.dogs = dogs
    
    def __getitem__(self, index):
        return self.dogs[index]

kennel = Kennel(["Rex", "Micka"])
print(kennel[0])  # -> Rex


class Kennel:
    def __init__(self, dogs):
        self.dogs = dogs
    
    def __len__(self):
        return len(self.dogs)

kennel = Kennel(["Rex", "Micka"])
print(len(kennel))  # -> 2
