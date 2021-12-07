with open("input.txt") as file:
    crabs = list(map(lambda x: int(x), file.read().split(',')))
    result = max(crabs) * len(crabs)
    for position in range(max(crabs)):
        curSum = 0
        for crab in [x for x in crabs if x != position]:
            curSum += abs(crab - position)
        if curSum < result:
            result = curSum
        

    print(result)