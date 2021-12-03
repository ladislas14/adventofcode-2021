def filterLinesForO2(lines, index):
    left = []
    right = []
    for line in lines:
        if int(line[index]) == 1:
            left.append(line)
        else:
            right.append(line)
    if len(left) >= len(right):
        return left
    else:
        return right

def filterLinesForCO2(lines, index):
    left = []
    right = []
    for line in lines:
        if int(line[index]) == 1:
            left.append(line)
        else:
            right.append(line)
    if len(left) < len(right):
        return left
    else:
        return right


with open("input.txt") as input:
    lines = input.readlines()
    o2 = lines.copy()
    co2 = lines.copy()
    i = 0
    while len(o2) != 1 and i < len(lines[0]):
        o2 = filterLinesForO2(o2, i)
        i += 1

    j = 0
    while len(co2) != 1 and j < len(lines[0]):
        co2 = filterLinesForCO2(co2, j)
        j += 1
    
    print(int(o2[0].strip('\n'), 2))
    print(int(co2[0].strip('\n'), 2))
    print(int(o2[0].strip('\n'), 2) * int(co2[0].strip('\n'), 2))
        
