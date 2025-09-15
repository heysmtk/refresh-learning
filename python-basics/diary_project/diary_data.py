import json
from datetime import datetime


def load_entries():
    """
    Load all diary entries from the JSON file.

    If the file does not exist, returns an empty list.

    Returns:
        list[dict]: A list of dictionaries, each representing a diary entry 
        with keys 'id', 'date', and 'text'.
    """
    try:
        with open("python-basics/diary_project/diary.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    

def save_entries(entries):
    """
    Save a list of diary entries to the JSON file.

    Args:
        entries (list[dict]): A list of dictionaries, each representing a diary entry 
        with keys 'id', 'date', and 'text'.
    """
    with open("python-basics/diary_project/diary.json", "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=4, ensure_ascii=False)
        

def add_entry(date=None, text="No text."):
    """
    Add a new diary entry to the JSON file.

    If no date is provided, the current date and time will be used.
    Automatically assigns a unique ID to the new entry.

    Args:
        date (str, optional): The date and time of the entry in "YYYY-MM-DD HH:MM:SS" format. Defaults to None.
        text (str, optional): The text content of the entry. Defaults to "No text.".

    Returns:
        dict: The newly created diary entry as a dictionary with keys 'id', 'date', and 'text'.
    """
    entries = load_entries()
    
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    if entries == []:
        new_id = 1
    else:
        new_id = max(entry["id"] for entry in entries) + 1
        
    new_entry = {
        "id": new_id,
        "date": date,
        "text": text
    }
    
    entries.append(new_entry)
    save_entries(entries)
    return new_entry


def delete_entry(entry_id):
    """
    Delete a diary entry by its ID.

    Searches for the entry with the specified ID and removes it from the JSON file.

    Args:
        entry_id (int): The unique ID of the diary entry to delete.

    Returns:
        bool: True if the entry was found and deleted, False if no entry with the given ID exists.
    """
    entries = load_entries()
    find = False
    new_entries = []
    
    for entry in entries:
        if entry["id"] == entry_id:
            find = True
        else:
            new_entries.append(entry)
    
    save_entries(new_entries)
    return find
 
 
 

# ------------------------------------------------------------------------

# print("Před smazáním:")
# print(load_entries())

# print("Výsledek smazání:", delete_entry(8))

# print("Po smazání:")
# print(load_entries())

# testovací přidání nového zápisu
# new_entry = add_entry(text="Dnes jsem testoval add_entry funkci.")
# print("Nový záznam:", new_entry)

# # načtení všech záznamů, abychom viděli, že se přidal
# all_entries = load_entries()
# print("Všechny záznamy:")
# for entry in all_entries:
#     print(entry)
        
# Test set
# dataset = [
#     {"id": 1, "date": "2025-09-10", "text": "Šel jsem na procházku"},
#     {"id": 2, "date": "2025-09-11", "text": "Pracoval jsem na projektu"},
#     {"id": 3, "date": "2025-09-12", "text": "Byl jsem ve fitku"},
#     {"id": 4, "date": "2025-09-13", "text": "Četl jsem knihu"},
#     {"id": 5, "date": "2025-09-14", "text": "Hrál jsem deskovky s rodinou"}
# ]

# save_entries(dataset)
# print(load_entries())