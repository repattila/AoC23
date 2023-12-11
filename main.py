from threading import Thread

def solve1():
    f = open("input1.txt", "r")
    lines = f.readlines()

    numSum = 0
    lineCount = 0
    for line in lines:
        print(line)

        foundFirst = False
        firstDigit = '0'
        lastDigit = '0'
        lineLength = len(line) - 1
        currPos = 0

        while currPos != lineLength:
            foundDigit = ''

            if line[currPos] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                foundDigit = line[currPos]
            else:
                next3 = line[currPos:currPos + 3]
                if next3 == "one":
                    foundDigit = '1'
                elif next3 == "two":
                    foundDigit = '2'
                elif next3 == "six":
                    foundDigit = '6'
                else:
                    next4 = line[currPos:currPos + 4]
                    if next4 == "four":
                        foundDigit = '4'
                    elif next4 == "five":
                        foundDigit = '5'
                    elif next4 == "nine":
                        foundDigit = '9'
                    else:
                        next5 = line[currPos:currPos + 5]
                        if next5 == "three":
                            foundDigit = '3'
                        elif next5 == "seven":
                            foundDigit = '7'
                        elif next5 == "eight":
                            foundDigit = '8'

            if foundDigit != '':
                if foundFirst:
                    lastDigit = foundDigit
                else:
                    firstDigit = foundDigit
                    lastDigit = foundDigit
                    foundFirst = True

            currPos += 1

        num = int(firstDigit + lastDigit)
        print(num)

        numSum += num
        lineCount += 1

    print(numSum)
    print(lineCount)

def solve2():
    f = open("input2.txt", "r")
    lines = f.readlines()

    possibleGames = []
    powerSum = 0

    for line in lines:
        gameSplit = line.split(':')
        gameNum = int(gameSplit[0][5:])
        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        hands = gameSplit[1].split(';')
        for hand in hands:
            balls = hand.split(',')
            for ball in balls:
                ballSplit = ball.strip().split(' ')
                ballNum = int(ballSplit[0])
                ballType = ballSplit[1]
                if ballType == "red":
                    maxRed = max(maxRed, ballNum)
                elif ballType == "green":
                    maxGreen = max(maxGreen, ballNum)
                else:
                    maxBlue = max(maxBlue, ballNum)

        print(line)
        print(f"{gameNum}, {maxRed}, {maxGreen}, {maxBlue}")

        if maxRed <= 12 and maxGreen <= 13 and maxBlue <= 14:
            possibleGames.append(gameNum)

        powerSum += maxRed * maxGreen * maxBlue

    print(sum(possibleGames))
    print(powerSum)

def solve3():
    f = open("input3.txt", "r")
    lines = f.readlines()

    field = []

    for line in lines:
        row = []

        for char in line:
            row.append(char)

        field.append(row)

    numbers = []
    gears = {}

    rowsCount = len(field)

    for r in range(rowsCount):
        foundNumber = False
        numChars = ''
        enabledNumber = False
        rowLen = len(field[r])
        possibleGear = False
        gearPos = (0, 0)

        for c in range(rowLen):
            if field[r][c].isdigit():
                foundNumber = True
                numChars += field[r][c]

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        adjCharRow = min(max(r + i, 0), rowsCount - 1)
                        adjCharCol = min(max(c + j, 0), rowLen - 1)
                        adjChar = field[adjCharRow][adjCharCol]
                        if adjChar != '.' and adjChar != '\n' and not adjChar.isdigit():
                            enabledNumber = True

                            if adjChar == '*':
                                possibleGear = True
                                gearPos = (adjCharRow, adjCharCol)

            else:
                if foundNumber:
                    if enabledNumber:
                        numbers.append(int(numChars))
                        enabledNumber = False

                        if possibleGear:
                            if gearPos in gears:
                                gears[gearPos].append(int(numChars))
                            else:
                                gears[gearPos] = [int(numChars)]
                            possibleGear = False

                    foundNumber = False
                    numChars = ''

    print(numbers)
    print(sum(numbers))

    gearRatioSum = 0

    for pos, gear in gears.items():
        if len(gear) == 2:
            print(gear)

            gearRatioSum += gear[0] * gear[1]

    print(gearRatioSum)

