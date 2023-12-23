heatLossLimit = 1171

def followRoute(field, cheapestRoute, currRow, currCol, dir, stepsInDir, heatLoss):
    global heatLossLimit

    if heatLossLimit <= heatLoss:
        return

    fieldLen = len(field)
    rowLen = len(field[0])

    if currRow == fieldLen - 1 and currCol == rowLen - 1:
        heatLossLimit = min(heatLoss, heatLossLimit)
        print(heatLossLimit)
        return

    moves = []

    if dir == 1:
        rightMove = None
        leftMove = None
        downMove = None

        nextRow = currRow
        nextCol = currCol + 1
        if nextCol < rowLen:
            rightMove = (2, nextRow, nextCol, field[nextRow][nextCol])

        nextCol = currCol - 1
        if 0 <= nextCol:
            leftMove = (3, nextRow, nextCol, field[nextRow][nextCol])

        if stepsInDir != 3:
            nextRow = currRow + 1
            nextCol = currCol
            if nextRow < fieldLen:
                downMove = (1, nextRow, nextCol, field[nextRow][nextCol])

        if downMove is not None:
            moves.append(downMove)
        if rightMove is not None:
            moves.append(rightMove)
        if leftMove is not None:
            moves.append(leftMove)

        #moves.sort(key=lambda m: m[3])

    elif dir == 0:
        rightMove = None
        leftMove = None
        upMove = None

        nextRow = currRow
        nextCol = currCol + 1
        if nextCol < rowLen:
            rightMove = (2, nextRow, nextCol, field[nextRow][nextCol])

        nextCol = currCol - 1
        if 0 <= nextCol:
            leftMove = (3, nextRow, nextCol, field[nextRow][nextCol])

        if stepsInDir != 3:
            nextRow = currRow - 1
            nextCol = currCol
            if 0 <= nextRow:
                upMove = (0, nextRow, nextCol, field[nextRow][nextCol])

        if rightMove is not None:
            moves.append(rightMove)
        if upMove is not None:
            moves.append(upMove)
        if leftMove is not None:
            moves.append(leftMove)

        #moves.sort(key=lambda m: m[3])

    elif dir == 2:
        downMove = None
        upMove = None
        rightMove = None

        nextRow = currRow + 1
        nextCol = currCol
        if nextRow < fieldLen:
            downMove = (1, nextRow, nextCol, field[nextRow][nextCol])

        nextRow = currRow - 1
        if 0 <= nextRow:
            upMove = (0, nextRow, nextCol, field[nextRow][nextCol])

        if stepsInDir != 3:
            nextRow = currRow
            nextCol = currCol + 1
            if nextCol < rowLen:
                rightMove = (2, nextRow, nextCol, field[nextRow][nextCol])

        if downMove is not None:
            moves.append(downMove)
        if rightMove is not None:
            moves.append(rightMove)
        if upMove is not None:
            moves.append(upMove)

        #moves.sort(key=lambda m: m[3])

    elif dir == 3:
        downMove = None
        upMove = None
        leftMove = None

        nextRow = currRow + 1
        nextCol = currCol
        if nextRow < fieldLen:
            downMove = (1, nextRow, nextCol, field[nextRow][nextCol])

        nextRow = currRow - 1
        if 0 <= nextRow:
            upMove = (0, nextRow, nextCol, field[nextRow][nextCol])

        if stepsInDir != 3:
            nextRow = currRow
            nextCol = currCol - 1
            if 0 <= nextCol:
                leftMove = (3, nextRow, nextCol, field[nextRow][nextCol])

        if downMove is not None:
            moves.append(downMove)
        if upMove is not None:
            moves.append(upMove)
        if leftMove is not None:
            moves.append(leftMove)

        #moves.sort(key=lambda m: m[3])

    #print(moves)

    for move in moves:
        nextRow = move[1]
        nextCol = move[2]
        nextDir = move[0]
        nextStepsInDir = 1 if nextDir != dir else stepsInDir + 1

        nextHeatLoss = heatLoss + move[3]
        if (cheapestRoute[nextRow][nextCol][nextDir] != 0 and
                cheapestRoute[nextRow][nextCol][nextDir] < nextHeatLoss):
            pass
        else:
            cheapestRoute[nextRow][nextCol][nextDir] = nextHeatLoss
            followRoute(field, cheapestRoute, nextRow, nextCol, nextDir, nextStepsInDir, nextHeatLoss)

def solve17():
    f = open("example17.txt", "r")
    rawLines = f.readlines()

    field = [[int(ch) for ch in line.strip()] for line in rawLines]
    # array of cheapest route per direction per pos: [u, d, r, l]
    cheapestRoute = [[[0, 0, 0, 0] for _ in line.strip()] for line in rawLines]

    #print(field)
    #print(cheapestRoute)

    followRoute(field, cheapestRoute, 0, 0, 2, 0, 0)

    # for route in cheapestRoute:
    #     print(route)
    print(cheapestRoute[-1][-1])

class PosInfo:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        # [up, down, right, left]
        self.minHL = [0, 0, 0, 0]
        self.stepsInDirs = [0, 0, 0, 0]
        self.done = [True, True, True, True]

    def __str__(self):
        return str(self.minHL) + ' ' + str(self.stepsInDirs) + ' ' + str(self.done)

    def updateHL(self, dirCode, stepsInDir, heatloss):
        if self.minHL[dirCode] == 0 or heatloss < self.minHL[dirCode]:
            self.minHL[dirCode] = heatloss
            self.stepsInDirs[dirCode] = stepsInDir
            self.done[dirCode] = False

    def getminHL(self):
        minHL = 0
        dir = 0
        stepsInDir = 0

        for i in range(4):
            if not self.done[i]:
                if minHL == 0 or self.minHL[i] < minHL:
                    minHL = self.minHL[i]
                    dir = i
                    stepsInDir = self.stepsInDirs[i]

        if minHL == 0:
            return None
        else:
            return minHL, dir, stepsInDir


