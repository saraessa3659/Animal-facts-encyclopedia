from functions import *

def main():
    while True:
        print("\n--- Animal Facts Encyclopedia ---")
        print("1. Search for an animal fact")
        print("2. Add a new animal fact")
        print("3. List all animals")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            animal = input("Enter animal name to search: ").strip().lower()
            fact = search_animal(animal)
            print(f"\n{animal.title()}: {fact}")
        elif choice == '2':
            animal = input("Enter new animal name: ").strip().lower()
            fact = input("Enter a fun fact about this animal: ").strip()
            add_fact(animal, fact)
        elif choice == '3':
            list_animals()
        elif choice == '4':
            print("Thanks for using Animal Facts Encyclopedia! 🐾")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
