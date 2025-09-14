# List / Dict Comprehensions - je způsob krátkého zápisu kolekcí

# Místo klasického zápis
numbers = []
for i in range(0,5):
    numbers.append(i)   
print(numbers)

# To lze jednoduše a zkráceně pomocí list-comprehension
numbers_2 = [x for x in range(5)]
print(numbers_2)

# Další příklady
squares = [x**2 for x in range(5)]
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Dictionaries comprehension
dict_comp = {x: x**2 for x in range(3)}
print(dict_comp)

# Test
set_comp = {x % 3 for x in range(10)}
print(set_comp)

sude = [x for x in range(21) if x % 2 == 0]
print(sude)

setik = {x % 3 for x in range(16)}
print(setik)

dictik = {x: x**3 for x in range(5)}
print(dictik)