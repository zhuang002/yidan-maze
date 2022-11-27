cases = int(input())


def move(deltaR: int, deltaC: int, pos: tuple[int, int], graph: list[list[str]], recording: list[list[int]]) -> int:
    if deltaR != 0 and graph[pos[0]][pos[1]] != '|' and graph[pos[0]][pos[1]] != '+':
        return None
    if deltaC != 0 and graph[pos[0]][pos[1]] != '-' and graph[pos[0]][pos[1]] != '+':
        return None

    nextPos = (pos[0] + deltaR, pos[1] + deltaC)
    if nextPos[0] < 0 or nextPos[0] >= len(graph) or nextPos[1] < 0 or nextPos[1] >= len(graph[0]):
        return None
    if recording[nextPos[0]][nextPos[1]] != -1:
        return None
    return nextPos


def getShortestPath(graph: list[str]) -> int:
    rows = len(graph)
    cols = len(graph[0])
    recording = [[-1] * cols for i in range(rows)]

    next = []
    target = [(row, col)]
    current = [(0, 0)]
    step = 0

    while not current:
        for coord in current:
            step += 1
            recording[coord[0]][coord[1]] = step
            nextCoord = move(-1, 0, coord, graph, recording)
            if nextCoord == target:
                return step + 1
            if nextCoord:
                next.append(nextCoord)
            nextCoord = move(1, 0, coord, graph, recording)
            if nextCoord == target:
                return step + 1
            if nextCoord:
                next.append(nextCoord)
            nextCoord = move(0, 1, coord, graph, recording)
            if nextCoord == target:
                return step + 1
            if nextCoord:
                next.append(nextCoord)
            nextCoord = move(0, -1, coord, graph, recording)
            if nextCoord == target:
                return step + 1
            if nextCoord:
                next.append(nextCoord)
        current = next
        next = []
    return -1


for i in range(cases):
    rows = int(input())
    cols = int(input())
    graph = [[None] * cols for j in range(rows)]
    for row in range(rows):
        s = input()
        for col in range(cols):
            graph[row][col] = s[col]
    print(getShortestPath(graph))
