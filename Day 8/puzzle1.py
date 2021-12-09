with open("input.txt") as file:
    outputs = [y[1].split(' ') for y in (
        x.rstrip('\n').split(' | ') for x in file.readlines())]
    print(outputs)
    flattenOutputs = [len(item) for sublist in outputs for item in sublist]
    totCount = 0
    for output in flattenOutputs:
        if output == 2 or output == 3 or output == 4 or output == 7:
            totCount += 1

    print(totCount)
