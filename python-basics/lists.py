# Seznamy - listy
# Ukládají více hodnot v pořadí, mohou mít různé datové typy
# Jsou mutabilní (měnitelné)

fruits = ["Jablko", "Banán"]  # Seznam ovoce, nese dva stringy
print(fruits)  # testovací print
fruits.append("Třešeň")  # přidá do seznamu "třešeň"
print(fruits)  # testovací print
fruits.remove("Banán")   # odstraní ze seznamu "banán"
print(fruits)  # testovací print
fruits[0] = "Hruška"     # změní hodnotu
print(fruits)  # testovací print

print("Seznam:")
for fruit in fruits:
    print(fruit)