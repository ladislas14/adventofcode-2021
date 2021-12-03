with open("input.txt") as input:
    depths = input.readlines()
    count = 1
    
    for i in range(len(depths) - 1):
        if depths[i] < depths[i+1]:
            count += 1
    
    print(count)
