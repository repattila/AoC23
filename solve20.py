import collections, difflib

class Pulse:
    def __init__(self, isHigh, source, dest):
        self.isHigh = isHigh
        self.source = source
        self.dest = dest

    def __str__(self):
        return f"Pulse({self.isHigh},{self.source},{self.dest})"

class FlipFlop:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.isOn = False

    def process(self, pulse):
        if pulse.isHigh:
            return []
        else:
            self.isOn = not self.isOn

            res = []
            for output in self.outputs:
                res.append(Pulse(self.isOn, self.name, output))

            return res

    def addInput(self, source):
        pass

    def __str__(self):
        res = f"FF({self.name}, outs="
        for out in self.outputs:
            res += out + ' '

        res += f"isON={1 if self.isOn else 0}"

        return res + ')'

class Conjunction:
    def __init__(self, name, outputs):
        self.name = name
        self.inputs = {}
        self.outputs = outputs

    def addInput(self, source):
        self.inputs[source] = False

    def process(self, pulse):
        self.inputs[pulse.source] = pulse.isHigh

        allHigh = True
        for input in self.inputs.values():
            if not input:
                allHigh = False
                break

        res = []
        for output in self.outputs:
            res.append(Pulse(not allHigh, self.name, output))

        return res

    def __str__(self):
        res = f"C({self.name}, outs="
        for out in self.outputs:
            res += out + ' '

        res += "ins="
        for input, val in self.inputs.items():
            res += f"{input}:{1 if val else 0} "

        return res + ')'

def solve20():
    f = open("input20.txt", "r")
    rawLines = f.readlines()

    components = {}
    pulses = []

    for rawLine in rawLines:
        splitLine = rawLine.strip().split(" -> ")
        type = splitLine[0][0]
        name = splitLine[0][1:]

        outputs = [out for out in splitLine[1].split(", ")]

        if type == '%':
            components[name] = FlipFlop(name, outputs)
        elif type == '&':
            components[name] = Conjunction(name, outputs)
        elif type == 'b':
            for output in outputs:
                pulses.append(Pulse(False, "broadcaster", output))

    for comp in components.values():
        for output in comp.outputs:
            targetComp = components.get(output, None)
            if targetComp is not None:
                targetComp.addInput(comp.name)

    initialState = ''

    for name, comp in components.items():
        print(name, end=', ')
        print(comp)

        initialState += str(comp)

    print(initialState)

    prevState = initialState
    highCount = 0
    lowCount = 0
    buttonPressCount = 0

    while True:
        buttonPressCount += 1

        # Count low pulse from button
        lowCount += 1

        pulsesQ = collections.deque()
        for pulse in pulses:
            pulsesQ.append(pulse)

        while pulsesQ:
            # for pulse in pulsesQ:
            #     print(pulse, end=", ")
            # print()

            currPulse = pulsesQ.popleft()
            if currPulse.isHigh:
                highCount += 1
            else:
                lowCount += 1

            if currPulse.dest == "rx" and not currPulse.isHigh:
                break

            destComp = components.get(currPulse.dest, None)
            if destComp is None:
                continue
            res = destComp.process(currPulse)

            for pulse in res:
                pulsesQ.append(pulse)
        else:
            currState = ''
            for name, comp in components.items():
                #print(name, end=', ')
                #print(comp)

                currState += str(comp)

            if currState == initialState:
                print(buttonPressCount)
            else:
                print(currState)

                diffLine = ''
                for i, s in enumerate(difflib.ndiff(currState, prevState)):
                    if s[0] == ' ':
                        diffLine += ' '
                    elif s[0] == '-':
                        diffLine += '-'
                print(diffLine)

                prevState = currState

            continue

        break

    print(highCount)
    print(lowCount)
    print(buttonPressCount)
    #print(highCount * lowCount)
