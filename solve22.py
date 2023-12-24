
class HOnX:
    def __init__(self, id, x, startY, endY, z):
        self.id = id
        self.x = x
        self.startY = startY
        self.endY = endY
        self.z = z

    def __str__(self):
        return(f"HOnX({self.id}, {self.x}, {self.startY}, {self.endY}, {self.z})")

    def __lt__(self, other):
        if type(other) is HOnX:
            return self.z < other.z
        elif type(other) is HOnY:
            return self.z < other.z
        elif type(other) is Vertical:
            return self.z < other.endZ

    def setZ(self, z):
        self.z = z

    def getBottom(self):
        return self.z

    def getTop(self):
        return self.z

    def collide(self, other):
        if type(other) is HOnX:
            collision = self.z < other.z and self.x == other.x and (
                self.startY <= other.startY <= self.endY or self.startY <= other.endY <= self.endY
            )

            if collision:
                other.setZ(self.z + 1)

            return collision
        elif type(other) is HOnY:
            collision = self.z < other.z and self.startY <= other.y <= self.endY and \
                other.startX <= self.x <= other.endX

            if collision:
                other.setZ(self.z + 1)

            return collision
        elif type(other) is Vertical:
            collision = self.z < other.startZ and self.startY <= other.y <= self.endY and \
                self.x == other.x

            if collision:
                other.setZ(self.z + 1)

            return collision

class HOnY:
    def __init__(self, id, startX, endX, y, z):
        self.id = id
        self.startX = startX
        self.endX = endX
        self.y = y
        self.z = z

    def __str__(self):
        return(f"HOnY({self.id}, {self.startX}, {self.endX}, {self.y}, {self.z})")

    def __lt__(self, other):
        if type(other) is HOnX:
            return self.z < other.z
        elif type(other) is HOnY:
            return self.z < other.z
        elif type(other) is Vertical:
            return self.z < other.endZ

    def setZ(self, z):
        self.z = z

    def getBottom(self):
        return self.z

    def getTop(self):
        return self.z

    def collide(self, other):
        if type(other) is HOnX:
            collision = self.z < other.z and self.startX <= other.x <= self.endX and \
                        other.startY <= self.y <= other.endY

            if collision:
                other.setZ(self.z + 1)

            return collision
        elif type(other) is HOnY:
            collision = self.z < other.z and self.y == other.y and (
                    self.startX <= other.startX <= self.endX or self.startX <= other.endX <= self.endX
            )

            if collision:
                other.setZ(self.z + 1)

            return collision
        elif type(other) is Vertical:
            collision = self.z < other.startZ and self.startX <= other.x <= self.endX and \
                        self.y == other.y

            if collision:
                other.setZ(self.z + 1)

            return collision

class Vertical:
    def __init__(self, id, x, y, startZ, endZ):
        self.id = id
        self.x = x
        self.y = y
        self.startZ = startZ
        self.endZ = endZ

    def __str__(self):
        return(f"Vertical({self.id}, {self.x}, {self.y}, {self.startZ}, {self.endZ})")

    def __lt__(self, other):
        if type(other) is HOnX:
            return self.endZ < other.z
        elif type(other) is HOnY:
            return self.endZ < other.z
        elif type(other) is Vertical:
            return self.endZ < other.startZ or self.endZ < other.endZ

    def setZ(self, z):
        height = self.endZ - self.startZ
        self.startZ = z
        self.endZ = z + height

    def getBottom(self):
        return self.startZ

    def getTop(self):
        return self.endZ

    def collide(self, other):
        if type(other) is HOnX:
            collision = self.endZ < other.z and other.startY <= self.y <= other.endY and \
                        self.x == other.x

            if collision:
                other.setZ(self.endZ + 1)

            return collision
        elif type(other) is HOnY:
            collision = self.endZ < other.z and other.startX <= self.x <= other.endX and \
                        self.y == other.y

            if collision:
                other.setZ(self.endZ + 1)

            return collision
        elif type(other) is Vertical:
            collision = self.endZ < other.startZ and other.x == self.x and self.y == other.y

            if collision:
                other.setZ(self.endZ + 1)

            return collision

def solve22():
    #f = open("examples/example22.txt", "r")
    f = open("input22.txt", "r")
    rawLines = f.readlines()

    bricks = []

    for r in range(len(rawLines)):
        rawLine = rawLines[r]
        splitRawLine = rawLine.strip().split('~')

        start = splitRawLine[0].split(',')
        end = splitRawLine[1].split(',')

        if start[2] == end[2]:
            if start[0] == end[0]:
                bricks.append(HOnX(r, int(start[0]), int(start[1]), int(end[1]), int(start[2])))
            else:
                bricks.append(HOnY(r, int(start[0]), int(end[0]), int(start[1]), int(start[2])))

        else:
            bricks.append(Vertical(r, int(start[0]), int(start[1]), int(start[2]), int(end[2])))

    bricks.sort()

    for brick in bricks:
        print(brick)

    supports = {}

    for i in range(len(bricks)):
        currBrick = bricks[i]

        if i == 0:
            currBrick.setZ(1)
            continue

        collisionAtZ = -1
        for j in range(i - 1, -1, -1):
            if collisionAtZ != -1 and bricks[j].getTop() != collisionAtZ:
                break

            if bricks[j].collide(currBrick):
                supportsList = supports.get(currBrick.id, None)
                if supportsList is None:
                    supports[currBrick.id] = [bricks[j].id]
                else:
                    supportsList.append(bricks[j].id)

                collisionAtZ = currBrick.getBottom() - 1

        if collisionAtZ == -1:
            currBrick.setZ(1)

        bricks.sort()

    for brick in bricks:
        print(brick)

    notRemovable = set()

    print(supports)

    for supported, supporters in supports.items():
        if len(supporters) == 1:
            notRemovable.add(supporters[0])

    print(notRemovable)
    print(len(bricks))
    print(len(bricks) - len(notRemovable))

