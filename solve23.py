
class Path:
    def __init__(self, row, col, visited, steps):
        self.row = row
        self.col = col
        self.visited = set(visited)
        self.steps = steps

    def makeStep(self, row, col):
        self.row = row
        self.col = col
        self.visited.add((row, col))
        self.steps += 1

import collections

def followRoute(field, paths: collections.deque, endSteps):
    while paths:
        print(len(paths))
        currPath = paths.popleft()

        while currPath.row != len(field) - 1:
            hasFirstRouteOption = False

            currRow = currPath.row
            currCol = currPath.col
            currSteps = currPath.steps

            # Up
            nextRow = currRow - 1
            nextCol = currCol

            if 0 <= nextRow \
            and (nextRow, nextCol) not in currPath.visited \
            and field[nextRow][nextCol] != '#':
            #and field[nextRow][nextCol] not in ['#', 'v']:
                currPath.makeStep(nextRow, nextCol)
                hasFirstRouteOption = True

            # Down
            nextRow = currRow + 1
            nextCol = currCol

            if nextRow < len(field) \
            and (nextRow, nextCol) not in currPath.visited \
            and field[nextRow][nextCol] != '#':
            #and field[nextRow][nextCol] not in ['#', '^']:
                if not hasFirstRouteOption:
                    currPath.makeStep(nextRow, nextCol)
                    hasFirstRouteOption = True
                else:
                    newPath = Path(currRow, currCol, currPath.visited, currSteps)
                    newPath.makeStep(nextRow, nextCol)
                    paths.append(newPath)

            # Right
            nextRow = currRow
            nextCol = currCol + 1

            if nextCol < len(field[nextRow]) \
            and (nextRow, nextCol) not in currPath.visited \
            and field[nextRow][nextCol] != '#':
            #and field[nextRow][nextCol] not in ['#', '<']:
                if not hasFirstRouteOption:
                    currPath.makeStep(nextRow, nextCol)
                    hasFirstRouteOption = True
                else:
                    newPath = Path(currRow, currCol, currPath.visited, currSteps)
                    newPath.makeStep(nextRow, nextCol)
                    paths.append(newPath)

            # Left
            nextRow = currRow
            nextCol = currCol - 1

            if 0 <= nextCol \
            and (nextRow, nextCol) not in currPath.visited \
            and field[nextRow][nextCol] != '#':
            #and field[nextRow][nextCol] not in ['#', '>']:
                if not hasFirstRouteOption:
                    currPath.makeStep(nextRow, nextCol)
                    hasFirstRouteOption = True
                else:
                    newPath = Path(currRow, currCol, currPath.visited, currSteps)
                    newPath.makeStep(nextRow, nextCol)
                    paths.append(newPath)

            if not hasFirstRouteOption:
                break
        else:
            endSteps.append(currPath.steps)

def solve23():
    f = open("input23.txt", "r")
    rawLines = f.readlines()

    field = []

    for rawLine in rawLines:
        field.append(rawLine.strip())

    endSteps = []
    paths = collections.deque()
    paths.append(Path(0, 1, set(), 0))
    followRoute(field, paths, endSteps)

    print(max(endSteps))

