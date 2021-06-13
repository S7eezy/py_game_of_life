import pygame
import time
import scipy
import numpy as np
from scipy import signal

class Earth:
    def __init__(self, width, height, scale, density):
        self.earthColumns = int(width/scale)
        self.earthRows = int(height/scale)
        self.Entity = np.random.choice([1, 0], self.earthColumns*self.earthRows, p=[cellDensity/100, 1-cellDensity/100]).reshape(self.earthColumns, self.earthRows)
        counts = scipy.signal.convolve2d(self.Entity, comparison, mode='same')
        self.upd(counts, displayNeighborsText)

    def upd(self, counts, displayText):
        for x in range(len(counts)):
            for y in range(len(counts[0])):
                rect = [x * cellSize, y * cellSize, cellSize, cellSize]

                if self.Entity[x][y] == 1:
                    if counts[x][y] == 2 or counts[x][y] == 3:
                        pass
                    else:
                        self.Entity[x][y] = 0

                elif self.Entity[x][y] == 0:
                    if counts[x][y] == 3:
                        self.Entity[x][y] = 1

                if self.Entity[x][y] == 1:
                    pygame.draw.rect(monitorDisplay, (51, 204, 255), rect)
                else:
                    pygame.draw.rect(monitorDisplay, (0, 0, 0), rect)
                    pygame.draw.rect(monitorDisplay, (5, 5, 5), rect, 1)
                if displayText:
                    font = pygame.font.SysFont('arial', 10)
                    text = font.render(str(counts[x][y]), False, (50,50,50))
                    monitorDisplay.blit(text, (x*cellSize, y*cellSize))
if __name__ == '__main__':

    cellSize = 10
    cellDensity = 20
    displayNeighborsText = False

    comparison = np.ones((3, 3))
    comparison[1][1] = 0

    pygame.init()
    pygame.display.set_caption("Steezy introduce CONWAY's Game of Life")
    monitorSpecs = pygame.display.Info()
    monitorDisplay = pygame.display.set_mode([monitorSpecs.current_w, monitorSpecs.current_h])

    Earth = Earth(width=monitorSpecs.current_w, height=monitorSpecs.current_h, scale=cellSize, density=cellDensity)

    while True:
        time.sleep(0.01)
        counts = scipy.signal.convolve2d(Earth.Entity, comparison, mode='same')
        Earth.upd(counts, displayNeighborsText)
        pygame.display.update()

