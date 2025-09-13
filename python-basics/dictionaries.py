# Slovníky = dict, dictionaries, větší a přehlednější kolekce dat
# Klíč - Hodnota
# Klíče musí být uníkatní

person = {
    "name": "Tomáš",
    "age": 30
}

person["job"] = "Programátor"  # takhle přidáš key + value do dict

for key, value in person.items():
    print(key, value)