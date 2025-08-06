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
    
# task - dicts
my_dict = {
    "jmeno": "Tomáš",
    "vek": 29,
    "hobby": "calisthenics"
}

print(f"Moje jméno je {my_dict['jmeno']}, mám {my_dict['vek']} let a můj koníček je hlavně {my_dict['hobby']}")

# functions
def pozdrav():
    print("Ahoj tohle je print z funkce - pozdrav()!")
    
# volání funkce
pozdrav()

# functions with parameters
def pozdrav_jmeno(jmeno):
    print(f"Ahoj {jmeno}!") 
    
pozdrav_jmeno("Kačenka") 

def secti(a, b): 
    result = a + b
    print(f"{a} + {b} = {result}")
    
secti(5, 3)

# functions with returned value
def secti_a_vrat(a, b):
    return a + b

def je_sude(cislo):
    return cislo % 2 == 0

# usecase
vysledek = secti_a_vrat(10, 5)
print(vysledek)
if je_sude(8):
    print("8 je sudé číslo")
    
# default paramater values
def predstav_se(jmeno, vek=18, mesto="Praha"):
    print(f"Jmenuji se {jmeno}, je mi {vek} let a jsem z {mesto}")
    
# some calls
predstav_se("Anna")     # uses default age and city
predstav_se("Karel", 25)    # uses default city
predstav_se("Petra", 30, "Brno")    # all parameters has been set
predstav_se("Tom", mesto="Ostrava")

# task for functions
def obvod_obdelnika(sirka, vyska):
    return (2 * sirka) + (2 * vyska)

print(obvod_obdelnika(23, 45))

# error handling - try/except
# try:
#     cislo = int(input("Zadej číslo: "))
#     vysledek = 10 / cislo
#     print(f"Výsledek: {vysledek}")
# except ValueError:
#     print("Tohle není platné číslo!")
# except ZeroDivisionError:
#     print("Nelze dělit nulou!")
    
# zachycení více chyb
# try:
#     soubor = open("neexistujici_soubor.txt", "r")
#     obsah = soubor.read()
# except (FileNotFoundError, PermissionError) as e:
#     print(f"Problém se souborem: {e}")
    
# try-except-else-finally
def bezpecne_deleni(a, b):
    try:
        vysledek = a / b
    except ZeroDivisionError:
        print("Chyba: Dělení nulou!")
        return None
    except TypeError:
        print("Chyba: Neplatné typy dat!")
        return None
    else:
        print("Dělení proběhlo úspěšně!")
        return vysledek
    finally:
        print("Tato zpráva se zobrazí vždy!")
        
print(bezpecne_deleni(10, 2))
print(bezpecne_deleni(10, 0))
print(bezpecne_deleni("a", 2))

# vlastní vyjímky
class TooOld(Exception):
    pass

def zkontroluj_vek(vek):
    if vek < 0:
        raise ValueError("Věk nemůže být záporný")
    if vek > 150:
        raise TooOld("Přílíš velký věk")
    return True

try:
    zkontroluj_vek(200)
except ValueError as e:
    print(f"Chyba hodnoty: {e}")
except TooOld as e:
    print(f"Vlastní chyba: {e}")
    
# task - ošetření chyb
# def bezpecny_vstup(num):
#         vstup = int(input("Zadej PIN: "))
#         if vstup != 1234:
#             print("Neplatný PIN!")
#         return True
    
# try:
#     bezpecny_vstup(4321)
# except ValueError as e:
#     print(f"Chyba hodnoty: {e}")
    
# práce se soubory
# základní čtení
try:
    with open("sample.txt", "r", encoding="utf-8") as soubor:
        obsah = soubor.read()
        print(obsah)
except FileNotFoundError:
    print("Soubor neexistuje!")
    
# čtení po řádcích
try:
    with open("sample.txt", "r", encoding="utf-8") as soubor:
        for line in soubor:
            print(line.strip())
except FileNotFoundError:
    print("Soubor neexistuje!")
    
# načtení počet řádků
try:
    with open("sample.txt", "r", encoding="utf-8") as soubor:
        radky = soubor.readlines()
        print(f"Soubor má {len(radky)} řádků")
except FileNotFoundError:
    print("Soubor neexistuje!")
    
# zápis do souboru