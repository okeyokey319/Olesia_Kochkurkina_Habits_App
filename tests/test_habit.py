"""
Unit tests for the Habit class in habits/habit.py.
"""

import unittest
import datetime
from habits.habit import Habit


class TestHabit(unittest.TestCase):
    """
    Test suite for verifying the functionality of the Habit class.
    """

    def test_create_habit(self):
        """
        Test that a Habit object is created with correct name and periodicity.
        """
        habit = Habit("Exercise", "daily")
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.periodicity, "daily")

    def test_mark_complete(self):
        """
        Test that mark_complete adds today's date to completions.
        """
        habit = Habit("Exercise", "daily")
        habit.mark_complete()
        today = datetime.date.today()
        self.assertIn(today, habit.completions)

    def test_mark_complete_only_once_per_day(self):
        """
        Test that mark_complete doesn't add duplicate entries for the same day.
        """
        habit = Habit("Exercise", "daily")
        habit.mark_complete()
        habit.mark_complete()
        self.assertEqual(habit.completions.count(datetime.date.today()), 1)

    def test_get_streak_empty(self):
        """
        Test that streak is 0 for a habit with no completions.
        """
        habit = Habit("Exercise", "daily")
        self.assertEqual(habit.get_streak(), 0)

    def test_get_streak_multiple_days(self):
        """
        Test streak calculation for consecutive daily completions.
        """
        habit = Habit("Exercise", "daily")
        today = datetime.date.today()
        habit.completions = [today - datetime.timedelta(days=i) for i in range(3)]
        self.assertEqual(habit.get_streak(), 3)


if __name__ == "__main__":
    unittest.main()
