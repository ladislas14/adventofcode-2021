with open("test.txt") as file:
    fishes = list(map(lambda x: int(x), file.read().split(',')))
    l = len(fishes)
    for i in range(80):
        for j in range(l):
            if fishes[j] == 0:
                fishes[j] = 6
                fishes.append(8)
                l += 1
            else:
                fishes[j] -= 1
    print(len(fishes))