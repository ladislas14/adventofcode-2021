import functools

with open("input.txt") as input:
    lines = input.readlines()
    gamma = [0] * (len(lines[0]) - 1)
    epsilon = [0] * (len(lines[0]) - 1) 
    for line in lines:
        for i in range(len(line) - 1):
            gamma[i] += int(line[i])

    for j in range(len(gamma)):
        if gamma[j] > len(lines) / 2:
            gamma[j] = 1
            epsilon[j] = 0
        else:
            gamma[j] = 0
            epsilon[j] = 1

    gammaInt = 0
    epsilonInt = 0
    for i in range(len(gamma)):
        gammaInt += gamma[len(gamma) - (i + 1)] * 2**i
        epsilonInt +=  epsilon[len(epsilon) - (i + 1)] * 2**i
    print(gammaInt * epsilonInt)