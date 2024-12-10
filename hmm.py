import numpy as np
from fractions import Fraction

def find_fixed_vector(ndarray, power):
    return np.linalg.matrix_power(ndarray, power)[0]

if __name__ == "__main__":
    A = np.array([[.8, .2], [.5, .5]])
    print(find_fixed_vector(A, 100))