def solve4_1():
    f = open("input4.txt", "r")
    lines = f.readlines()

    sum = 0

    for line in lines:
        print(line)

        numbers = line.split(':')[1].split('|')
        winingNums = [int(i) for i in numbers[0].strip().split(' ') if i != '']
        myNums = [int(i) for i in numbers[1].strip().split(' ') if i != '']
        winerNum = 0

        for num in myNums:
            if num in winingNums:
                print(num)
                winerNum += 1

        if winerNum != 0:
            sum += pow(2, winerNum - 1)

    print(sum)

class Card:
    def __init__(self, winningNums, myNums):
        self.winnerNum = 0

        for num in myNums:
            if num in winningNums:
                self.winnerNum += 1

    def __str__(self):
        return f"{self.winnerNum}"


def solve4_2():
    f = open("input4.txt", "r")
    lines = f.readlines()

    cards = [Card([], [])]
    myCards = []
    lineNum = 0

    for line in lines:
        lineNum += 1

        lineSplit = line.split(':')
        numbers = lineSplit[1].split('|')
        winningNums = [int(i) for i in numbers[0].strip().split(' ') if i != '']
        myNums = [int(i) for i in numbers[1].strip().split(' ') if i != '']

        cards.append(Card(winningNums, myNums))
        myCards.append(lineNum)

    for card in cards:
        print(card)
    print(len(cards))

    i = 0
    while i < len(myCards):
        print(len(myCards))

        currCard = myCards[i]
        currWinnerNum = cards[currCard].winnerNum
        if currWinnerNum != 0:
            for j in range(currCard + 1, currCard + 1 + currWinnerNum):
                myCards.append(j)

        i += 1

    print(len(myCards))

class Range():
    def __init__(self, start, end, length):
        self.start = start
        self.end = start + length - 1 if end == -1 else end

    def __str__(self):
        return f"{self.start},{self.end}"

    def __lt__(self, other):
        return self.start < other.start

    def hasOverlap(self, other):
        return ((self.start <= other.start and other.start <= self.end) or
                (self.start <= other.end and other.end <= self.end))

    def intersect(self, other):
        if self.hasOverlap(other):
            intersectStart = -1
            intersectEnd = -1
            remain1Start = -1
            remain1End = -1
            remain2Start = -1
            remain2End = -1
            if self.start <= other.start:
                intersectStart = other.start
            else:
                intersectStart = self.start
                remain1Start = other.start
                remain1End = self.start - 1

            if other.end <= self.end:
                intersectEnd = other.end
            else:
                intersectEnd = self.end
                remain2Start = self.end + 1
                remain2End = other.end

            return(Range(intersectStart, intersectEnd, -1),
                   None if remain1Start == -1 else Range(remain1Start, remain1End, -1),
                   None if remain2Start == -1 else Range(remain2Start, remain2End, -1))
        else:
            return (None, other, None)

class Conversion:
    def __init__(self, destRangeStart, sourceRangeStart, rangeLength):
        self.sourceRange = Range(int(sourceRangeStart), -1, int(rangeLength))
        self.conversionDif = int(destRangeStart) - int(sourceRangeStart)
        self.rangeLength = int(rangeLength)

    def __str__(self):
        return(f"{self.sourceRange}({self.rangeLength})({self.conversionDif})")

    def __lt__(self, other):
        return self.sourceRange.start < other.sourceRange.start

    def convert(self, source):
        (intersection, prev, after) = self.sourceRange.intersect(source)

        if intersection is not None:
            intersection.start += self.conversionDif
            intersection.end += self.conversionDif

        return (intersection, prev, after)

def solve5():
    f = open("input5.txt", "r")
    lines = f.readlines()

    seeds = []
    conversions = []

    c = -1
    for line in lines:
        if line.startswith("seeds:"):
            #seeds += [Range(int(s), -1, 1) for s in line[7:].strip().split(' ')]

            seedsSplit = [int(s) for s in line[7:].strip().split(' ')]
            for i in range(0, len(seedsSplit), 2):
                seeds.append(Range(seedsSplit[i], -1, seedsSplit[i + 1]))
        elif line.strip() in ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]:
            conversions.append([])
            c += 1
        elif line.startswith("\n"):
            pass
        else:
            convParams = line.strip().split(' ')
            conversions[c].append(Conversion(convParams[0], convParams[1], convParams[2]))

    for typeConvs in conversions:
        typeConvs.sort()
        for conv in typeConvs:
            print(conv)
        print()

    for seed in seeds:
        print(seed)
    print()

    for typeConvs in conversions:
        s = 0
        while s < len(seeds):
            for conv in typeConvs:
                (intersection, prev, after) = conv.convert(seeds[s])

                if intersection is not None:
                    seeds[s] = intersection

                    if prev is not None:
                        seeds.append(prev)
                    if after is not None:
                        seeds.append(after)

                    break

            s += 1

    seeds.sort()
    for seed in seeds:
        print(seed)

