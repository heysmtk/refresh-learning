# V každém jazyce máme nějaké smyčcky (loops), v pythonu je for a while

# For loop - používá se pro iteraci přes kolekce (list, str, range, atd...)

for i in range(3):  # range(3) = 0, 1, 2
    print(i)
    
# While loop - opakuje se, dokud je podmínka true!

count = 0  # proměnná, která má nastavenou hodnotu 0, dále s ní pracuju
while count < 3:  # když count je menší než 3 vždy se provede dokud je to true
    print(count)  # vypíše aktuální hodnotu proměnné count
    count += 1  # připíše +1 při každé iteraci