"""
Unit tests for analytics functions related to habit tracking.
"""


import datetime
import unittest
from habits.habit import Habit
from habits.analytics import get_longest_streak


class TestAnalytics(unittest.TestCase):
    """Test suite for streak calculation in habits.analytics"""

    def test_streak_single_completion(self):
        """Test a single completion returns a streak of 1"""
        habit = Habit("Meditate", "daily")
        habit.completions = [habit.creation_date]
        self.assertEqual(get_longest_streak(habit), 1)

    def test_streak_consecutive_days(self):
        """Test streak calculation for consecutive daily completions"""
        habit = Habit("Workout", "daily")
        today = datetime.date.today()
        habit.completions = [today - datetime.timedelta(days=i) for i in range(5)]
        self.assertEqual(get_longest_streak(habit), 5)

    def test_streak_non_consecutive_days(self):
        """Test that non-consecutive completions return a streak of 1"""
        habit = Habit("Workout", "daily")
        today = datetime.date.today()
        habit.completions = [today - datetime.timedelta(days=i) for i in [0, 2, 4, 6]]
        self.assertEqual(get_longest_streak(habit), 1)

    def test_streak_weekly_consecutive(self):
        """Test weekly habit with consecutive completions"""
        habit = Habit("Yoga", "weekly")
        today = datetime.date.today()
        habit.completions = [today - datetime.timedelta(weeks=i) for i in range(4)]
        self.assertEqual(get_longest_streak(habit), 4)

    def test_streak_weekly_non_consecutive(self):
        """Test weekly habit with a gap in completions"""
        habit = Habit("Budget review", "weekly")
        today = datetime.date.today()
        habit.completions = [
            today - datetime.timedelta(weeks=0),
            today - datetime.timedelta(weeks=1),
            today - datetime.timedelta(weeks=3),  # gap
            today - datetime.timedelta(weeks=4)
        ]
        self.assertEqual(get_longest_streak(habit), 2)  # only weeks 0 and 1 are consecutive

    def test_streak_empty(self):
        """Test that an empty completions list returns a streak of 0"""
        habit = Habit("Read", "daily")
        habit.completions = []
        self.assertEqual(get_longest_streak(habit), 0)


if __name__ == '__main__':
    unittest.main()
