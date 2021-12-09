
def visitDfs(i, j, matrix, alreadyVisited):
    [n, m] = [len(matrix), len(matrix[0])]
    neighborhood = list(filter(lambda cur: matrix[cur[0]][cur[1]] != 9, [[k, j] for k in range(i-1, i+2) if k >= 0 and k < n and k != i] + [
        [i, l] for l in range(j-1, j+2) if l >= 0 and l < m and l != j]))
    alreadyVisited.append([i, j])
    for neighbor in neighborhood:
        if neighbor not in alreadyVisited:
            visitDfs(neighbor[0], neighbor[1], matrix, alreadyVisited)


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
                minima.append([i, j])

    clusters = []
    for minimum in minima:
        current = []
        [i, j] = minimum
        visitDfs(i, j, matrix, current)
        clusters.append(current)

    clusters = list(map(lambda cluster: len(cluster), clusters))
    clusters.sort(reverse=True)
    print(clusters[0] * clusters[1] * clusters[2])
