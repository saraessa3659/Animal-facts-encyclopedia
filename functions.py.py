def load_facts():
    try:
        with open("animaldata.txt", "r") as file:
            lines = file.readlines()
            facts = {}
            for line in lines:
                if ':' in line:
                    animal, fact = line.strip().split(":", 1)
                    facts[animal.strip().lower()] = fact.strip()
            return facts
    except FileNotFoundError:
        return {}

def save_facts(facts):
    with open("animaldata.txt", "a") as file:
        for animal, fact in facts.items():
            file.write(f"{animal}:{fact}\n")

def search_animal(animal):
    facts = load_facts()
    return facts.get(animal, "Sorry, no fact found for that animal.")

def add_fact(animal, fact):
    facts = load_facts()
    facts[animal] = fact
    save_facts(facts)
    print(f"{animal.title()} added successfully!")

def list_animals():
    facts = load_facts()
    if not facts:
        print("No animals in the encyclopedia yet.")
    else:
        print("\nAnimals in the Encyclopedia:")
        for animal in facts:
            print(f"- {animal.title()}")
