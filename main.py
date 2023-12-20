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

# https://mathoverflow.net/questions/9477/uniquely-generate-all-permutations-of-three-digits-that-sum-to-a-particular-valu
def multichoose(n,k):
    if k < 0 or n < 0: return "Error"
    if not k: return [[0]*n]
    if not n: return []
    if n == 1: return [[k]]
    return [[0]+val for val in multichoose(n-1,k)] + \
        [[val[0]+1]+val[1:] for val in multichoose(n,k-1)]

def solve12_bruteforce():
    f = open("input12.txt", "r")
    rawLines = f.readlines()

    lines = []
    checkSums = []

    for rawLine in rawLines:
        splitLine = rawLine.strip().split(' ')
        lines.append(splitLine[0])
        checkSums.append([int(c) for c in splitLine[1].split(',')])

    print(lines)
    print(checkSums)

    fittingArrangementsCounts = []

    for i in range(len(lines)):
        currLine = lines[i]
        currCheckSum = checkSums[i]

        # Generate possible lengths of spaces

        spaceCount = len(currCheckSum) + 1
        spaceSum = len(currLine) - (sum(currCheckSum) + (len(currCheckSum) - 1))

        arrangements = multichoose(spaceCount, spaceSum)

        print(arrangements)

        # Check each arrangement if it fits the line
        fittingArrangementsCount = 0
        for arrangement in arrangements:
            arrLen = len(arrangement)
            lineOption = []
            for a in range(arrLen):
                lineOption += ['.' for _ in range(arrangement[a])]

                if a != arrLen - 1:
                    lineOption += ['#' for _ in range(currCheckSum[a])]
                    if a != arrLen - 2:
                        lineOption.append('.')

            print(lineOption)

            optionFitsActual = True
            for l in range(len(currLine)):
                if currLine[l] != '?':
                    if currLine[l] != lineOption[l]:
                        optionFitsActual = False
                        break

            if optionFitsActual:
                fittingArrangementsCount += 1

        fittingArrangementsCounts.append(fittingArrangementsCount)

    print(sum(fittingArrangementsCounts))

def getArrangements(allFields, numOfActive):
    if allFields == numOfActive:
        return [[1 for _ in range(allFields)]]

    if numOfActive == 0:
        return [[0 for _ in range(allFields)]]

    return [[1] + res for res in getArrangements(allFields - 1, numOfActive - 1)] + [[0] + res for res in getArrangements(allFields - 1, numOfActive)]

def solve12():
    f = open("example12.txt", "r")
    rawLines = f.readlines()

    lines = []
    checkSums = []

    for rawLine in rawLines:
        splitLine = rawLine.strip().split(' ')
        lines.append(splitLine[0])
        checkSums.append([int(c) for c in splitLine[1].split(',')])

    print(lines)
    print(checkSums)

    sumValidArrangaments = 0
    for l in range(len(lines)):
        currLine = lines[l]
        currCheckSum = checkSums[l]

        sumHash = 0
        sumWildcard = 0
        for ch in currLine:
            if ch == '#':
                sumHash += 1
            if ch == '?':
                sumWildcard += 1

        print(sumWildcard)

        missingHashCount = sum(currCheckSum) - sumHash
        print(missingHashCount)

        arrangements = getArrangements(sumWildcard, missingHashCount)

        validArrangamentsCount = 0
        for arrangement in arrangements:
            lineOption = []
            wildcardNum = 0
            for ch in currLine:
                if ch == '?':
                    if arrangement[wildcardNum] == 1:
                        lineOption.append('#')
                    else:
                        lineOption.append('.')

                    wildcardNum += 1
                else:
                    lineOption.append(ch)

            #print(lineOption)

            contHashNum = -1
            inContHash = False
            contHashLen = 0
            for ch in lineOption:
                if ch == '#':
                    if not inContHash:
                        inContHash = True
                        contHashNum += 1

                    contHashLen += 1
                else:
                    if inContHash:
                        if len(currCheckSum) <= contHashNum or currCheckSum[contHashNum] != contHashLen:
                            break

                        inContHash = False
                        contHashLen = 0
            else:
                if inContHash:
                    if len(currCheckSum) <= contHashNum or currCheckSum[contHashNum] != contHashLen:
                        pass
                    else:
                        validArrangamentsCount += 1
                else:
                    validArrangamentsCount += 1

        print(validArrangamentsCount)
        print()

        sumValidArrangaments += validArrangamentsCount

    print(sumValidArrangaments)

