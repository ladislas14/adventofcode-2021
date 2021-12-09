import numpy as np

with open("input.txt") as file:
    crabs = list(map(lambda x: int(x), file.read().split(',')))
    print(int(sum(abs(crabs - np.median(crabs)))))