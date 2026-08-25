"""
module5_oop.py

The program asks the user for a positive integer N, then reads N numbers
one by one. Finally, it asks the user for an integer X and outputs the
index (from 1 to N) of X among the entered numbers, or -1 if X was
never entered.

The basic data processing functionality (data initialization, data
insertion, data search) is implemented using the Object-Oriented
Programming paradigm via the NumberStore class below.
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


def main():
    # Read N and make sure it is a positive integer
    n = int(input("Enter N (positive integer): "))
    while n <= 0:
        n = int(input("N must be positive. Enter N again: "))

    # Create the storage object (data initialization happens in __init__)
    store = NumberStore()

    # Read N numbers one by one and insert each of them into the store
    for i in range(1, n + 1):
        number = int(input(f"Enter number {i}: "))
        store.insert(number)

    # Read X and output the search result: index from 1 to N, or -1
    x = int(input("Enter X (integer): "))
    print(store.search(x))


if __name__ == "__main__":
    main()
