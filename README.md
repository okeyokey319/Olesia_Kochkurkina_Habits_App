# Habit Tracker

**Habit Tracker** is a simple command-line Python app to help you track and analyze your daily and weekly habits. It stores data in a JSON file and includes basic analytics such as current streak calculation.

## Features

- Create habits with `daily` or `weekly` periodicity  
- Mark habits as completed  
- Track current streaks based on periodicity  
- Store data in `data/habits.json`  
- Analyze habits using built-in analytics module  

## Project Structure

```
habit-tracker/
│
├── habits/
│   ├── habit.py          # Habit class
│   ├── analytics.py      # Analytics functions
│   └── __init__.py
│
├── data/
│   └── habits.json       # Predefined habit data
│
├── tests/                # Unit tests
│   ├── test_habit.py
│   └── test_analytics.py
│
├── storage.py            # Load/save habits to JSON
├── cli.py                # Command-line interface
└── README.md
```

## ▶Getting Started

1. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Run the app:
   ```bash
   python cli.py
   ```

3. Follow the menu:
   ```
   1. Create habit
   2. Mark complete
   3. View stats
   4. Exit
   ```

## Running Tests

Make sure `pytest` is installed:
```bash
pip install pytest
```

Then run:
```bash
pytest
```

## Data File

The app uses `data/habits.json` for predefined habit data, including at least 4 weeks of activity for testing streak logic.

