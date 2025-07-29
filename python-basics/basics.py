# printing
print("Hello, World!")

# variables
name = "Tomáš"
age = 30
favorite_food = "kebab"
print(f"My name is {name} and I am {age} years old and my favorite food is {favorite_food}.")

# data types
integer_number = 42  # celé číslo
float_number = 3.14  # desetinné číslo

# basic operations with numbers
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

exc = 15 * 7
print("Výsledek je", exc)

# strings
pozdrav = "Ahoj"
zprava = "Jak se máš?"
dlouhy_text = """Toto je
víceřádkový
text"""

# work with text
name = "Tom"
print(len(name))
print(name.upper())
print(name.lower())
print("om" in name)  # True

# concentation text
first_name = "Tomáš"
last_name = "Smutek"
full_name = first_name + " " + last_name
print(full_name)
print(f"{first_name} {last_name}")

# boolean 
me_student = False
have_car = True

# comparsion
age = 30
adult = age >= 18   # True
senior = age >= 65  # False

# task bool, comparsion
my_age_comp = 30 >= 16  # True
print(my_age_comp)

# lists
fruits = ["apple", "banana", "peach"]
first_fruit = fruits[0]
last_fruit = fruits[-1]
fruits.append("orange")
fruits.insert(1, "kiwi")
print(fruits)
fruits.remove("peach")
last_fruit = fruits.pop()
print(fruits)
length_list = len(fruits)
is_there = "banana" in fruits
print(length_list, is_there)

# task - lists
my_fav_movies = ["Oppenheimer", "Interstellar", "Equallizer"]
my_fav_movies.append("Superman")
print(my_fav_movies)

# conditions
