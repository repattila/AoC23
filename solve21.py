def solve21():
    f = open("examples/example21.txt", "r")
    rawLines = f.readlines()

    field = []
    currReachables: set

    for r in range(len(rawLines)):
        rawLine = rawLines[r]
        field.append(rawLine.strip())

        sPos = rawLine.find('S')
        if sPos != -1:
            currReachables = {(r, sPos)}

    fieldLen = len(field)
    rowLen = len(field[0])
    evenReachableCount = 1
    oddReachableCount = 0
    prevReachables = currReachables
    stepsCount = 0
    while stepsCount != 26501365:
    #while stepsCount != 5000:
        stepsCount += 1
        newReachables = set()
        for reachable in currReachables:
            currRow = reachable[0]
            currCol = reachable[1]
            for nextRow, nextCol in [(currRow + 1, currCol), (currRow - 1, currCol),
                                     (currRow, currCol + 1), (currRow, currCol - 1)]:
                if (nextRow, nextCol) not in prevReachables:
                    mappedNextRow = nextRow % fieldLen
                    mappedNextCol = nextCol % rowLen

                    if field[mappedNextRow][mappedNextCol] != '#':
                        newReachables.add((nextRow, nextCol))

        prevReachables = currReachables
        currReachables = newReachables

        if stepsCount % 2 == 0:
            evenReachableCount += len(newReachables)
        else:
            oddReachableCount += len(newReachables)

        print(stepsCount)

    if stepsCount % 2 == 0:
        print(evenReachableCount)
    else:
        print(oddReachableCount)
