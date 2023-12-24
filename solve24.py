
class Hailstone:
    def __init__(self, x0, y0, vX, vY):
        x1 = x0 + vX
        y1 = y0 + vY

        self.x0 = x0
        self.y0 = y0
        self.vX = vX
        self.vY = vY

        self.m = vY / vX
        self.c = (x1 * y0 - x0 * y1) / vX

        self.intersectTime = 0

    def intersect(self, other):
        if self.m == other.m:
            return None
        else:
            intersectX = (other.c - self.c) / (self.m - other.m)
            intersectY = self.m * intersectX + self.c

            return intersectX, intersectY
def solve24():
    f = open("input24.txt", "r")
    rawLines = f.readlines()

    hailstones = []

    for rawLine in rawLines:
        splitRawLine = rawLine.strip().split(" @ ")

        start = splitRawLine[0].split(", ")
        speed = splitRawLine[1].split(", ")

        hailstones.append(Hailstone(int(start[0]), int(start[1]), int(speed[0]), int(speed[1])))

    sumIntersects = 0
    for l in range(len(hailstones) - 1):
        for ol in range(l + 1, len(hailstones)):
            intersect = hailstones[l].intersect(hailstones[ol])
            if intersect is not None:
                print(intersect)

                t1 = ((intersect[0] - hailstones[l].x0)) / hailstones[l].vX
                t2 = ((intersect[0] - hailstones[ol].x0)) / hailstones[ol].vX

                print(t1)
                print(t2)

                # if 7 <= intersect[0] <= 27 \
                # and 7 <= intersect[1] <= 27 \
                if 200000000000000 <= intersect[0] <= 400000000000000 \
                and 200000000000000 <= intersect[1] <= 400000000000000 \
                and 0 <= t1 \
                and 0 <= t2:
                    sumIntersects += 1
            else:
                print("no intersection")

    print(sumIntersects)

