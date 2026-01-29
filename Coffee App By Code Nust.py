"""
This app helps people decide
what to eat for dinner
"""

import webbrowser

def homepage():
    print("Dinner Picker")
    print("-------------")
    print("Old Meals:1")
    print("Create New Meals:2")

    choice = input("choose 1 or 2: ")

    if choice == '1':
        old_meals()
    elif choice == '2':
        create_new_meals()
    else:
        print("Invalid choice. Try again")
        homepage()

def old_meals():
    print("\n--- Saved Meals ---")
    try:
        with open("meals.txt", "r") as file:
            meals = [m.strip() for m in file.readlines() if m.strip()]
            
        if not meals:
            print("No saved meals found.")
            print("-------------------")
            input("Press Enter to go back...")
            homepage()
            return

        for index, meal in enumerate(meals):
            print(f"{index + 1}. {meal}")
        
        print("-------------------")
        print("Enter the number of the meal to search again, or press Enter to go back.")
        choice = input("Choice: ")
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(meals):
                query = meals[idx]
                url = "https://www.bettycrocker.com/" + query
                print("Opening your browser for:", url)
                webbrowser.open(url)
            else:
                print("Invalid number.")
        
    except FileNotFoundError:
        print("No saved meals found.")
        print("-------------------")
        input("Press Enter to go back...")
    
    homepage()

def create_new_meals():
    print("Create a New Meal")
    query = input("Type your cravings here: ")
    url = "https://www.bettycrocker.com/" + query
    print("Opening your browser for:", url)
    webbrowser.open(url)

    save_choice = input("Would you like to save this search? (y/n): ")
    if save_choice.lower() == 'y':
        with open("meals.txt", "a") as file:
            file.write(query + "\n")
        print("Search saved!")
    
    homepage()

homepage()
