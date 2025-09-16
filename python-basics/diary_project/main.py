from diary_data import add_entry, delete_entry, load_entries


def main():
    print("Welcome to Diary Notes!")
    
    while True:
        try:
            print("------------------------------------------")
            print("1 - Add | 2 - Delete | 3 - Show | 4 - Exit")
            user_input = int(input("Your command: "))

            if user_input == 1:
                text = input("Write your diary entry: ")
                new_entry = add_entry(text=text)
                print(f"Entry added with ID {new_entry['id']}.")
            
            elif user_input == 2:
                try:
                    entry_id = int(input("Enter ID of entry to delete: "))
                    success = delete_entry(entry_id)
                    if success:
                        print("Entry deleted.")
                    else:
                        print("No entry with that ID.")
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            
            elif user_input == 3:
                notes = load_entries()
                if not notes:
                    print("No notes found.")
                else:
                    for note in notes:
                        print(f"[{note['id']}] {note['date']} - {note['text']}")
            
            elif user_input == 4:
                print("Exiting program...")
                break
            
            else:
                print("ERROR: Invalid input, try again.")
                        
        except ValueError:
            print("ERROR: The value must be a integer!")
        

if __name__ == "__main__":
    main()