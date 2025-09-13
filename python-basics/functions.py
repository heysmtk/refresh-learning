# Functions - kromně již vestavěných funkcí jako třeba type(), můžeme vytváře vlastní
# Je to znovupoužitelný blok kódu, součást DRY konceptu

def greet(name):  # def - definice nové funkce
    """Vrátí pozdrav pro dané jméno"""  # docstring - popis toho co funkce dělá
    return f"Ahoj, {name}"  # return vrací to co funkce má vrátit

print(greet("Tom"))  # název funkce + ("value") zavolá funkci a provede akci