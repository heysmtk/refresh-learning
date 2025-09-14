# # enumerate() - dává index i hodnotu

# fruits = ["jablko", "hruška", "třešeň"]

# for i, fruit in enumerate(fruits):
#     print(i, fruit)


# # zip() - spojuje více kolekcí do sebe
# # výsledek je iterátor, lze použít list(zip(...))

# names = ["Tom", "Anna"]
# ages = [30, 1]

# for name, age in zip(names, ages):
#     print(name, age)
    
# # Cvičení
# abc = ["a", "b", "c"]
# for i, letter in enumerate(abc, start=1):
#     print(i, letter)
    
# cities = ["Brno", "Valmez"]
# for name, age, city in zip(names, ages, cities):
#     print(name, age, city)
    
# pairs = list(zip(names, ages))
# print(pairs)

# students = ["Alice", "Bob", "Charlie"]
# grades = [90, 85, 78]
# students_dict = {}

# for student, grade in zip(students, grades):
#     print(f"{student} má {grade} bodů")
#     students_dict[student] = grade

# print(students_dict)

# students = ["Alice", "Bob", "Charlie"]
# grades = [90, 85, 78]

# for i, (student, grade) in enumerate(zip(students, grades), 1):
#     print(f"{i}. {student} má {grade} bodů")
    
# names = ["Tom", "Anna", "Jake"]
# ages = [30, 1, 25]
# cities = ["Praha", "Brno", "Ostrava"]

# for i, (name, age, city) in enumerate(zip(names, ages, cities), start=1):
#     print(f"{i}. {name} ({age}) žije v {city}")

students = ["Alice", "Bob", "Charlie"]
grades = [90, 85, 78]

string_list = [f"{i}. {student} má {grade} bodů\n" for i, (student, grade) in enumerate(zip(students, grades), start=1)]
print(string_list)