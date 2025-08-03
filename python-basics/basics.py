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
age = 18

if age >= 18:
    print("Můžeš řídit auto")
elif age >= 15:
    print("Můžeš jet na mopude")
else:
    print("Ještě musíš počkat")
    
a == b  # rovná se
a != b  # nerovná se
a > b   # větší než
a < b   # menší než
a >= b  # větší nebo rovno
a <= b  # menší nebo rovno

# logic operators
vek = 18
ma_ridicak = True

if vek >= 18 and ma_ridicak:
    print("Můžeš řídit!")

if vek <= 18 or not ma_ridicak:
    print("Nemůžeš řídit!")
    
# task for conditions and logic operations
age_task = 20

if age_task < 13:
    print("Jsi dítě")
elif age_task <= 19:
    print("Jsi teenager")
else:
    print("Jsi dospělý")
    
# loops (for, while)
# for loop (když víš kolikrát opakovat)

ovoce = ["jablko", "hruška", "banán"]

# projde celý seznam a postupně vypíše jednotlivé položky
for item in ovoce:
    print(f"Mam rád {item}")
    
# range (od-do)
for i in range(5):
    print(f"číslo: {i}")
    
for i in range(2, 8):
    print(f"číslo_2: {i}")
    
# s indexem i hodnotou
for i, item in enumerate(ovoce):
    print(f"{i+1}. {item}")
    
# while loop (dokud smyčka platí tak jede)
counter = 0
while counter < 5:
    print(f"Počítadlo: {counter}")
    counter += 1
    
# task loops
for i in range(1, 11):
    print(f"číslo: {i}")
    
# dictionaries
student = {
    "name": "Anno",
    "age": 22,
    "obor": "informatika"
}

jmeno = student["name"]
vek = student.get("vek", 0)     # 0 is default value

# změna/přidání
student["rocnik"] = 3
student["age"] = 23

# procházení
for key, value in student.items():
    print(f"{key}, {value}")