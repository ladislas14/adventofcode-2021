with open("input.txt") as input:
    depths = input.readlines()
    count = 0
    for i in range(len(depths) - 3):
        a = int(depths[i]) + int(depths[i+1]) + int(depths[i+2])
        b = int(depths[i+1]) + int(depths[i+2]) + int(depths[i+3])
        if a < b:
            count += 1

    print(count)