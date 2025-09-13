# String - řetězec znaků (text), je iterovatelný jako list
# Umí indexovat, řezat (slice), metody (upper, lower...)
# Formátování pomocí f-stringů (skvělá věc!)

text = "Python"
print(text[0])      # "P" - 0 je první index, nikoliv 1
print(text[-1])     # "n" - -1 je vždy poslední index
print(text[0:3])    # "Pyt" - 0 až 3 index
print(text.upper()) # PYTHON - metoda pro všechny znaky velké

name = "Tomáš"
age = 30
print(f"Ahoj, jmenuji se {name} a je mi {age} let.") # - formátovaný string