def solve6():
    times = [46, 80, 78, 66]
    distances = [214, 1177, 1402, 1024]
    res = 1

    for i in range(4):
        time = times[i]
        winnerOptions = 0

        for t in range(time):
            dist = (time - t) * t
            if distances[i] < dist:
                winnerOptions += 1

        res *= winnerOptions

    print(res)

def solve6_2():
    time = 46807866
    distance = 214117714021024

    winnerOptions = 0

    for t in range(time):
        dist = (time - t) * t
        if distance < dist:
            winnerOptions += 1

    print(winnerOptions)

orderOfCards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

        matchingCards = []
        matchingCardsNums = []
        jokers = 0
        for i in range(len(cards)):
            if cards[i] == 'J':
                jokers += 1
            elif not cards[i] in matchingCards:
                matchingCardsNum = 1
                for j in range(len(cards)):
                    if i != j and cards[j] == cards[i]:
                        matchingCardsNum += 1

                if 1 < matchingCardsNum:
                    matchingCards.append(cards[i])
                    matchingCardsNums.append(matchingCardsNum)

        if len(matchingCards) == 0:
            if jokers == 0:
                self.type = 1
            elif jokers == 1:
                self.type = 2
            elif jokers == 2:
                self.type = 4
            elif jokers == 3:
                self.type = 6
            elif jokers == 4 or jokers == 5:
                self.type = 7
        elif len(matchingCards) == 1:
            if matchingCardsNums[0] == 2:
                if jokers == 0:
                    self.type = 2
                elif jokers == 1:
                    self.type = 4
                elif jokers == 2:
                    self.type = 6
                elif jokers == 3:
                    self.type = 7
            elif matchingCardsNums[0] == 3:
                if jokers == 0:
                    self.type = 4
                elif jokers == 1:
                    self.type = 6
                elif jokers == 2:
                    self.type = 7
            elif matchingCardsNums[0] == 4:
                if jokers == 0:
                    self.type = 6
                elif jokers == 1:
                    self.type = 7
            elif matchingCardsNums[0] == 5:
                self.type = 7
        elif len(matchingCards) == 2:
            if matchingCardsNums[0] == 2 and matchingCardsNums[1] == 2:
                if jokers == 0:
                    self.type = 3
                elif jokers == 1:
                    self.type = 5
            else:
                self.type = 5

    def __str__(self):
        return f"{self.cards}({self.type})({self.bid})"

    def __lt__(self, other):
        if self.type == other.type:
            for i in range(len(self.cards)):
                orderofMyCard = orderOfCards.index(self.cards[i])
                orderOfOthersCard = orderOfCards.index(other.cards[i])
                if orderofMyCard == orderOfOthersCard:
                    continue
                else:
                    return orderofMyCard < orderOfOthersCard

            return False
        else:
            return self.type < other.type
def solve7():
    f = open("input7.txt", "r")
    lines = f.readlines()

    hands = []

    for line in lines:
        lineSplit = line.split(' ')
        hands.append(Hand(lineSplit[0], int(lineSplit[1])))

    hands.sort()

    sumOfBids = 0

    for i in range(len(hands)):
        print(hands[i])

        sumOfBids += hands[i].bid * (i + 1)

    print(sumOfBids)

def solve8(start, end):
    f = open("input8.txt", "r")
    lines = f.readlines()

    currPlace = start
    stepCount = 0
    insts = lines[0].strip()
    map = {}

    for l in range(2, len(lines)):
        splitLine = lines[l].strip().split('=')
        splitLF = splitLine[1][2: -1].split(', ')
        map[splitLine[0].strip()] = (splitLF[0], splitLF[1])

    print(map)

    while True:
        for inst in insts:
            if stepCount != 0 and currPlace == end:
                break
            else:
                stepCount += 1
                if inst == 'L':
                    currPlace = map[currPlace][0]
                elif inst == 'R':
                    currPlace = map[currPlace][1]
        else:
            continue

        break

    print(stepCount)

