import numpy as np  # import NumPy library for data storage and calculations

# --- Read N: number of points ---
N = int(input("Enter N (positive integer): "))

# --- Read k: number of nearest neighbors ---
k = int(input("Enter k (positive integer): "))

# --- Initialize empty NumPy arrays to store the points ---
x_points = np.empty(N)  # array for x coordinates
y_points = np.empty(N)  # array for y coordinates

# --- Read N points from the user, one by one (first x, then y) ---
for i in range(N):
    x = float(input(f"Point {i + 1} - enter x: "))
    y = float(input(f"Point {i + 1} - enter y: "))
    x_points[i] = x  # store x value in the array
    y_points[i] = y  # store y value in the array

# --- Read the query value X for prediction ---
X = float(input("Enter X for prediction: "))

# --- k-NN Regression works only if k <= N ---
if k <= N:
    # calculate distance from X to every stored x coordinate
    distances = np.abs(x_points - X)

    # sort distances and take indices of the k nearest points
    nearest = np.argsort(distances)[:k]

    # regression result: average of the y values of the k nearest points
    result = np.mean(y_points[nearest])

    print("Result (Y):", result)
else:
    # error message if k is greater than N
    print("Error: k cannot be greater than N")

    