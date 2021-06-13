import pygame
import time
import scipy
import numpy as np
from scipy import signal

# @Earth       : Numpy Grid
# @Earth.upd() : Compute neighbors count through 2d convolution
class Earth:
    def __init__(self, width, height, scale, density):
        self.earthColumns = int(width/scale)
        self.earthRows = int(height/scale)

        # 1: Living cell, 0: Dead cell
        # Density can be set in __main__
        self.Entity = np.random.choice([1, 0], self.earthColumns*self.earthRows, p=[cellDensity/100, 1-cellDensity/100]).reshape(self.earthColumns, self.earthRows)

        # Compute neighbors by comparing every cell with a 3*3 ones matrix
        counts = scipy.signal.convolve2d(self.Entity, comparison, mode='same')
        self.upd(counts, displayNeighborsText)

    def upd(self, counts, displayText):

        # Iterate through the whole board
        for x in range(len(counts)):
            for y in range(len(counts[0])):

                # pygame.draw.rect takes a rect as an argument: (posX, posY, width, height)
                rect = [x * cellSize, y * cellSize, cellSize, cellSize]

                # Rule 1: if a cell is living and is surrounded by 2 or 3 living cells, it survives
                if self.Entity[x][y] == 1:
                    if counts[x][y] == 2 or counts[x][y] == 3:
                        pass
                    else:
                        self.Entity[x][y] = 0

                # Rule 2: if a cell is dead and is surrounded by 3 living cells, it comes back to life
                elif self.Entity[x][y] == 0:
                    if counts[x][y] == 3:
                        self.Entity[x][y] = 1

                # If no rule is respected, the cell is dead upon the next iteration

                # Draws a cell on the display, blue if the cell is living, black if the cell is dead
                if self.Entity[x][y] == 1:
                    pygame.draw.rect(monitorDisplay, (51, 204, 255), rect)
                else:
                    pygame.draw.rect(monitorDisplay, (0, 0, 0), rect)
                    pygame.draw.rect(monitorDisplay, (5, 5, 5), rect, 1)

                # If the boolean is set to true in __main_, display the number of neighbors in real time
                if displayText:
                    font = pygame.font.SysFont('arial', 10)
                    text = font.render(str(counts[x][y]), False, (50,50,50))
                    monitorDisplay.blit(text, (x*cellSize, y*cellSize))

if __name__ == '__main__':

    # Useful parameters to edit your simulation
    # @cellSize: sets the width and height of each cell in pixels
    # @cellDensity: gives the percentage used for the distribution of initial living cells
    # @displayNeighborsText: display the amount of neighbors in real time
    cellSize = 10
    cellDensity = 20
    displayNeighborsText = False

    # Comparison matrix for the 2d convolution
    comparison = np.ones((3, 3))
    # The center cell is set to zero so the current cell doesn't count itself as a neighbor
    comparison[1][1] = 0

    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")
    monitorSpecs = pygame.display.Info()
    # Sets the size of the window according to the screen resolution
    monitorDisplay = pygame.display.set_mode([monitorSpecs.current_w, monitorSpecs.current_h])

    # Create the grid object
    Earth = Earth(width=monitorSpecs.current_w, height=monitorSpecs.current_h, scale=cellSize, density=cellDensity)

    # Main loop
    while True:
        time.sleep(0.01)
        counts = scipy.signal.convolve2d(Earth.Entity, comparison, mode='same')
        Earth.upd(counts, displayNeighborsText)
        pygame.display.update()