def navigate(places, placeNum, insts: str, map):

    currPlace = places[placeNum][0]

    stepCount = places[placeNum][1]
    startStep = places[placeNum][1]

    currInst = places[placeNum][2]
    enabled = places[placeNum][3]

    if not enabled:
        return

    while True:
        if stepCount != startStep and currPlace[2] == 'Z':
            places[placeNum] = (currPlace, stepCount, currInst, False)
            break
        else:
            inst = insts[currInst]
            if inst == 'L':
                currPlace = map[currPlace][0]
            elif inst == 'R':
                currPlace = map[currPlace][1]

            stepCount += 1
            currInst += 1
            if currInst == len(insts):
                currInst = 0

def solve8_2_bruteforce():
    f = open("input8.txt", "r")
    lines = f.readlines()

    currPlaces = []
    insts = lines[0].strip()
    map = {}

    for l in range(2, len(lines)):
        splitLine = lines[l].strip().split('=')
        splitLF = splitLine[1][2: -1].split(', ')
        map[splitLine[0].strip()] = (splitLF[0], splitLF[1])

    print(map)

    for place in map.keys():
        if place[-1] == 'A':
            currPlaces.append((place, 0, 0, True))

    print(currPlaces)

    while True:
        threads = []

        for p in range(len(currPlaces)):
            newThread = Thread(target=navigate, args=(currPlaces, p, insts, map))
            newThread.start()
            threads.append(newThread)

        for thread in threads:
            thread.join()

        highestStepCount = currPlaces[0][1]
        for currPlace in currPlaces:
            if highestStepCount < currPlace[1]:
                highestStepCount = currPlace[1]

        isAllOnEnd = True
        for p in range(len(currPlaces)):
            if currPlaces[p][1] != highestStepCount:
                isAllOnEnd = False

            if currPlaces[p][1] != highestStepCount:
                currPlaces[p] = (currPlaces[p][0], currPlaces[p][1], currPlaces[p][2], True)

        print(currPlaces)
        print(highestStepCount)

        if isAllOnEnd:
            break

def solve8_2():
    f = open("input8.txt", "r")
    lines = f.readlines()

    starts = []
    ends = []
    insts = lines[0].strip()
    map = {}

    for l in range(2, len(lines)):
        splitLine = lines[l].strip().split('=')
        splitLF = splitLine[1][2: -1].split(', ')
        map[splitLine[0].strip()] = (splitLF[0], splitLF[1])


    for place in map.keys():
        if place[-1] == 'A':
            starts.append(place)

    print(starts)

def getDiffSeries(series: list):
    res = []
    allZero = True
    for i in range(len(series) - 1):
        diff = series[i + 1] - series[i]
        res.append(diff)

        if diff != 0:
            allZero = False

    return (allZero, res)

def solve9():
    f = open("input9.txt", "r")
    lines = f.readlines()

    data = [[int(i) for i in l.strip().split(' ')] for l in lines]
    sumPred = 0
    sumBack = 0

    for series in data:
        diffs = []
        base = series
        while True:
            diff = getDiffSeries(base)
            diffs.append(diff[1])

            if diff[0]:
                break
            else:
                base = diff[1]

        pred = 0
        for d in range(len(diffs) - 2, -1, -1):
            pred += diffs[d][-1]

        back = 0
        for d in range(len(diffs) - 2, -1, -1):
            back = diffs[d][0] - back

        sumPred += series[-1] + pred
        sumBack += series[0] - back

        print(diffs)
        print(pred)
        print(back)

    print(sumPred)
    print(sumBack)