import regex as re

def findOptions(line, alreadyMatched, matchPos, pattern, checksums, currChecksumNum, consHashs, optionCount):
    if len(line) <= matchPos:
        return optionCount
    else:
        currCheck = 0
        if currChecksumNum < len(checksums):
            currCheck = checksums[currChecksumNum]

        if line[matchPos] == '?':
            restOfLine = line[matchPos + 1:]

            option1Count = 0
            option2Count = 0

            if consHashs == 0 or currCheck == 0:
                option1 = alreadyMatched + '.'
                if pattern.fullmatch(option1 + restOfLine):
                    option1Count = findOptions(line, option1, matchPos + 1, pattern, checksums, currChecksumNum, consHashs,  1)
            elif consHashs == currCheck:
                consHashs = 0
                currChecksumNum += 1

                option1Count = findOptions(line, alreadyMatched + '.', matchPos + 1, pattern, checksums, currChecksumNum, consHashs,1)

            if consHashs == 0:
                option2 = alreadyMatched + '#'
                if pattern.fullmatch(option2 + restOfLine):
                    option2Count = findOptions(line, option2, matchPos + 1, pattern, checksums, currChecksumNum, consHashs + 1, 1)

            elif currCheck != 0 and consHashs < currCheck:
                option2Count = findOptions(line, alreadyMatched + '#', matchPos + 1, pattern, checksums, currChecksumNum,
                                           consHashs + 1, 1)

            return option1Count + option2Count
        else:
            if line[matchPos] == '#':
                consHashs += 1
            elif line[matchPos] == '.':
                if currCheck != 0 and consHashs == currCheck:
                    consHashs = 0
                    currChecksumNum += 1

            return findOptions(line, alreadyMatched + line[matchPos], matchPos + 1, pattern, checksums, currChecksumNum, consHashs, optionCount)

def solve12_alt():
    f = open("input12.txt", "r")
    rawLines = f.readlines()

    lines = []
    checkSums = []

    for rawLine in rawLines:
        splitLine = rawLine.strip().split(' ')
        lines.append(splitLine[0])
        checkSums.append([int(c) for c in splitLine[1].split(',')])

    print(lines)
    print(checkSums)

    sum = 0

    for l in range(len(lines)):
        currLine = lines[l]
        currCheckSum = checkSums[l]

        pattern = "^[\\.\\?]*"
        for c in range(len(currCheckSum) - 1):
            pattern += '[#\\?]{' + str(currCheckSum[c]) + '}[\\.\\?]+'

        pattern += '[#\\?]{' + str(currCheckSum[-1]) + '}[\\.\\?]*$'

        print(pattern)

        p = re.compile(pattern)

        optionsCount = findOptions(currLine, "", 0, p, currCheckSum, 0, 0, 0)
        print(optionsCount)

        sum += optionsCount

    print(sum)

def solve12_2():
    f = open("input12.txt", "r")
    rawLines = f.readlines()

    lines = []
    checkSums = []

    for rawLine in rawLines:
        splitRawLine = rawLine.strip().split(' ')

        line = splitRawLine[0]
        for _ in range(4):
            line += '?' + splitRawLine[0]
        lines.append(line)

        checkSum = [int(c) for c in splitRawLine[1].split(',')]
        unfoldedCheckSum = []
        for _ in range(5):
            unfoldedCheckSum += checkSum
        checkSums.append(unfoldedCheckSum)

    print(lines)
    print(checkSums)

    sum = 0

    for l in range(len(lines)):
        currLine = lines[l]
        currCheckSum = checkSums[l]

        pattern = "^[\\.\\?]*"
        for c in range(len(currCheckSum) - 1):
            pattern += '[#\\?]{' + str(currCheckSum[c]) + '}[\\.\\?]+'

        pattern += '[#\\?]{' + str(currCheckSum[-1]) + '}[\\.\\?]*$'

        print(pattern)

        p = re.compile(pattern)

        optionsCount = findOptions(currLine, "", 0, p, currCheckSum, 0, 0, 0)
        print(optionsCount)

        sum += optionsCount

    print(sum)

