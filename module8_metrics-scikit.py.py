"""
Vmodule8_metrics-scikit.py

Reads N (x, y) points from the user, where:
    x = ground truth (correct) class label  -> 0 or 1
    y = predicted class label               -> 0 or 1

Data initialization / insertion : NumPy
Metric computation (ML part)    : scikit-learn

Outputs Precision and Recall.
"""

import numpy as np
from sklearn.metrics import precision_score, recall_score


def read_positive_int(prompt):
    """Keep asking until the user enters a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("  -> Value must be a positive integer. Try again.")
        except ValueError:
            print("  -> That is not an integer. Try again.")


def read_binary(prompt):
    """Keep asking until the user enters 0 or 1."""
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return value
            print("  -> Value must be 0 or 1. Try again.")
        except ValueError:
            print("  -> That is not an integer. Try again.")


def main():
    # ---------- input ----------
    n = read_positive_int("Enter N (positive integer): ")

    # NumPy: initialize the array, then insert the points one by one
    data = np.zeros((n, 2), dtype=int)

    print()
    for i in range(n):
        print(f"Point {i + 1}:")
        data[i, 0] = read_binary("  x (true label, 0 or 1): ")
        data[i, 1] = read_binary("  y (predicted label, 0 or 1): ")

    # NumPy slicing to split the columns
    y_true = data[:, 0]
    y_pred = data[:, 1]

    # ---------- computation (scikit-learn) ----------
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    # ---------- output ----------
    print("\n--- Results ---")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")


if __name__ == "__main__":
    main()
