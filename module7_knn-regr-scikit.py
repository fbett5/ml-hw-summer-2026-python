"""
k-NN Regression
---------------
Data initialization / insertion : NumPy
ML computation (fit + predict)  : scikit-learn
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def read_positive_int(prompt):
    """Read a positive integer, re-asking until valid."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Error: the value must be a positive integer.")
        except ValueError:
            print("Error: please enter an integer.")


def read_float(prompt):
    """Read a real number, re-asking until valid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: please enter a real number.")


def main():
    # ---- 1. Read N and k -------------------------------------------------
    N = read_positive_int("Enter N (number of points, positive integer): ")
    k = read_positive_int("Enter k (number of neighbors, positive integer): ")

    # ---- 2. Initialize the arrays with NumPy -----------------------------
    X = np.empty((N, 1), dtype=float)   # features: column vector, as sklearn expects
    y = np.empty(N, dtype=float)        # labels

    # ---- 3. Insert the N (x, y) points one by one ------------------------
    print(f"\nEnter {N} points (x then y for each):")
    for i in range(N):
        X[i, 0] = read_float(f"  Point {i + 1} - x: ")
        y[i] = read_float(f"  Point {i + 1} - y: ")

    # ---- 4. Variance of the labels (NumPy) -------------------------------
    print(f"\nVariance of labels in the training dataset: {np.var(y):.6f}")

    # ---- 5. Read the query point X ---------------------------------------
    x_query = read_float("\nEnter X (query point): ")

    # ---- 6. Validate k and run k-NN Regression (scikit-learn) ------------
    if k > N:
        print(f"Error: k = {k} is greater than N = {N}. "
              f"Cannot run k-NN Regression.")
        return

    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X, y)

    y_pred = model.predict(np.array([[x_query]]))[0]
    print(f"\nk-NN Regression result: Y = {y_pred:.6f}")


if __name__ == "__main__":
    main()