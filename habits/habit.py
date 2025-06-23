"""
habit.py - Defines the Habit class used to track individual habits,
including periodicity, completion records, and streak calculation.
"""

import datetime


class Habit:
    """
    A class to represent a habit and track its completion over time.

    Attributes:
        name (str): The name of the habit.
        periodicity (str): "daily" or "weekly" indicating the frequency.
        creation_date (date): The date the habit was created.
        completions (list): List of dates when the habit was marked
            as complete.
    """

    def __init__(self, name, periodicity):
        """
        Initialize a new Habit.

        Args:
            name (str): Name of the habit.
            periodicity (str): "daily" or "weekly".
        """
        self.name = name
        self.periodicity = periodicity
        self.creation_date = datetime.date.today()
        self.completions = []

    def mark_complete(self):
        """
        Mark today's date as completed for the habit.
        Prevents duplicate entries for the same day.
        """
        today = datetime.date.today()
        if today not in self.completions:
            self.completions.append(today)

    def get_streak(self):
        """
        Calculate the current streak of the habit based on its periodicity.

        Returns:
            int: The number of consecutive periods the habit was completed.
        """
        if not self.completions:
            return 0

        sorted_completions = sorted(self.completions, reverse=True)
        streak = 0
        delta = datetime.timedelta(
            days=1 if self.periodicity == "daily" else 7
        )

        for i in range(len(sorted_completions) - 1):
            if (
                sorted_completions[i] - sorted_completions[i + 1]
                == delta
            ):
                streak += 1
            else:
                break

        return streak + 1  # Include the first day