def checkMirror(pattern):
    mirrorRows = []
    #longestMirrorLength = 0

    for mR in range(1, len(pattern)):
        isMirror = True
        mirrorLength = 0
        for checkR in range(mR, len(pattern)):
            mirrorLength = checkR - mR
            mirroredRowNum = mR - 1 - mirrorLength
            if 0 <= mirroredRowNum:
                if pattern[checkR] != pattern[mirroredRowNum]:
                    isMirror = False
                    break
            else:
                break

        #if isMirror and longestMirrorLength <= mirrorLength:
        if isMirror:
            mirrorRows.append(mR)
            #longestMirrorLength = mirrorLength

    return mirrorRows

def transposePattern(pattern):
    transposedPattern = []
    for c in range(len(pattern[0])):
        newRow = ""
        for row in pattern:
            newRow += row[c]

        transposedPattern.append(newRow)

    return transposedPattern

def solve13():
    f = open("input13.txt", "r")
    rawLines = f.readlines()

    patterns = []
    newPattern = []

    for rawLine in rawLines:
        if len(rawLine) == 1:
            patterns.append(newPattern)
            newPattern = []
        else:
            newPattern.append([c for c in rawLine.strip()])

    print(len(patterns))
    print(patterns)

    sum = 0
    for pattern in patterns:
        mirrorRows = checkMirror(pattern)
        mirrorRow = mirrorRows[0] if len(mirrorRows) != 0 else 0
        mirrorCol = 0

        print(mirrorRow)

        if mirrorRow == 0:
            transposedPattern = transposePattern(pattern)

            #print(transposedPattern)

            mirrorCols = checkMirror(transposedPattern)
            mirrorCol = mirrorCols[0] if len(mirrorCols) != 0 else 0

        print(mirrorCol)

        # Part 2
        for l in range(len(pattern)):
            line = pattern[l]
            for c in range(len(line)):
                prevVal = line[c]
                if line[c] == '.':
                    line[c] = '#'
                else:
                    line[c] = '.'

                altMirrorRow = 0
                for newMirrorRow in checkMirror(pattern):
                    if newMirrorRow != mirrorRow:
                        altMirrorRow = newMirrorRow

                altMirrorCol = 0

                if altMirrorRow == 0:
                    transposedPattern = transposePattern(pattern)

                    # print(transposedPattern)

                    for newMirrorCol in checkMirror(transposedPattern):
                        if newMirrorCol != mirrorCol:
                            altMirrorCol = newMirrorCol

                if altMirrorRow != 0:
                    mirrorRow = altMirrorRow
                    mirrorCol = 0

                    print(f"{l} {c}")
                    print(mirrorRow)
                    print(mirrorCol)
                    break

                if altMirrorCol != 0:
                    mirrorRow = 0
                    mirrorCol = altMirrorCol

                    print(f"{l} {c}")
                    print(mirrorRow)
                    print(mirrorCol)
                    break

                line[c] = prevVal
            else:
                continue

            break

        sum += 100 * mirrorRow
        sum += mirrorCol

        print()

    print(sum)

def moveRockNorth(field, row, col):
    prevRow = row
    for nextRow in range(row - 1, -1, -1):
        if field[nextRow][col] in ['#', 'O']:
            break
        else:
            field[nextRow][col] = 'O'
            field[prevRow][col] = '.'
            prevRow = nextRow

def moveRockSouth(field, row, col):
    prevRow = row
    for nextRow in range(row + 1, len(field)):
        if field[nextRow][col] in ['#', 'O']:
            break
        else:
            field[nextRow][col] = 'O'
            field[prevRow][col] = '.'
            prevRow = nextRow

def moveRockWest(field, row, col):
    prevCol = col
    for nextCol in range(col - 1, -1, -1):
        if field[row][nextCol] in ['#', 'O']:
            break
        else:
            field[row][nextCol] = 'O'
            field[row][prevCol] = '.'
            prevCol = nextCol

def moveRockEast(field, row, col):
    prevCol = col
    for nextCol in range(col + 1, len(field[row])):
        if field[row][nextCol] in ['#', 'O']:
            break
        else:
            field[row][nextCol] = 'O'
            field[row][prevCol] = '.'
            prevCol = nextCol

