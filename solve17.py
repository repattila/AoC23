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

def solve17_alt():
    f = open("example17.txt", "r")
    rawLines = f.readlines()

    field = [[int(ch) for ch in line.strip()] for line in rawLines]

    lastRow = len(field) - 1
    lastCol = len(field[0]) - 1
    currRow = 0
    currCol = 0

    posDict = {}
    cheapestRouteEnds = []
    for r in range(len(rawLines)):
        line = rawLines[r].strip()
        for c in range(len(line)):
            # row, col, minHeatLoss, lastDir, stepsInDir, visited, isRouteEnd
            posInfo = [r, c, 0, 'r', 0, False, False]
            posDict[(r, c)] = posInfo

    print(posDict)

    while True:
        currPosInfo = posDict[(currRow, currCol)]
        currCost = currPosInfo[2]

        # Update current neighbours

        if currPosInfo[3] == 'd':
            # Right
            nextRow = currRow
            nextCol = currCol + 1

            if nextCol <= lastCol:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]
                nextCost = nextPosInfo[2]

                if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                    nextPosInfo[2] = currCost + nextHeatLoss
                    nextPosInfo[3] = 'r'
                    nextPosInfo[4] = 1
                    nextPosInfo[5] = False

                    if not nextPosInfo[6]:
                        nextPosInfo[6] = True
                        cheapestRouteEnds.append(nextPosInfo)

            # Left
            nextRow = currRow
            nextCol = currCol - 1

            if 0 <= nextCol:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]
                nextCost = nextPosInfo[2]

                if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                    nextPosInfo[2] = currCost + nextHeatLoss
                    nextPosInfo[3] = 'l'
                    nextPosInfo[4] = 1
                    nextPosInfo[5] = False

                    if not nextPosInfo[6]:
                        nextPosInfo[6] = True
                        cheapestRouteEnds.append(nextPosInfo)

            if currPosInfo[4] != 3:
                # Down
                nextRow = currRow + 1
                nextCol = currCol

                if nextRow <= lastRow:
                    nextHeatLoss = field[nextRow][nextCol]
                    nextPosInfo = posDict[(nextRow, nextCol)]
                    nextCost = nextPosInfo[2]

                    if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                        nextPosInfo[2] = currCost + nextHeatLoss
                        nextPosInfo[3] = 'd'
                        nextPosInfo[4] = currPosInfo[4] + 1
                        nextPosInfo[5] = False

                        if not nextPosInfo[6]:
                            nextPosInfo[6] = True
                            cheapestRouteEnds.append(nextPosInfo)

        elif currPosInfo[3] == 'u':
            # Right
            nextRow = currRow
            nextCol = currCol + 1

            if nextCol <= lastCol:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]
                nextCost = nextPosInfo[2]

                if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                    nextPosInfo[2] = currCost + nextHeatLoss
                    nextPosInfo[3] = 'r'
                    nextPosInfo[4] = 1
                    nextPosInfo[5] = False

                    if not nextPosInfo[6]:
                        nextPosInfo[6] = True
                        cheapestRouteEnds.append(nextPosInfo)

            # Left
            nextRow = currRow
            nextCol = currCol - 1

            if 0 <= nextCol:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]
                nextCost = nextPosInfo[2]

                if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                    nextPosInfo[2] = currCost + nextHeatLoss
                    nextPosInfo[3] = 'l'
                    nextPosInfo[4] = 1
                    nextPosInfo[5] = False

                    if not nextPosInfo[6]:
                        nextPosInfo[6] = True
                        cheapestRouteEnds.append(nextPosInfo)

            if currPosInfo[4] != 3:
                # Up
                nextRow = currRow - 1
                nextCol = currCol

                if 0 <= nextRow:
                    nextHeatLoss = field[nextRow][nextCol]
                    nextPosInfo = posDict[(nextRow, nextCol)]
                    nextCost = nextPosInfo[2]

                    if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                        nextPosInfo[2] = currCost + nextHeatLoss
                        nextPosInfo[3] = 'u'
                        nextPosInfo[4] = currPosInfo[4] + 1
                        nextPosInfo[5] = False

                        if not nextPosInfo[6]:
                            nextPosInfo[6] = True
                            cheapestRouteEnds.append(nextPosInfo)

        elif currPosInfo[3] == 'r':
            # Up
            nextRow = currRow - 1
            nextCol = currCol

            if 0 <= nextRow:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]
                nextCost = nextPosInfo[2]

                if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                    nextPosInfo[2] = currCost + nextHeatLoss
                    nextPosInfo[3] = 'u'
                    nextPosInfo[4] = 1
                    nextPosInfo[5] = False

                    if not nextPosInfo[6]:
                        nextPosInfo[6] = True
                        cheapestRouteEnds.append(nextPosInfo)

            # Down
            nextRow = currRow + 1
            nextCol = currCol

            if nextRow <= lastRow:
                nextHeatLoss = field[nextRow][nextCol]
                nextPosInfo = posDict[(nextRow, nextCol)]
                nextCost = nextPosInfo[2]

                if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                    nextPosInfo[2] = currCost + nextHeatLoss
                    nextPosInfo[3] = 'd'
                    nextPosInfo[4] = 1
                    nextPosInfo[5] = False

                    if not nextPosInfo[6]:
                        nextPosInfo[6] = True
                        cheapestRouteEnds.append(nextPosInfo)

            if currPosInfo[4] != 3:
                # Right
                nextRow = currRow
                nextCol = currCol + 1

                if nextCol <= lastCol:
                    nextHeatLoss = field[nextRow][nextCol]
                    nextPosInfo = posDict[(nextRow, nextCol)]
                    nextCost = nextPosInfo[2]

                    if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                        nextPosInfo[2] = currCost + nextHeatLoss
                        nextPosInfo[3] = 'r'
                        nextPosInfo[4] = currPosInfo[4] + 1
                        nextPosInfo[5] = False

                        if not nextPosInfo[6]:
                            nextPosInfo[6] = True
                            cheapestRouteEnds.append(nextPosInfo)

            elif currPosInfo[3] == 'l':
                # Up
                nextRow = currRow - 1
                nextCol = currCol

                if 0 <= nextRow:
                    nextHeatLoss = field[nextRow][nextCol]
                    nextPosInfo = posDict[(nextRow, nextCol)]
                    nextCost = nextPosInfo[2]

                    if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                        nextPosInfo[2] = currCost + nextHeatLoss
                        nextPosInfo[3] = 'u'
                        nextPosInfo[4] = 1
                        nextPosInfo[5] = False

                        if not nextPosInfo[6]:
                            nextPosInfo[6] = True
                            cheapestRouteEnds.append(nextPosInfo)

                # Down
                nextRow = currRow + 1
                nextCol = currCol

                if nextRow <= lastRow:
                    nextHeatLoss = field[nextRow][nextCol]
                    nextPosInfo = posDict[(nextRow, nextCol)]
                    nextCost = nextPosInfo[2]

                    if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                        nextPosInfo[2] = currCost + nextHeatLoss
                        nextPosInfo[3] = 'd'
                        nextPosInfo[4] = 1
                        nextPosInfo[5] = False

                        if not nextPosInfo[6]:
                            nextPosInfo[6] = True
                            cheapestRouteEnds.append(nextPosInfo)

                if currPosInfo[4] != 3:
                    # Left
                    nextRow = currRow
                    nextCol = currCol - 1

                    if 0 <= nextCol:
                        nextHeatLoss = field[nextRow][nextCol]
                        nextPosInfo = posDict[(nextRow, nextCol)]
                        nextCost = nextPosInfo[2]

                        if nextCost == 0 or currCost + nextHeatLoss <= nextCost:
                            nextPosInfo[2] = currCost + nextHeatLoss
                            nextPosInfo[3] = 'l'
                            nextPosInfo[4] = currPosInfo[4] + 1
                            nextPosInfo[5] = False

                            if not nextPosInfo[6]:
                                nextPosInfo[6] = True
                                cheapestRouteEnds.append(nextPosInfo)

        #Find not visited element with smallest heatloss
        nextPosInfo = None
        for posInfo in posDict.values():
            if not posInfo[5] and posInfo[2] != 0:
                if nextPosInfo is None:
                    nextPosInfo = posInfo
                else:
                    if posInfo[2] < nextPosInfo[2]:
                        nextPosInfo = posInfo

        # Go to next pos
        if nextPosInfo is None:
            break
        else:
            currRow = nextPosInfo[0]
            currCol = nextPosInfo[1]
            nextPosInfo[5] = True

    print(posDict[(lastRow, lastCol)])
