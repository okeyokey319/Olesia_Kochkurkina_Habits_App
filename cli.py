"""
Command-line interface (CLI) for the Habit Tracking App.
"""

import json
from habits.habit import Habit
from storage import load_habits_from_json


def load_habits():
    """
    Load habits from the JSON file using storage module.

    Returns:
        list: A list of Habit objects.
    """
    return load_habits_from_json("data/habits.json")


def save_habits(habits):
    """
    Save current habits list to the JSON file.

    Args:
        habits (list): List of Habit objects to save.
    """
    with open("data/habits.json", "w", encoding="utf-8") as f:
        json.dump([habit.__dict__ for habit in habits], f, default=str)


def main():
    """
    Main function to handle CLI interaction with the user.
    """
    habits = load_habits()

    print("1. Create habit\n2. Mark complete\n3. View stats\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter habit name: ")
        periodicity = input("Enter periodicity (daily/weekly): ")
        habits.append(Habit(name, periodicity))

    elif choice == "2":
        for i, h in enumerate(habits):
            print(f"{i + 1}. {h.name}")
        idx = int(input("Choose habit to mark complete: ")) - 1
        habits[idx].mark_complete()

    elif choice == "3":
        for habit in habits:
            print(f"{habit.name}: {habit.get_streak()} streak")

    save_habits(habits)


if __name__ == "__main__":
    main()
