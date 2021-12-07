with open("input.txt") as file:
    crabs = list(map(lambda x: int(x), file.read().split(',')))
    result = sum(i for i in range(max(crabs) - min(crabs))) * len(crabs)
    for position in range(max(crabs)):
        curSum = 0
        for crab in [x for x in crabs if x != position]:
            dif = abs(crab - position)
            curSum += sum([i for i in range(dif + 1)])
            if curSum > result:
                break
        if curSum < result:
            result = curSum
        

    print(result)