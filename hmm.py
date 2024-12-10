import numpy as np

def find_fixed_vector(matrix, power):
    return np.linalg.matrix_power(matrix, power)[0]

# helper function to append to the correct path, checks length and last state
def append_state(paths, last_state, new_state, new_probability, length):
    for i, path in enumerate(paths):
        if len(path) == length and path[-1][0] == last_state:
            paths[i].append((new_state, new_probability))

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
                append_state(paths, 'A', 'A', a, i)
            else:
                a = b_a
                append_state(paths, 'B', 'A', a, i)

            # A, B --> B
            a_b = last_a * T[0,1] * (bag_a[color] / sum(bag_a.values()))
            b_b = last_b * T[1,1] * (bag_b[color] / sum(bag_b.values()))

            if a_b >= b_b:
                b = a_b
                append_state(paths, 'A', 'B', b, i)
            else:
                b = b_b
                append_state(paths, 'B', 'B', b, i)

    correct_length_paths = [path for path in paths if len(path) == len(sequence)]
    max_probability = max(path[-1][1] for path in correct_length_paths)
    return [path for path in correct_length_paths if path[-1][1] == max_probability]
    
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

    sequence = ['red', 'red', 'black', 'red']

    result = solve_hmm(T, fixed_vector, bag_a, bag_b, sequence)
    print(f"HMMwithPicturesExample: {result}")

    # LONG EXAMPLE 1
    result2 = solve_hmm(T, fixed_vector, bag_a, bag_b, ['red', 'red', 'black', 'red', 'red', 'red', 'black', 'red'])
    print(f"HMMwithPicturesExampleDouble: {result2}")

    T_2 = np.array([[.3, .7], [.6, .4]])
    fixed_vector_2 = find_fixed_vector(T_2, 100)

    bag_a2 = {
        'red': 3,
        'black': 2
    }

    bag_b2 = {
        'red': 2,
        'black': 3
    }

    sequence2 = ['red', 'black', 'black']
    result3 = solve_hmm(T_2, fixed_vector_2, bag_a2, bag_b2, sequence2)
    print(f"TakeHomeP4: {result3}")