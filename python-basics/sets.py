# Sets - kolekce unikátních hodnot (duplicitní zmizí!)
# rychlé testování, zda hodnota existuje

my_set = {1, 2, 3, 3}  # jsou tam dvě číslice (3), n-tice jednu vymaže!
print(my_set)  # {1, 2, 3}

my_set.add(4)  # přidá číslo (4) do setu, podobně jako list.append()
print(my_set)
print(3 in my_set)  # True - číslo (3) je v tomto setu