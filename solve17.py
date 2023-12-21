heatLossLimit = 1171

def followRoute(field, cheapestRoute, currRow, currCol, dir, stepsInDir, heatLoss):
    global heatLossLimit

    if heatLossLimit <= heatLoss:
        return

    endRow = len(field) - 1
    endCol = len(field[currRow]) - 1

    if currRow == endRow and currCol == endCol:
        heatLossLimit = min(heatLoss, heatLossLimit)
        print(heatLossLimit)
        return

    moveDown = False
    moveLeft = False
    moveRight = False
    moveUp = False

    if dir == 'd':
        if stepsInDir == 3:
            moveLeft = True
            moveRight = True
        else:
            moveLeft = True
            moveRight = True
            moveDown = True
    elif dir == 'u':
        if stepsInDir == 3:
            moveLeft = True
            moveRight = True
        else:
            moveLeft = True
            moveRight = True
            moveUp = True
    elif dir == 'r':
        if stepsInDir == 3:
            moveDown = True
            moveUp = True
        else:
            moveDown = True
            moveUp = True
            moveRight = True
    elif dir == 'l':
        if stepsInDir == 3:
            moveDown = True
            moveUp = True
        else:
            moveDown = True
            moveUp = True
            moveLeft = True

    if moveDown:
        nextRow = currRow + 1
        nextCol = currCol

        if nextRow == endRow and nextCol == endCol:
            moveUp = False
            moveRight = False
            moveLeft = False

    if moveRight:
        nextRow = currRow
        nextCol = currCol + 1

        if nextRow == endRow and nextCol == endCol:
            moveUp = False
            moveDown = False
            moveLeft = False

    if moveDown:
        nextRow = currRow + 1
        nextCol = currCol
        nextDir = 'd'
        nextStepsInDir = 1 if nextDir != dir else stepsInDir + 1

        if nextRow < len(field):
            nextHeatLoss = heatLoss + field[nextRow][nextCol]
            if cheapestRoute[nextRow][nextCol][1] != 0 and cheapestRoute[nextRow][nextCol][1] < nextHeatLoss:
                pass
            else:
                cheapestRoute[nextRow][nextCol][1] = nextHeatLoss
                followRoute(field, cheapestRoute, nextRow, nextCol, nextDir, nextStepsInDir, nextHeatLoss)

    if moveRight:
        nextRow = currRow
        nextCol = currCol + 1
        nextDir = 'r'
        nextStepsInDir = 1 if nextDir != dir else stepsInDir + 1

        if nextCol < len(field[nextRow]):
            nextHeatLoss = heatLoss + field[nextRow][nextCol]
            if cheapestRoute[nextRow][nextCol][2] != 0 and cheapestRoute[nextRow][nextCol][2] < nextHeatLoss:
                pass
            else:
                cheapestRoute[nextRow][nextCol][2] = nextHeatLoss
                followRoute(field, cheapestRoute, nextRow, nextCol, nextDir, nextStepsInDir, nextHeatLoss)

    if moveLeft:
        nextRow = currRow
        nextCol = currCol - 1
        nextDir = 'l'
        nextStepsInDir = 1 if nextDir != dir else stepsInDir + 1

        if 0 <= nextCol:
            nextHeatLoss = heatLoss + field[nextRow][nextCol]
            if cheapestRoute[nextRow][nextCol][3] != 0 and cheapestRoute[nextRow][nextCol][3] < nextHeatLoss:
                pass
            else:
                cheapestRoute[nextRow][nextCol][3] = nextHeatLoss
                followRoute(field, cheapestRoute, nextRow, nextCol, nextDir, nextStepsInDir, nextHeatLoss)

    if moveUp:
        nextRow = currRow - 1
        nextCol = currCol
        nextDir = 'u'
        nextStepsInDir = 1 if nextDir != dir else stepsInDir + 1

        if 0 <= nextRow:
            nextHeatLoss = heatLoss + field[nextRow][nextCol]
            if cheapestRoute[nextRow][nextCol][0] != 0 and cheapestRoute[nextRow][nextCol][0] < nextHeatLoss:
                pass
            else:
                cheapestRoute[nextRow][nextCol][0] = nextHeatLoss
                followRoute(field, cheapestRoute, nextRow, nextCol, nextDir, nextStepsInDir, nextHeatLoss)

def solve17():
    f = open("input17.txt", "r")
    rawLines = f.readlines()

    field = [[int(ch) for ch in line.strip()] for line in rawLines]
    # array of cheapest route per direction per pos: [u, d, r, l]
    cheapestRoute = [[[0, 0, 0, 0] for _ in line.strip()] for line in rawLines]

    #print(field)
    #print(cheapestRoute)

    followRoute(field, cheapestRoute, 0, 0, 'r', 0, 0)

    print(cheapestRoute[-1][-1])
