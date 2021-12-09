def checkContainsSublist(sublist, list):
    return all(x in list for x in sublist)


with open("input.txt") as file:
    lines = file.readlines()
    inputs = list(map(lambda cur: [list(el) for el in cur], [y[0].split(' ') for y in (
        x.rstrip('\n').split(' | ') for x in lines)]))
    outputs = [z[1].split(' ') for z in (
        w.rstrip('\n').split(' | ') for w in lines)]
    result = 0
    for i in range(len(inputs)):
        mapping = [[]] * 10
        for input in inputs[i]:
            if len(input) == 2:
                mapping[1] = input
            elif len(input) == 4:
                mapping[4] = input
            elif len(input) == 3:
                mapping[7] = input
            elif len(input) == 7:
                mapping[8] = input

        # Search 3:
        mapping[3] = (list(filter(lambda cur: len(cur) ==
                                  5 and checkContainsSublist(mapping[1], cur), inputs[i])))[0]

        # Search 9:
        mapping[9] = (list(filter(lambda cur: len(cur) ==
                                  6 and checkContainsSublist(mapping[4], cur), inputs[i])))[0]

        # Search 0:
        mapping[0] = (list(filter(lambda cur: len(cur) == 6 and cur !=
                                  mapping[9] and checkContainsSublist(mapping[1], cur), inputs[i])))[0]

        # Search 6:
        mapping[6] = (list(filter(lambda cur: len(cur) == 6 and cur !=
                                  mapping[9] and cur != mapping[0], inputs[i])))[0]

        # Search 5:
        mapping[5] = (list(filter(lambda cur: len(cur) ==
                                  5 and checkContainsSublist(cur, mapping[6]), inputs[i])))[0]

        # Search 5:
        mapping[2] = (list(filter(lambda cur: len(cur) ==
                                  5 and cur != mapping[3] and cur != mapping[5], inputs[i])))[0]

        nb = ""
        for output in outputs[i]:
            for digit in range(len(mapping)):
                if len(output) == len(mapping[digit]) and checkContainsSublist(output, mapping[digit]):
                    nb += str(digit)
        result += int(nb)

    print(result)
