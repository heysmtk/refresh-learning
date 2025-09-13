# Práce se soubory pomocí - open()
# "w" - zápis do souboru (w-write)
# "a" - přídání do souboru (a-append)
# "r" - čtení ze souboru (r-read)
# with - automatické zavře soubor = with open()

# Zápis do souboru
with open("soubor.txt", "w") as f:
    f.write("Ahoj soubore, jsem tady!\n")
 
# přidání dalšího textu do souboru   
with open("soubor.txt", "a") as f:
    f.write("Tohle je další řádek!\n")
    
# čtení ze souboru
with open("soubor.txt","r") as f:
    print(f.read())

# vyčte řádek po řádku, strip() odstraní prázné řádky a mezery
with open("soubor.txt", "r") as f:
    for line in f:
        print("line:", line.strip())

# readline vyčte jeden řádek ze souboru
with open("soubor.txt", "r") as f:
    print(f.readline())
    
# readlines vyčte seznam všech řádků
with open("soubor.txt", "r") as f:
print(f.readlines())