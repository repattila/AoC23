
def followRoute(field, row, col, visited, steps):
    currRow = row
    currCol = col

    if currRow != len(field) - 1:
        # Up
        nextRow = currRow - 1
        nextCol = currCol

        if 0 <= nextRow \
        and (nextRow, nextCol) not in visited \
        and field[nextRow][nextCol] not in ['#', 'v']:
            newVisited = set(visited)
            newVisited.add((nextRow, nextCol))
            followRoute(field, nextRow, nextCol, newVisited, steps + 1)

        # Down
        nextRow = currRow + 1
        nextCol = currCol

        if nextRow < len(field) \
        and (nextRow, nextCol) not in visited \
        and field[nextRow][nextCol] not in ['#', '^']:
            newVisited = set(visited)
            newVisited.add((nextRow, nextCol))
            followRoute(field, nextRow, nextCol, newVisited, steps + 1)

        # Right
        nextRow = currRow
        nextCol = currCol + 1

        if nextCol < len(field[row]) \
        and (nextRow, nextCol) not in visited \
        and field[nextRow][nextCol] not in ['#', '<']:
            newVisited = set(visited)
            newVisited.add((nextRow, nextCol))
            followRoute(field, nextRow, nextCol, newVisited, steps + 1)

        # Left
        nextRow = currRow
        nextCol = currCol - 1

        if 0 <= nextCol \
        and (nextRow, nextCol) not in visited \
        and field[nextRow][nextCol] not in ['#', '>']:
            newVisited = set(visited)
            newVisited.add((nextRow, nextCol))
            followRoute(field, nextRow, nextCol, newVisited, steps + 1)
    else:
        print(steps)

field = []
def solve23():
    f = open("input23.txt", "r")
    rawLines = f.readlines()

    for rawLine in rawLines:
        field.append(rawLine.strip())

    followRoute(field, 0, 1, set(), 0)

