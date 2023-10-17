import yaml

def prompt_for_new_settlement():
    new_settlement = {}
    new_settlement['id'] = input("Enter the ID for the new settlement: ")
    new_settlement['title'] = input("Enter the title for the new settlement: ")
    # ... (rest of the code remains the same)

def read_existing_settlements(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f) or []

def write_new_settlements(file_path, settlements):
    with open(file_path, 'w') as f:
        yaml.dump(settlements, f)

def display_menu():
    print("1: Add a new settlement")
    print("2: Delete a settlement")
    print("3: View all settlements")
    print("4: Clear all settlements")
    print("5: Exit")
    return input("Select an option: ")

def main():
    file_path = '_data/settlements.yml'
    while True:
        choice = display_menu()
        
        if choice == '1':
            new_settlement = prompt_for_new_settlement()
            existing_settlements = read_existing_settlements(file_path)
            existing_settlements.append(new_settlement)
            write_new_settlements(file_path, existing_settlements)
            print("New settlement added successfully!")
        
        elif choice == '2':
            id_to_delete = input("Enter the ID of the settlement to delete: ")
            settlements = read_existing_settlements(file_path)
            settlements = [s for s in settlements if s['id'] != id_to_delete]
            write_new_settlements(file_path, settlements)
            print(f"Settlement {id_to_delete} deleted.")
        
        elif choice == '3':
            settlements = read_existing_settlements(file_path)
            for s in settlements:
                print(s)
        
        elif choice == '4':
            write_new_settlements(file_path, [])
            print("All settlements cleared.")
        
        elif choice == '5':
            break

        else:
            print("Invalid choice, please try again.")
        
        print("\n")

if __name__ == "__main__":
    main()
