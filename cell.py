import pygame
from colors import *
from fonts import *

CELL_WIDTH = 30

# 16 x 30 cells
# 99 mines
GRID_WIDTH = 30
GRID_HEIGHT = 16

class Cell :
    def __init__(self, i, j, mine, rect) :
        self.i = i
        self.j = j
        self.x = i * CELL_WIDTH
        self.y = j * CELL_WIDTH
        self.mine = mine
        self.rect = rect
        self.revealed = False
        self.neighborMines = 0


    def countNeighborMines(self, grid) :
        if self.mine :
            self.neighborMines = -1
            return -1
        else :
            total = 0
            for xoff in range(-1,2) :
                for yoff in range(-1,2) :
                    i = self.i + xoff
                    j = self.j + yoff

                    if i > -1 and i < GRID_WIDTH and j > -1 and j < GRID_HEIGHT :
                        neighbor = grid[i][j]
                        if (neighbor.mine) :
                            total += 1

            self.neighborMines = total
            return total
    

    def reveal(self, WIN, grid) :
        self.revealed = True

        if self.mine == True :
            drawMine(self, WIN)
            return -1
        else :
            drawEmptyCell(self, WIN, grid)
            if self.neighborMines == 0 :
                for xoff in range(-1,2) :
                    for yoff in range(-1,2) :
                        i = self.i + xoff
                        j = self.j + yoff

                        if i > -1 and i < GRID_WIDTH and j > -1 and j < GRID_HEIGHT :
                            if grid[i][j].mine == False and grid[i][j].revealed == False:
                                grid[i][j].reveal(WIN, grid)
        return 0 


def drawMine(cell, WIN) :
    pygame.draw.circle(WIN, RED, (cell.x + CELL_WIDTH/2, cell.y + CELL_WIDTH/2), 10)

    pygame.display.update() 


def drawEmptyCell(cell, WIN, grid) :
    cell.rect = pygame.draw.rect(WIN, LIGHT_GRAY, cell.rect)
    minesText = COMIC_SANS.render(str(cell.countNeighborMines(grid)), 1, BLACK)
    if cell.neighborMines != 0 :
        WIN.blit(minesText, (cell.x + 5, cell.y - 6))
    
    pygame.display.update() 