def solve14():
    f = open("input14.txt", "r")
    rawLines = f.readlines()

    field = []

    for rawLine in rawLines:
        row = []
        field.append(row)
        for char in rawLine.strip():
            row.append(char)

    print(field)

    for _ in range(1000):
        # Move rocks north
        for r in range(1, len(field)):
            row = field[r]
            for c in range(len(row)):
                if row[c] == 'O':
                    moveRockNorth(field, r, c)

        # Move rocks west
        for r in range(len(field)):
            row = field[r]
            for c in range(1, len(row)):
                if row[c] == 'O':
                    moveRockWest(field, r, c)

        # Move rocks south
        for r in range(len(field) - 2, -1, -1):
            row = field[r]
            for c in range(len(row)):
                if row[c] == 'O':
                    moveRockSouth(field, r, c)

        # Move rocks east
        for r in range(len(field)):
            row = field[r]
            for c in range(len(row) - 2, -1, -1):
                if row[c] == 'O':
                    moveRockEast(field, r, c)

    sumWeight = 0
    fieldLen = len(field)
    for r in range(0, fieldLen):
        row = field[r]
        print(row)

        for char in row:
            if char == 'O':
                sumWeight += (fieldLen - r)

    print(sumWeight)

def hash(input):
    hash = 0
    for ch in input:
        hash += ord(ch)
        hash *= 17
        hash %= 256

    return hash

class Lens:
    def __init__(self, power, ord):
        self.power = power
        self.ord = ord

    def __lt__(self, other):
        return self.ord < other.ord

    def __str__(self):
        return f"{self.ord} {self.power}"

class Box:
    def __init__(self):
        self.lensOrd = 0
        self.lenses = {}

def solve15():
    f = open("input15.txt", "r")
    rawLines = f.readlines()

    insts = [inst for inst in rawLines[0].strip().split(',')]

    boxes = [Box() for _ in range(256)]

    sum = 0

    for inst in insts:
        splitInst = inst.split('=')
        if len(splitInst) == 1:
            label = splitInst[0][0:-1]
            boxes[hash(label)].lenses.pop(label, None)
        else:
            label = splitInst[0]
            power = int(splitInst[1])
            currBox = boxes[hash(label)]

            lens = currBox.lenses.get(label, None)
            if lens == None:
                currBox.lenses[label] = Lens(power, currBox.lensOrd)
                currBox.lensOrd += 1
            else:
                lens.power = power

    for b in range(256):
        lenses = list(boxes[b].lenses.values())
        lenses.sort()

        for lens in lenses:
            print(lens, end=',')
        print()

        for l in range(len(lenses)):
            sum += (b + 1) * (l + 1) * lenses[l].power

    print(sum)

def followBeam(field, energized, splits, currRow, currCol, dir):
    if currRow < 0 or currCol < 0 or len(field) <= currRow or len(field[currRow]) <= currCol:
        return

    if (currRow, currCol) in splits:
        return

    energized[currRow][currCol] = True
    currElem = field[currRow][currCol]

    if dir == 'r':
        if currElem == '.' or currElem == '-':
            followBeam(field, energized, splits, currRow, currCol + 1, dir)
        elif currElem == '/':
            followBeam(field, energized, splits, currRow - 1, currCol, 'u')
        elif currElem == '\\':
            followBeam(field, energized, splits, currRow + 1, currCol, 'd')
        elif currElem == '|':
            splits.append((currRow, currCol))
            followBeam(field, energized, splits, currRow - 1, currCol, 'u')
            followBeam(field, energized, splits, currRow + 1, currCol, 'd')
    elif dir == 'd':
        if currElem == '.' or currElem == '|':
            followBeam(field, energized, splits, currRow + 1, currCol, dir)
        elif currElem == '/':
            followBeam(field, energized, splits, currRow, currCol - 1, 'l')
        elif currElem == '\\':
            followBeam(field, energized, splits, currRow, currCol + 1, 'r')
        elif currElem == '-':
            splits.append((currRow, currCol))
            followBeam(field, energized, splits, currRow, currCol - 1, 'l')
            followBeam(field, energized, splits, currRow, currCol + 1, 'r')
    elif dir == 'l':
        if currElem == '.' or currElem == '-':
            followBeam(field, energized, splits, currRow, currCol - 1, dir)
        elif currElem == '/':
            followBeam(field, energized, splits, currRow + 1, currCol, 'd')
        elif currElem == '\\':
            followBeam(field, energized, splits, currRow - 1, currCol, 'u')
        elif currElem == '|':
            splits.append((currRow, currCol))
            followBeam(field, energized, splits, currRow - 1, currCol, 'u')
            followBeam(field, energized, splits, currRow + 1, currCol, 'd')
    elif dir == 'u':
        if currElem == '.' or currElem == '|':
            followBeam(field, energized, splits, currRow - 1, currCol, dir)
        elif currElem == '/':
            followBeam(field, energized, splits, currRow, currCol + 1, 'r')
        elif currElem == '\\':
            followBeam(field, energized, splits, currRow, currCol - 1, 'l')
        elif currElem == '-':
            splits.append((currRow, currCol))
            followBeam(field, energized, splits, currRow, currCol - 1, 'l')
            followBeam(field, energized, splits, currRow, currCol + 1, 'r')

