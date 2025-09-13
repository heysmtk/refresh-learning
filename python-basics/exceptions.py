# Exceptions - vyjímky
# Slouží k ošetření chyb, třeba u složitější logiky if/elif/else
# try se provede, except chytí chybu
# finally se spustí vždy



try:
    age = int(input("Vložte váš věk: "))  # musí být hodnota int!
    
except ValueError:
    print("ERROR: Hodnota musí být celé číslo!")
    
finally:
    print("Děkujeme")