def solve10():
    f = open("input10.txt", "r")
    rawLines = f.readlines()

    startLine = 0
    startCol = 0
    linesLen = len(rawLines)
    lineLen = 0

    lines = []
    field = []

    # Find S, prepare lines array and fill field array with all 0
    for l in range(linesLen):
        rawLine = rawLines[l]
        lineLen = len(rawLine) - 1

        line = []
        lines.append(line)

        row = []
        field.append(row)

        for c in range(lineLen):
            line.append(rawLine[c])
            row.append(0)

            if rawLine[c] == 'S':
                startLine = l
                startCol = c

    currLine = startLine
    currCol = startCol
    currElem = 'S'
    prevLine = startLine
    prevCol = startCol
    stepCount = 0
    firstDirAfterS = ''
    lastDir = ''

    # Navigate the pipe, mark pipe segments with 1 on field
    while stepCount == 0 or currLine != startLine or currCol != startCol:
        print(f"({currLine})({currCol}) {currElem}")
        field[currLine][currCol] = 1

        if currElem == 'S':
            nextCol = currCol + 1
            if nextCol != prevCol and nextCol < lineLen:
                nextElem = lines[currLine][nextCol]
                if nextElem in ['-', 'J', '7']:
                    prevLine = currLine
                    prevCol = currCol

                    currCol = nextCol
                    currElem = nextElem
                    stepCount += 1
                    firstDirAfterS = 'E'
                    continue

            nextCol = currCol - 1
            if nextCol != prevCol and 0 <= nextCol:
                nextElem = lines[currLine][nextCol]
                if nextElem in ['-', 'L', 'F']:
                    prevLine = currLine
                    prevCol = currCol

                    currCol = nextCol
                    currElem = nextElem
                    stepCount += 1
                    firstDirAfterS = 'W'
                    continue

            nextLine = currLine + 1
            if nextLine != prevLine and nextLine < linesLen:
                nextElem = lines[nextLine][currCol]
                if nextElem in ['|', 'J', 'L']:
                    prevLine = currLine
                    prevCol = currCol

                    currLine = nextLine
                    currElem = nextElem
                    stepCount += 1
                    firstDirAfterS = 'S'
                    continue

            nextLine = currLine - 1
            if nextLine != prevLine and 0 <= nextLine:
                nextElem = lines[nextLine][currCol]
                if nextElem in ['|', 'F', '7']:
                    prevLine = currLine
                    prevCol = currCol

                    currLine = nextLine
                    currElem = nextElem
                    stepCount += 1
                    firstDirAfterS = 'N'
                    continue
        elif currElem == '|':
            nextLine = currLine + 1
            if nextLine != prevLine and nextLine < linesLen:
                nextElem = lines[nextLine][currCol]
                if nextElem in ['|', 'J', 'L', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currLine = nextLine
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'S'
                    continue

            nextLine = currLine - 1
            if nextLine != prevLine and 0 <= nextLine:
                nextElem = lines[nextLine][currCol]
                if nextElem in ['|', 'F', '7', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currLine = nextLine
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'N'
                    continue
        elif currElem == '-':
            nextCol = currCol + 1
            if nextCol != prevCol and nextCol < lineLen:
                nextElem = lines[currLine][nextCol]
                if nextElem in ['-', 'J', '7', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currCol = nextCol
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'E'
                    continue

            nextCol = currCol - 1
            if nextCol != prevCol and 0 <= nextCol:
                nextElem = lines[currLine][nextCol]
                if nextElem in ['-', 'L', 'F', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currCol = nextCol
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'W'
                    continue
        elif currElem == 'J':
            nextLine = currLine - 1
            if nextLine != prevLine and 0 <= nextLine:
                nextElem = lines[nextLine][currCol]
                if nextElem in ['|', 'F', '7', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currLine = nextLine
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'N'
                    continue

            nextCol = currCol - 1
            if nextCol != prevCol and 0 <= nextCol:
                nextElem = lines[currLine][nextCol]
                if nextElem in ['-', 'L', 'F', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currCol = nextCol
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'W'
                    continue
        elif currElem == 'L':
            nextLine = currLine - 1
            if nextLine != prevLine and 0 <= nextLine:
                nextElem = lines[nextLine][currCol]
                if nextElem in ['|', 'F', '7', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currLine = nextLine
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'N'
                    continue

            nextCol = currCol + 1
            if nextCol != prevCol and nextCol < lineLen:
                nextElem = lines[currLine][nextCol]
                if nextElem in ['-', 'J', '7', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currCol = nextCol
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'E'
                    continue
        elif currElem == 'F':
            nextLine = currLine + 1
            if nextLine != prevLine and nextLine < linesLen:
                nextElem = lines[nextLine][currCol]
                if nextElem in ['|', 'J', 'L', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currLine = nextLine
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'S'
                    continue

            nextCol = currCol + 1
            if nextCol != prevCol and nextCol < lineLen:
                nextElem = lines[currLine][nextCol]
                if nextElem in ['-', 'J', '7', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currCol = nextCol
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'E'
                    continue
        elif currElem == '7':
            nextLine = currLine + 1
            if nextLine != prevLine and nextLine < linesLen:
                nextElem = lines[nextLine][currCol]
                if nextElem in ['|', 'J', 'L', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currLine = nextLine
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'S'
                    continue

            nextCol = currCol - 1
            if nextCol != prevCol and 0 <= nextCol:
                nextElem = lines[currLine][nextCol]
                if nextElem in ['-', 'L', 'F', 'S']:
                    prevLine = currLine
                    prevCol = currCol

                    currCol = nextCol
                    currElem = nextElem
                    stepCount += 1
                    lastDir = 'W'
                    continue

    print(stepCount)

    # Replace S with actual element
    if (firstDirAfterS == 'N' and lastDir == 'N') or (firstDirAfterS == 'S' and lastDir == 'S'):
        lines[startLine][startCol] = '|'
    elif (firstDirAfterS == 'E' and lastDir == 'E') or (firstDirAfterS == 'W' and lastDir == 'W'):
        lines[startLine][startCol] = '-'
    elif (firstDirAfterS == 'N' and lastDir == 'E') or (firstDirAfterS == 'W' and lastDir == 'S'):
        lines[startLine][startCol] = 'J'
    elif (firstDirAfterS == 'N' and lastDir == 'W') or (firstDirAfterS == 'E' and lastDir == 'S'):
        lines[startLine][startCol] = 'L'
    elif (firstDirAfterS == 'S' and lastDir == 'E') or (firstDirAfterS == 'W' and lastDir == 'N'):
        lines[startLine][startCol] = '7'
    elif (firstDirAfterS == 'S' and lastDir == 'W') or (firstDirAfterS == 'E' and lastDir == 'N'):
        lines[startLine][startCol] = 'F'

    # Check in or out
    for r in range(len(field)):
        prevBend = ''
        crossCount = 0
        row = field[r]
        for c in range(len(row)):
            if row[c] == 0:
                if crossCount % 2 == 1:
                    row[c] = 2
            elif row[c] == 1:
                currElem = lines[r][c]
                if currElem in ['|', 'L', 'F']:
                    crossCount += 1
                elif currElem == '7':
                    if not prevBend in ['L']:
                        crossCount += 1
                elif currElem == 'J':
                    if not prevBend in ['F']:
                        crossCount += 1

                if currElem in ['L', 'F', '7', 'J']:
                    prevBend = currElem

    insideCount = 0
    for row in field:
        for col in row:
            print(col, end='')
            if col == 2:
                insideCount += 1
        print()

    print(insideCount)

def solve11():
    f = open("input11.txt", "r")
    lines = f.readlines()

    expandRows = []
    for r in range(len(lines)):
        isEmpty = True
        for col in lines[r].strip():
            if col != '.':
                isEmpty = False
                break

        if isEmpty:
            expandRows.append(r)

    print(expandRows)

    expandCols = []
    for c in range(len(lines[0])):
        isEmpty = True
        for row in lines:
            if row[c] != '.':
                isEmpty = False
                break

        if isEmpty:
            expandCols.append(c)

    print(expandCols)

    galaxies = {}

    galaxyNum = 0
    for r in range(len(lines)):
        row = lines[r]
        for c in range(len(row)):
            if row[c] == '#':
                galaxies[galaxyNum] = (r, c)
                galaxyNum += 1

    print(galaxies)

    sumRanges = 0

    keys = galaxies.keys()
    for k in range(len(keys)):
        for ok in range(k + 1, len(keys)):
            #print(f"{k} {ok}")

            thisRow = galaxies[k][0]
            thisCol = galaxies[k][1]
            thatRow = galaxies[ok][0]
            thatCol = galaxies[ok][1]
            minRow = min(thisRow, thatRow)
            maxRow = max(thisRow, thatRow)
            minCol = min(thisCol, thatCol)
            maxCol = max(thisCol, thatCol)
            rowsBetween = 0
            colsBetween = 0
            for row in expandRows:
                if minRow < row and row < maxRow:
                    rowsBetween += 1

            for col in expandCols:
                if minCol < col and col < maxCol:
                    colsBetween += 1

            ran = abs(thatRow - thisRow) + abs(thatCol - thisCol) + (rowsBetween * (1000000 - 1)) + (colsBetween * (1000000 - 1))
            # print(ran)
            sumRanges += ran

    print(sumRanges)


import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.setrecursionlimit(20000)
    solve10()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
