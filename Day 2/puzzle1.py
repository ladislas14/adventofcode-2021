with open("input.txt") as input:
    commands = input.readlines()
    horizontal = 0
    depth = 0
    for command in commands:
        commandType = command.split(' ')[0]
        commandValue = int(command.split(' ')[1])
        if commandType == "forward":
            horizontal += commandValue
        elif commandType == "up":
            depth -= commandValue
        elif commandType == "down":
            depth += commandValue
        else:
            print("Error: Unknown command type")
    print(horizontal)
    print(depth * horizontal)