def solve16():
    f = open("input16.txt", "r")
    rawLines = f.readlines()

    field = []

    for rawLine in rawLines:
        line = rawLine.strip()
        field.append(line)

    maxEnergizedCount = 0
    for c in range(len(field[0])):
        energized = [[False for _ in range(len(rawLines[1]))] for _ in rawLines]

        followBeam(field, energized, [], 0, c, 'd')

        sum = 0
        for row in energized:
            for pos in row:
                if pos:
                    print(1, end='')
                    sum += 1
                else:
                    print(0, end='')
            print()

        print(sum)
        maxEnergizedCount = max(maxEnergizedCount, sum)

    for c in range(len(field[0])):
        energized = [[False for _ in range(len(rawLines[1]))] for _ in rawLines]

        followBeam(field, energized, [], len(field) - 1, c, 'u')

        sum = 0
        for row in energized:
            for pos in row:
                if pos:
                    print(1, end='')
                    sum += 1
                else:
                    print(0, end='')
            print()

        print(sum)
        maxEnergizedCount = max(maxEnergizedCount, sum)

    for r in range(len(field)):
        energized = [[False for _ in range(len(rawLines[1]))] for _ in rawLines]

        followBeam(field, energized, [], r, 0, 'r')

        sum = 0
        for row in energized:
            for pos in row:
                if pos:
                    print(1, end='')
                    sum += 1
                else:
                    print(0, end='')
            print()

        print(sum)
        maxEnergizedCount = max(maxEnergizedCount, sum)

    for r in range(len(field)):
        energized = [[False for _ in range(len(rawLines[1]))] for _ in rawLines]

        followBeam(field, energized, [], r, len(field[0]) - 1, 'l')

        sum = 0
        for row in energized:
            for pos in row:
                if pos:
                    print(1, end='')
                    sum += 1
                else:
                    print(0, end='')
            print()

        print(sum)
        maxEnergizedCount = max(maxEnergizedCount, sum)

    print(maxEnergizedCount)

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

class RowElem:
    def __init__(self, type, startCol, endCol):
        self.type = type
        self.start = startCol
        self.end = endCol

    def __str__(self):
        return f"{self.type}({self.start}, {self.end})"

