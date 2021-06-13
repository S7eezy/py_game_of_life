import pygame
import time
import earth

def updateAlive(Earth):
    print("COL:", len(Earth.Entity[0]), "ROW:", len(Earth.Entity))
    for col in range(len(Earth.Entity[0])):  # ligne
        for row in range(len(Earth.Entity)):  # colonne
            Earth.upd()
            rect = [col * cellSize, row * cellSize, cellSize, cellSize]
            if Earth[col][row] == 1:
                pygame.draw.rect(monitorDisplay, (51, 204, 255), rect)
            else:
                pygame.draw.rect(monitorDisplay, (0, 0, 0), rect)
                pygame.draw.rect(monitorDisplay, (5, 5, 5), rect, 1)

if __name__ == '__main__':

    cellSize = 300
    cellDensity = 10

    pygame.init()
    pygame.display.set_caption("Steezy introduce CONWAY's Game of Life")
    monitorSpecs = pygame.display.Info()
    monitorDisplay = pygame.display.set_mode([monitorSpecs.current_w, monitorSpecs.current_h])

    Earth = earth.Earth(width=monitorSpecs.current_w, height=monitorSpecs.current_h, scale=cellSize, density=cellDensity)

    while True:
        time.sleep(0.01)
        updateAlive(Earth)
        pygame.display.update()

