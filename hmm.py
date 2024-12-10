import numpy as np

def find_fixed_vector(matrix, power):
    return np.linalg.matrix_power(matrix, power)[0]

def solve_hmm(T, fixed_vector, bag_a, bag_b, sequence):
    # last respective probability
    a = int()
    b = int()

    # all possible paths
    paths = []

    for i in range(len(sequence)):
        color = sequence[i]
        if i == 0:
            # fixed vector is < a , b >
            # probably of color given a choosen bag
            a = fixed_vector[0] * (bag_a[color] / sum(bag_a.values()))
            paths.append([('A', a)])
            b = fixed_vector[1] * (bag_b[color] / sum(bag_b.values()))
            paths.append([('B', b)])
        else:
            # temp variables
            last_a = a
            last_b = b
            
            # A, B --> A
            a_a = last_a * T[0,0] * (bag_a[color] / sum(bag_a.values()))
            b_a = last_b * T[1,0] * (bag_b[color] / sum(bag_b.values()))

            if a_a >= b_a:
                a = a_a                    
            else:
                a = b_a

            # A, B --> B
            a_b = last_a * T[0,1] * (bag_a[color] / sum(bag_a.values()))
            b_b = last_b * T[1,1] * (bag_b[color] / sum(bag_b.values()))

            if a_b >= b_b:
                b = a_b
            else:
                b = b_b

    print(paths)



if __name__ == "__main__":
    T = np.array([[.8, .2], [.5, .5]])
    fixed_vector = find_fixed_vector(T, 100)

    bag_a = {
        'red': 4,
        'black': 6
    }

    bag_b = {
        'red': 7,
        'black': 3
    }

    sequence = ['red', 'red']

    solve_hmm(T, fixed_vector, bag_a, bag_b, sequence)