def solve18():
    f = open("input18.txt", "r")
    rawLines = f.readlines()

    steps = []

    for rawLine in rawLines:
        splitLine = rawLine.strip().split(' ')

        dir = ''
        if splitLine[2][7] == '0':
            dir = 'R'
        elif splitLine[2][7] == '1':
            dir = 'D'
        elif splitLine[2][7] == '2':
            dir = 'L'
        elif splitLine[2][7] == '3':
            dir = 'U'

        steps.append((dir, int(splitLine[2][2:7], 16)))

        #steps.append((splitLine[0], int(splitLine[1])))

    print(steps)

    maxRow = 0
    minRow = 0
    maxCol = 0
    minCol = 0

    currRow = 0
    currCol = 0

    for step in steps:
        if step[0] == 'R':
            currCol += step[1]
            maxCol = max(maxCol, currCol)
        elif step[0] == 'L':
            currCol -= step[1]
            minCol = min(minCol, currCol)
        elif step[0] == 'D':
            currRow += step[1]
            maxRow = max(maxRow, currRow)
        elif step[0] == 'U':
            currRow -= step[1]
            minRow = min(minRow, currRow)

    print(f"{currRow, currCol}")
    print(f"{minRow, maxRow, minCol, maxCol}")

    rowLen = maxRow - minRow + 1
    colLen = maxCol - minCol + 1

    currRow: int = 0 - minRow
    currCol: int = 0 - minCol

    startRow = currRow
    startCol = currCol

    field = [[RowElem('.', 0, colLen)] for _ in range(rowLen)]

    lastStepNum = len(steps) - 1
    for s in range(len(steps)):
        currStep = steps[s]
        if currStep[0] == 'R':
            newElem = RowElem('-', currCol + 1, currCol + currStep[1] + 1)
            bendElem = None

            if s != lastStepNum:
                nextStep = steps[s + 1]

                if nextStep[0] == 'D':
                    newElem = RowElem('-', currCol + 1, currCol + currStep[1])
                    bendElem = RowElem('7', currCol + currStep[1], currCol + currStep[1] + 1)
                elif nextStep[0] == 'U':
                    newElem = RowElem('-', currCol + 1, currCol + currStep[1])
                    bendElem = RowElem('J', currCol + currStep[1], currCol + currStep[1] + 1)

            newRow = []
            for elem in field[currRow]:
                if elem.start <= newElem.start and newElem.start < elem.end:
                    if elem.start == newElem.start:
                        newRow.append(newElem)
                    else:
                        newRow.append(RowElem(elem.type, elem.start, newElem.start))
                        newRow.append(newElem)

                    if bendElem is not None:
                        newRow.append(bendElem)

                        if bendElem.end < elem.end:
                            newRow.append(RowElem(elem.type, bendElem.end, elem.end))
                    else:
                        if newElem.end < elem.end:
                            newRow.append(RowElem(elem.type, newElem.end, elem.end))
                else:
                    newRow.append(elem)

            field[currRow] = newRow

            currCol += currStep[1]
        elif currStep[0] == 'L':
            newElem = RowElem('-', currCol - currStep[1], currCol)
            bendElem = None

            if s != lastStepNum:
                nextStep = steps[s + 1]

                if nextStep[0] == 'D':
                    newElem = RowElem('-', currCol - currStep[1] + 1, currCol)
                    bendElem = RowElem('F', currCol - currStep[1], currCol - currStep[1] + 1)
                elif nextStep[0] == 'U':
                    newElem = RowElem('-', currCol - currStep[1] + 1, currCol)
                    bendElem = RowElem('L', currCol - currStep[1], currCol - currStep[1] + 1)

            newRow = []
            if bendElem is None:
                for elem in field[currRow]:
                    if elem.start <= newElem.start and newElem.start < elem.end:
                        if elem.start == newElem.start:
                            newRow.append(newElem)
                        else:
                            newRow.append(RowElem(elem.type, elem.start, newElem.start))
                            newRow.append(newElem)

                        if newElem.end < elem.end:
                            newRow.append(RowElem(elem.type, newElem.end, elem.end))
                    else:
                        newRow.append(elem)
            else:
                for elem in field[currRow]:
                    if elem.start <= bendElem.start and bendElem.start < elem.end:
                        if elem.start == bendElem.start:
                            newRow.append(bendElem)
                            newRow.append(newElem)
                        else:
                            newRow.append(RowElem(elem.type, elem.start, bendElem.start))
                            newRow.append(bendElem)
                            newRow.append(newElem)

                        if newElem.end < elem.end:
                            newRow.append(RowElem(elem.type, newElem.end, elem.end))
                    else:
                        newRow.append(elem)

            field[currRow] = newRow

            currCol -= currStep[1]
        elif currStep[0] == 'D':
            for r in range(1, currStep[1]):
                newElem = RowElem('|', currCol, currCol + 1)
                nextRowNum = currRow + r

                newRow = []
                for elem in field[nextRowNum]:
                    if elem.start <= newElem.start and newElem.start < elem.end:
                        if elem.start == newElem.start:
                            newRow.append(newElem)
                        else:
                            newRow.append(RowElem(elem.type, elem.start, newElem.start))
                            newRow.append(newElem)

                        if newElem.end < elem.end:
                            newRow.append(RowElem(elem.type, newElem.end, elem.end))
                    else:
                        newRow.append(elem)

                field[nextRowNum] = newRow

            bendElem = None
            if s != lastStepNum:
                nextStep = steps[s + 1]

                if nextStep[0] == 'R':
                    bendElem = RowElem('L', currCol, currCol + 1)
                elif nextStep[0] == 'L':
                    bendElem = RowElem('J', currCol, currCol + 1)

            if bendElem is not None:
                newRow = []
                for elem in field[currRow + currStep[1]]:
                    if elem.start <= bendElem.start and bendElem.start < elem.end:
                        if elem.start == bendElem.start:
                            newRow.append(bendElem)
                        else:
                            newRow.append(RowElem(elem.type, elem.start, bendElem.start))
                            newRow.append(bendElem)

                        if bendElem.end < elem.end:
                            newRow.append(RowElem(elem.type, bendElem.end, elem.end))
                    else:
                        newRow.append(elem)

                field[currRow + currStep[1]] = newRow

            currRow += currStep[1]
        elif currStep[0] == 'U':
            for r in range(1, currStep[1]):
                newElem = RowElem('|', currCol, currCol + 1)
                nextRowNum = currRow - r

                newRow = []
                for elem in field[nextRowNum]:
                    if elem.start <= newElem.start and newElem.start < elem.end:
                        if elem.start == newElem.start:
                            newRow.append(newElem)
                        else:
                            newRow.append(RowElem(elem.type, elem.start, newElem.start))
                            newRow.append(newElem)

                        if newElem.end < elem.end:
                            newRow.append(RowElem(elem.type, newElem.end, elem.end))
                    else:
                        newRow.append(elem)

                field[nextRowNum] = newRow

            bendElem = None
            if s != lastStepNum:
                nextStep = steps[s + 1]

                if nextStep[0] == 'R':
                    bendElem = RowElem('F', currCol, currCol + 1)
                elif nextStep[0] == 'L':
                    bendElem = RowElem('7', currCol, currCol + 1)

            if bendElem is not None:
                newRow = []
                for elem in field[currRow - currStep[1]]:
                    if elem.start <= bendElem.start and bendElem.start < elem.end:
                        if elem.start == bendElem.start:
                            newRow.append(bendElem)
                        else:
                            newRow.append(RowElem(elem.type, elem.start, bendElem.start))
                            newRow.append(bendElem)

                        if bendElem.end < elem.end:
                            newRow.append(RowElem(elem.type, bendElem.end, elem.end))
                    else:
                        newRow.append(elem)

                field[currRow - currStep[1]] = newRow

            currRow -= currStep[1]

        bendElem = None
        if steps[-1][0] == 'U':
            if steps[0][0] == 'R':
                bendElem = RowElem('F', startCol, startCol + 1)
            elif steps[0][0] == 'L':
                bendElem = RowElem('7', startCol, startCol + 1)
        elif steps[-1][0] == 'D':
            if steps[0][0] == 'R':
                bendElem = RowElem('L', startCol, startCol + 1)
            elif steps[0][0] == 'L':
                bendElem = RowElem('J', startCol, startCol + 1)
        elif steps[-1][0] == 'L':
            if steps[0][0] == 'U':
                bendElem = RowElem('L', startCol, startCol + 1)
            elif steps[0][0] == 'D':
                bendElem = RowElem('F', startCol, startCol + 1)
        elif steps[-1][0] == 'R':
            if steps[0][0] == 'U':
                bendElem = RowElem('J', startCol, startCol + 1)
            elif steps[0][0] == 'D':
                bendElem = RowElem('7', startCol, startCol + 1)

        newRow = []
        for elem in field[startRow]:
            if elem.start <= bendElem.start and bendElem.start < elem.end:
                if elem.start == bendElem.start:
                    newRow.append(bendElem)
                else:
                    newRow.append(RowElem(elem.type, elem.start, bendElem.start))
                    newRow.append(bendElem)

                if bendElem.end < elem.end:
                    newRow.append(RowElem(elem.type, bendElem.end, elem.end))
            else:
                newRow.append(elem)

        field[startRow] = newRow

    sum = 0
    for row in field:
        inDigSite = False
        prevBend = ''

        for elem in row:
            print(elem, end='')

            if elem.type == '.':
                if inDigSite:
                    sum += elem.end - elem.start
            elif elem.type == '-':
                sum += elem.end - elem.start
            elif elem.type == '|':
                sum += 1

                inDigSite = not inDigSite
            elif elem.type == 'F':
                sum += 1

                inDigSite = not inDigSite

                prevBend = 'F'
            elif elem.type == 'J':
                sum += 1

                if prevBend != 'F':
                    inDigSite = not inDigSite

                prevBend = 'J'
            elif elem.type == 'L':
                sum += 1

                inDigSite = not inDigSite

                prevBend = 'L'
            elif elem.type == '7':
                sum += 1

                if prevBend != 'L':
                    inDigSite = not inDigSite

                prevBend = '7'

        print()

    print(sum)

