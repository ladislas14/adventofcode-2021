import numpy

with open("input.txt") as file:
    fishes = numpy.array(list(map(lambda x: int(x), file.read().split(','))))
    counts = numpy.bincount(fishes)
    fishesCount = list(counts) + [0] * (9 - len(counts))
    for i in range(256):
        newCount = [0] * 9
        for j in range(9):
            if j == 8:
                newCount[j] = fishesCount[0]
            elif j == 6:
                newCount[j] = fishesCount[0] + fishesCount[7]
            else:
                newCount[j] = fishesCount[j+1]
        fishesCount = newCount.copy()
    print(sum(fishesCount))