"""
module5_mod.py

Module that contains the NumberStore class used by module5_call.py.
The class implements the basic data processing functionality:
data initialization, data insertion, and data search.
"""


class NumberStore:
    """A simple container class that stores numbers and supports search."""

    def __init__(self):
        """Data initialization: create an empty list to hold the numbers."""
        self.numbers = []

    def insert(self, value):
        """Data insertion: add one number to the end of the store."""
        self.numbers.append(value)

    def search(self, x):
        """Data search: return the 1-based index of the first occurrence
        of x in the store, or -1 if x is not present."""
        for index, value in enumerate(self.numbers, start=1):
            if value == x:
                return index
        return -1
