"""
module5_call.py

Main program for Module 5. It imports the NumberStore class from the
module5_mod.py file and uses it to read N numbers from the user, then
searches for X and outputs its index (from 1 to N), or -1 if X was
never entered.

Run with:  python module5_call.py
(module5_mod.py must be in the same folder)
"""

from module5_mod import NumberStore


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