class WFStep:
    def __init__(self, code):
        splitCode = code.split(':')

        if len(splitCode) == 1:
            self.compareTo = None
            self.sendTo = splitCode[0][:-1]
        else:
            compareChar = splitCode[0][0]
            if compareChar == 'x':
                self.compare = 0
            elif compareChar == 'm':
                self.compare = 1
            elif compareChar == 'a':
                self.compare = 2
            elif compareChar == 's':
                self.compare = 3

            self.compareTo = int(splitCode[0][2:])
            self.smaller = True if splitCode[0][1] == '<' else False
            self.sendTo = splitCode[1]

    def __str__(self):
        if self.compareTo is None:
            return(f"{self.sendTo}")
        else:
            return(f"{self.compare}{'<' if self.smaller else '>'}{self.compareTo}:{self.sendTo}")

    def exec(self, input):
        if self.compareTo is None:
            return self.sendTo
        else:
            if self.smaller:
                if input[self.compare] < self.compareTo:
                    return self.sendTo
                else:
                    return None
            else:
                if self.compareTo < input[self.compare]:
                    return self.sendTo
                else:
                    return None

    def execOnRange(self, input):
        res = []
        if self.compareTo is None:
            resRanges = [r for r in input]
            res.append((self.sendTo, resRanges))
        else:
            rangeStart = input[self.compare][0]
            rangeEnd = input[self.compare][1]

            matchRange = None
            complementRange = None

            if self.smaller:
                if rangeStart < self.compareTo:
                    if self.compareTo < rangeEnd:
                        matchRange = (rangeStart, self.compareTo)
                        complementRange = (self.compareTo, rangeEnd)
                    else:
                        matchRange = (rangeStart, rangeEnd)
                else:
                    complementRange = (rangeStart, rangeEnd)
            else:
                if self.compareTo < rangeStart:
                    matchRange = (rangeStart, rangeEnd)
                else:
                    if self.compareTo < rangeEnd:
                        matchRange = (self.compareTo + 1, rangeEnd)
                        complementRange = (rangeStart, self.compareTo + 1)
                    else:
                        complementRange = (rangeStart, rangeEnd)

            if matchRange is not None:
                resRanges = [r for r in input]
                resRanges[self.compare] = matchRange
                res.append((self.sendTo, resRanges))

            if complementRange is not None:
                resRanges = [r for r in input]
                resRanges[self.compare] = complementRange
                res.append((None, resRanges))

        return res

