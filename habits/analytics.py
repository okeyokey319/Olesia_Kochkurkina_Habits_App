"""
Analytics module for habit tracking.

This module provides analytical functions to evaluate and filter habit data,
such as filtering by periodicity, calculating the longest streak, and
counting total completions.
"""


def filter_habits_by_periodicity(habits, periodicity):
    """
    Filter habits by their periodicity.

    Args:
        habits (list): List of Habit instances.
        periodicity (str): "daily" or "weekly".

    Returns:
        list: Habits with the specified periodicity.
    """
    return [habit for habit in habits if habit.periodicity == periodicity]


def get_longest_streak(habit):
    """
    Get the longest streak of a habit.

    Args:
        habit (Habit): The habit instance.

    Returns:
        int: Longest streak count.
    """
    return habit.get_streak()


def get_total_completions(habit):
    """
    Get the total number of completions for a habit.

    Args:
        habit (Habit): The habit instance.

    Returns:
        int: Total times the habit was completed.
    """
    return len(habit.completions)
