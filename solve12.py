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

import re

def findOptions(line, alreadyMatched, matchPos, pattern, checksums, currChecksumNum, consHashs):
    if len(line) <= matchPos or len(checksums) <= currChecksumNum:
        return 1
    else:
        currCheck = checksums[currChecksumNum]

        if line[matchPos] == '?':
            option1Count = 0
            option2Count = 0

            if consHashs == 0:
                option1 = alreadyMatched + '.'
                restOfLine = line[matchPos + 1:]
                if pattern.fullmatch(option1 + restOfLine):
                    option1Count = findOptions(line, option1, matchPos + 1, pattern, checksums, currChecksumNum, consHashs)
            elif consHashs == currCheck:
                consHashs = 0
                currChecksumNum += 1

                option1Count = findOptions(line, alreadyMatched + '.', matchPos + 1, pattern, checksums, currChecksumNum, consHashs)

            if consHashs == 0:
                option2 = alreadyMatched + '#'
                restOfLine = line[matchPos + 1:]
                if pattern.fullmatch(option2 + restOfLine):
                    option2Count = findOptions(line, option2, matchPos + 1, pattern, checksums, currChecksumNum, consHashs + 1)
            elif consHashs < currCheck:
                option2Count = findOptions(line, alreadyMatched + '#', matchPos + 1, pattern, checksums, currChecksumNum,
                                           consHashs + 1)

            return option1Count + option2Count
        else:
            if line[matchPos] == '#':
                consHashs += 1
            elif line[matchPos] == '.':
                if consHashs == currCheck:
                    consHashs = 0
                    currChecksumNum += 1

            return findOptions(line, alreadyMatched + line[matchPos], matchPos + 1, pattern, checksums, currChecksumNum, consHashs)

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

        optionsCount = findOptions(currLine, "", 0, p, currCheckSum, 0, 0)
        print(optionsCount)

        sum += optionsCount

    print(sum)

def doMatch(line, matchPos, checksums, currChecksumNum):
    currCheck = checksums[currChecksumNum]
    currMatchPos = matchPos

    isMatching = True
    for checkChar in currCheck:
        if len(line) <= currMatchPos:
            isMatching = False
            break

        lineChar = line[currMatchPos]
        if lineChar != '?' and lineChar != checkChar:
            isMatching = False
            break
        else:
            currMatchPos += 1

    return isMatching, currMatchPos

def findOptionsAlt(line, matchPos, checksums, checksumNum):
    options = 0
    currMatchPos = matchPos
    currChecksumNum = checksumNum
    while currMatchPos < len(line):
        currLineChar = line[currMatchPos]

        while currLineChar == '.':
            currMatchPos += 1

            if currMatchPos == len(line):
                break
            else:
                currLineChar = line[currMatchPos]

        if currMatchPos == len(line):
            continue

        if currLineChar == '#':
            if len(checksums) <= currChecksumNum:
                break
            else:
                isMatching, newMatchPos = doMatch(line, currMatchPos, checksums, currChecksumNum)

                if not isMatching:
                    break
                else:
                    currMatchPos = newMatchPos
                    currChecksumNum += 1

                    if currMatchPos == len(line):
                        continue
                    else:
                        currLineChar = line[currMatchPos]

        if currLineChar == '?':
            # try matching current block
            if currChecksumNum < len(checksums):
                isMatching, newMatchPos = doMatch(line, currMatchPos, checksums, currChecksumNum)

                if isMatching:
                    options += findOptionsAlt(line, newMatchPos, checksums, currChecksumNum + 1)

            # try .
            currMatchPos += 1
    else:
        if currChecksumNum == len(checksums):
            return options + 1
        else:
            return options

    return options

def solve12_alt1():
    f = open("input12.txt", "r")
    rawLines = f.readlines()

    lines = []
    checksums = []

    for rawLine in rawLines:
        splitLine = rawLine.strip().split(' ')
        lines.append(splitLine[0])

        checksum = []
        checks = splitLine[1].split(',')
        for c in range(len(checks)):
            check = ''
            for i in range(int(checks[c])):
                check += '#'

            if c != len(checks) - 1:
                check += '.'

            checksum.append(check)

        checksums.append(checksum)

    print(lines)
    print(checksums)

    sum = 0
    for l in range(len(lines)):
        currLine = lines[l]
        currChecksums = checksums[l]

        options = findOptionsAlt(currLine, 0, currChecksums, 0)
        print(options)

        sum += options

    print(sum)

def solve12_2():
    f = open("input12.txt", "r")
    rawLines = f.readlines()

    lines = []
    checksums = []

    for rawLine in rawLines:
        splitRawLine = rawLine.strip().split(' ')

        line = splitRawLine[0]
        for _ in range(4):
            line += '?' + splitRawLine[0]
        lines.append(line)

        checksum = [int(c) for c in splitRawLine[1].split(',')]
        unfoldedChecksum = []
        for _ in range(5):
            unfoldedChecksum += checksum

        checksum = []
        for c in range(len(unfoldedChecksum)):
            check = ''
            for i in range(unfoldedChecksum[c]):
                check += '#'

            if c != len(unfoldedChecksum) - 1:
                check += '.'

            checksum.append(check)

        checksums.append(checksum)

    print(lines)
    print(checksums)

    sum = 0
    for l in range(len(lines)):
        currLine = lines[l]
        currChecksums = checksums[l]

        options = findOptionsAlt(currLine, 0, currChecksums, 0)
        print(options)

        sum += options

    print(sum)
