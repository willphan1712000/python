import numpy as np
import math


def sigmoid(x):
    return 1 / (1 + math.e ** (-x))

# Layer 1 - input layer
X = np.array([[1,0,1]])

# Layer 2 - hidden layer
W11 = np.array([[0.2, -0.3], [0.4, 0.1], [-0.5, 0.2]])
B11 = np.array([[-0.4, 0.2]])
A11 = sigmoid(X @ W11 + B11)

# Layer 3 - output layer
W111 = np.array([[-0.3], [-0.2]])
B111 = np.array([[0.1]])
A111 = sigmoid(A11 @ W111 + B111)

# Target
T = np.array([[1]])
# Learning rate
r = 0.9


n = 100000

for i in range(n):
    print("Training loop " + str(i))
    # Back propagation
    A111_diag = np.diag(A111).reshape(-1,1)
    dCdb111 = (A111 - T) @ A111_diag @ (1 - A111_diag)

    B111 = B111 - r * dCdb111 # update B111

    W111 = W111 - r * A11.T @ dCdb111 # update W111

    A11_diag = np.diag(A11).reshape(-1, 1)
    dCdb11 = dCdb111 @ A11_diag @ (1 - A11_diag)

    B11 = B11 - r * dCdb11 # update B11

    W11 = W11 - r * X.T @ dCdb11 # update W11

    # Feed Forward
    A11 = sigmoid(X @ W11 + B11)

    A111 = sigmoid(A11 @ W111 + B111)


# Feed Forward
A11 = sigmoid(X @ W11 + B11)

A111 = sigmoid(A11 @ W111 + B111)

print(A111)

print("Weight before layer 3:")
print(W111)
print("Bias on layer 3:")
print(B111)
print("Weight before layer 2:")
print(W11)
print("Bias on layer 2:")
print(B11)