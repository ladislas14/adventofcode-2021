with open("input.txt") as file:
    fishesCount = [0] * 9
    
    for value in file.read().split(','):
        fishesCount[int(value)] += 1
    
    for i in range(256):
        newFishes = fishesCount[0]
        for i in range(8):
            fishesCount[i] = fishesCount[i+1]

        fishesCount[6] += newFishes
        fishesCount[8] = newFishes

    print(sum(fishesCount))