import random

class Earth:
    def __init__(self, width, height, scale, density):
        self.earthColumns = int(width/scale)
        self.earthRows = int(height/scale)

        def densityRepartition(percentage):
            self.ceil = random.random()
            if 100 * self.ceil < percentage:
                return 1
            else:
                return 0

        self.Entity = [[densityRepartition(density) for x in range(self.earthColumns)] for y in range(self.earthRows)]
        for x in range(len(self.Entity[0])):
            for y in range(len(self.Entity)):
                neighbors = 0
                if x > 0 and y > 0:
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if not i == j == 0:
                                if x + i >= 0:
                                    if x + i <= len(self.Entity[0]):
                                        if y + j >= 0:
                                            if y + j <= len(self.Entity):
                                                try:
                                                    if self.Entity[x + j][y + i] == 1:
                                                        neighbors += 1
                                                except IndexError:
                                                    print("x", x, "y", y, "i", i, "j", j)
        print("col", len(self.Entity[0]), "row", len(self.Entity))

    def upd(self):
        live = False
        for x in range(len(self.Entity[0])):
            for y in range(len(self.Entity)):
                neighbors = 0
                if x > 0 and y > 0:
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if not i == j == 0:
                                if x + i >= 0:
                                    if x + i <= len(self.Entity[0]):
                                        if y + j >= 0:
                                            if y + j <= len(self.Entity):
                                                try:
                                                    if self.Entity[x + j][y + i] == 1:
                                                        neighbors += 1
                                                except IndexError:
                                                    print("x", x, "y", y, "i", i, "j", j)
        if self.Entity[x][y] == 1:
            if neighbors == 2 or neighbors == 3:
                live = True
        elif self.Entity[x][y] == 0:
            if neighbors == 3:
                live = True
        if live:
            self.Entity[x][y] = 1
        else:
            self.Entity[x][y] = 0
