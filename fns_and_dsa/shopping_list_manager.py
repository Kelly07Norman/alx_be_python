def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the list.")
        elif choice == 2:
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                item = input("Enter the item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} has been removed from the list.")
                else:
                    print(f"{item} is not in the list.")
        elif choice == 3:
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
