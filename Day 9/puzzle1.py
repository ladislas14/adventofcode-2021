with open("input.txt") as file:
    matrix = [list(map(lambda x: int(x), list(line.rstrip('\n'))))
              for line in file.readlines()]
    minima = []
    result = 0
    [n, m] = [len(matrix), len(matrix[0])]
    for i in range(n):
        for j in range(m):
            neightborhood = [matrix[i][j] < matrix[k][l] for k in range(
                i-1, i+2) if k >= 0 and k < n for l in range(j-1, j+2) if l >= 0 and l < m and (k != i or l != j)]
            if all(neightborhood):
                minima.append(matrix[i][j])
                result += matrix[i][j] + 1
    print(result)
