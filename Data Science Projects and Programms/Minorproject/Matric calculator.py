import numpy123 as np

class MatrixCalculator:
    @staticmethod
    def input_matrix(name="Matrix"):
        matrix = np.zeros((2, 2), dtype=int)
        print(f"Enter values for {name}:")
        for i in range(2):
            for j in range(2):
                matrix[i][j] = int(input(f"Enter element {i}{j}: "))
        return matrix

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return np.dot(a, b)

    @staticmethod
    def transpose(matrix):
        return matrix.T

# --- Main Program ---
print("Welcome to 2x2 Matrix Calculator!")

# Input matrices
a = MatrixCalculator.input_matrix("Matrix A")
b = MatrixCalculator.input_matrix("Matrix B")

# Menu
print("\nSelect Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose")

choice = int(input("Enter your choice (1-4): "))

# Operation Execution
if choice == 1:
    result = MatrixCalculator.add(a, b)
    print("Result of Addition:")
    print(result)
elif choice == 2:
    result = MatrixCalculator.subtract(a, b)
    print("Result of Subtraction:")
    print(result)
elif choice == 3:
    result = MatrixCalculator.multiply(a, b)
    print("Result of Multiplication:")
    print(result)
elif choice == 4:
    print("Transpose of Matrix A:")
    print(MatrixCalculator.transpose(a))
    print("Transpose of Matrix B:")
    print(MatrixCalculator.transpose(b))
else:
    print("Invalid choice!")