def solve17_alt():
    f = open("example17.txt", "r")
    rawLines = f.readlines()

    field = [[int(ch) for ch in line.strip()] for line in rawLines]

    lastRow = len(field) - 1
    lastCol = len(field[0]) - 1
    currRow = 0
    currCol = 0

    currDir = 2
    currStepsInDir = 0

    posDict = {}

    for r in range(len(rawLines)):
        line = rawLines[r].strip()
        for c in range(len(line)):
            # row, col, minHeatLoss, lastDir, stepsInDir, visited, isRouteEnd
            posInfo = PosInfo(r, c)
            posDict[(r, c)] = posInfo

    print(posDict)

    while True:
        currPosInfo = posDict[(currRow, currCol)]
        currHL = currPosInfo.minHL[currDir]

        # Update current neighbours

        if currDir == 1:
            # Right
            nextRow = currRow
            nextCol = currCol + 1

            if nextCol <= lastCol:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]

                nextPosInfo.updateHL(2, 1, currHL + nextHeatLoss)

            # Left
            nextRow = currRow
            nextCol = currCol - 1

            if 0 <= nextCol:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]

                nextPosInfo.updateHL(3, 1, currHL + nextHeatLoss)

            if currStepsInDir != 3:
                # Down
                nextRow = currRow + 1
                nextCol = currCol

                if nextRow <= lastRow:
                    nextHeatLoss = field[nextRow][nextCol]
                    nextPosInfo = posDict[(nextRow, nextCol)]

                    nextPosInfo.updateHL(1, currStepsInDir + 1, currHL + nextHeatLoss)

        elif currDir == 0:
            # Right
            nextRow = currRow
            nextCol = currCol + 1

            if nextCol <= lastCol:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]

                nextPosInfo.updateHL(2, 1, currHL + nextHeatLoss)

            # Left
            nextRow = currRow
            nextCol = currCol - 1

            if 0 <= nextCol:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]

                nextPosInfo.updateHL(3, 1, currHL + nextHeatLoss)

            if currStepsInDir != 3:
                # Up
                nextRow = currRow - 1
                nextCol = currCol

                if 0 <= nextRow:
                    nextHeatLoss = field[nextRow][nextCol]
                    nextPosInfo = posDict[(nextRow, nextCol)]

                    nextPosInfo.updateHL(0, currStepsInDir + 1, currHL + nextHeatLoss)

        elif currDir == 2:
            # Up
            nextRow = currRow - 1
            nextCol = currCol

            if 0 <= nextRow:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]

                nextPosInfo.updateHL(0, 1, currHL + nextHeatLoss)

            # Down
            nextRow = currRow + 1
            nextCol = currCol

            if nextRow <= lastRow:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]

                nextPosInfo.updateHL(1, 1, currHL + nextHeatLoss)

            if currStepsInDir != 3:
                # Right
                nextRow = currRow
                nextCol = currCol + 1

                if nextCol <= lastCol:
                    nextHeatLoss = field[nextRow][nextCol]
                    nextPosInfo = posDict[(nextRow, nextCol)]

                    nextPosInfo.updateHL(2, currStepsInDir + 1, currHL + nextHeatLoss)

            elif currDir == 3:
                # Up
                nextRow = currRow - 1
                nextCol = currCol

                if 0 <= nextRow:
                    nextHeatLoss = field[nextRow][nextCol]
                    nextPosInfo = posDict[(nextRow, nextCol)]

                    nextPosInfo.updateHL(0, 1, currHL + nextHeatLoss)

                # Down
                nextRow = currRow + 1
                nextCol = currCol

                if nextRow <= lastRow:
                    nextHeatLoss = field[nextRow][nextCol]
                    nextPosInfo = posDict[(nextRow, nextCol)]

                    nextPosInfo.updateHL(1, 1, currHL + nextHeatLoss)

                if currStepsInDir != 3:
                    # Left
                    nextRow = currRow
                    nextCol = currCol - 1

                    if 0 <= nextCol:
                        nextHeatLoss = field[nextRow][nextCol]
                        nextPosInfo = posDict[(nextRow, nextCol)]

                        nextPosInfo.updateHL(3, currStepsInDir + 1, currHL + nextHeatLoss)

        #Find not visited element with smallest heatloss
        nextPosInfo = None
        nextPosMinHLInfo = None
        for posInfo in posDict.values():
            minHLInfo = posInfo.getminHL()
            if minHLInfo is not None:
                if nextPosInfo is None:
                    nextPosInfo = posInfo
                    nextPosMinHLInfo = minHLInfo
                else:
                    if minHLInfo[0] < nextPosMinHLInfo[0]:
                        nextPosInfo = posInfo
                        nextPosMinHLInfo = minHLInfo

        # Go to next pos
        if nextPosInfo is None:
            break
        else:
            currRow = nextPosInfo.row
            currCol = nextPosInfo.col
            currDir = nextPosMinHLInfo[1]
            currStepsInDir = nextPosMinHLInfo[2]
            nextPosInfo.done[currDir] = True

    print(posDict[(lastRow, lastCol)])
