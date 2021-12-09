import numpy as np

with open("input.txt") as file:
    crabs = list(map(lambda x: int(x), file.read().split(',')))
    mean = np.mean(crabs)
    print(mean - 1/2, mean + 1/2)