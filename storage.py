"""
Module for loading and saving habit data to and from JSON.
"""

import json
import datetime
from habits.habit import Habit


def load_habits_from_json(file_path):
    """
    Load habits from a JSON file and return them as Habit objects.

    Args:
       file_path (str): Path to the JSON file.

    Returns:
        list: A list of Habit objects.
    """
    with open(file_path, 'r', encoding='utf-8') as f:

        data = json.load(f)

    habits = []
    for item in data:
        habit = Habit(
            name=item['name'],
            periodicity=item['periodicity']
        )
        habit.creation_date = datetime.date.fromisoformat(item['creation_date'])
        habit.completions = [
            datetime.date.fromisoformat(date_str)
            for date_str in item.get('completions', [])
        ]
        habits.append(habit)

    return habits


def save_habits_to_json(habits, file_path):
    """
    Save a list of Habit objects to a JSON file.

    Args:
        habits (list): A list of Habit objects.
        file_path (str): Path to the JSON file.
    """
    data = []
    for habit in habits:
        data.append({
            'name': habit.name,
            'periodicity': habit.periodicity,
            'creation_date': habit.creation_date.isoformat(),
            'completions': [date.isoformat() for date in habit.completions]
        })

    with open(file_path, 'r', encoding='utf-8') as f:

        json.dump(data, f, indent=4)