def solve19():
    f = open("input19.txt", "r")
    rawLines = f.readlines()

    inWorkflows = True
    workflows = {}
    parts = []
    for rawLine in rawLines:
        if rawLine == '\n':
            inWorkflows = False
            continue

        if inWorkflows:
            firstSplit = rawLine.strip().split('{')
            secondSplit = firstSplit[1].split(',')

            workflows[firstSplit[0]] = [WFStep(split) for split in secondSplit]
        else:
            part = [int(split.split('=')[1]) for split in rawLine[1:-2].split(',')]
            parts.append(part)

    for k, v in workflows.items():
        print(f"{k} ", end='')
        for step in v:
            print(step, end=',')
        print()

    print(parts)

    accSum = 0
    for part in parts:
        wf = 'in'
        while wf not in ['A', 'R']:
            for step in workflows[wf]:
                wf = step.exec(part)
                if wf is not None:
                    break

        if wf == 'A':
            accSum += sum(part)

    print(accSum)

def mapWorkflow(workflows, currW, currRanges, acceptedRanges):
    if currW == 'A':
        acceptedRanges.append(currRanges)
        return
    elif currW == 'R':
        return
    else:
        procRanges = currRanges
        for step in workflows[currW]:
            res = step.execOnRange(procRanges)

            print(res)

            if 0 < len(res):
                mapWorkflow(workflows, res[0][0], res[0][1], acceptedRanges)

            if len(res) == 2:
                procRanges = res[1][1]
            else:
                break


def solve19_2():
    f = open("input19.txt", "r")
    rawLines = f.readlines()

    inWorkflows = True
    workflows = {}

    for rawLine in rawLines:
        if rawLine == '\n':
            inWorkflows = False
            continue

        if inWorkflows:
            firstSplit = rawLine.strip().split('{')
            secondSplit = firstSplit[1].split(',')

            workflows[firstSplit[0]] = [WFStep(split) for split in secondSplit]
        else:
            break

    for k, v in workflows.items():
        print(f"{k} ", end='')
        for step in v:
            print(step, end=',')
        print()

    validRanges = [(1, 4001), (1, 4001), (1, 4001), (1, 4001)]
    acceptedRanges = []

    mapWorkflow(workflows, "in", validRanges, acceptedRanges)

    print()

    sum = 0
    for ranges in acceptedRanges:
        print(ranges)

        options = 1
        for range in ranges:
            options *= max(1, range[1] - range[0])

        sum += options

    print(sum)



import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    solve12_alt()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
