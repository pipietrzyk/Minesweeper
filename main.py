import pygame
import os
import random
from cell import *
from colors import *


# Draw the window
WIN = pygame.display.set_mode((CELL_WIDTH * GRID_WIDTH, CELL_WIDTH * GRID_HEIGHT))
WIN.fill(WHITE)
pygame.display.set_caption('MINESWEEPER')

# 2d array which will hold the grid
grid = []

# number of mines in the game
MINES = 99


# set up the canvas and the game board
def setup() :

    # create the 2d array that will represent the game grid and fill it with cells
    for i in range(GRID_WIDTH):
        col = []
        for j in range(GRID_HEIGHT):
            col.append(Cell(i, j, False, pygame.draw.rect(WIN, BLACK, pygame.Rect(i * CELL_WIDTH, j * CELL_WIDTH, CELL_WIDTH, CELL_WIDTH), 2)))
        grid.append(col)

    pygame.display.update() 


def endGame() :
    for row in grid :
        for cell in row :
            cell.reveal(WIN, grid)


# always make the 9x9 area where the mouse is clicked devoid of mines
def startGame(mx, my) :
    for row in grid :
        for cell in row :
            if mx > cell.x and mx < cell.x + CELL_WIDTH and my > cell.y and my < cell.y + CELL_WIDTH : 
                startCell = cell

    mineSpots = []
    for i in range(0, GRID_WIDTH) :
        for j in range(0, GRID_HEIGHT) :
            mineSpots.append(grid[i][j])

    for xoff in range(-1,2) :
        for yoff in range(-1,2) :
            i = startCell.i + xoff
            j = startCell.j + yoff
            if i > -1 and i < GRID_WIDTH and j > -1 and j < GRID_HEIGHT :
                mineSpots.remove(grid[i][j])


    for m in range(0, MINES) :
        index = random.randrange(0, len(mineSpots))
        curCell = mineSpots[index]
        grid[curCell.i][curCell.j].mine = True
        mineSpots.remove(curCell)

    if startCell.reveal(WIN, grid) == -1 :
        endGame()
        


def main() :

    setup()

    gameStarted = False
    run = True
    while run :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        
            # when the mouse is first pressed on a cell begin the game
            if event.type == pygame.MOUSEBUTTONUP and not gameStarted :
                gameStarted = not gameStarted
                (mx, my) = pygame.mouse.get_pos()
                startGame(mx, my)

            # handle clicking on a cell
            elif event.type == pygame.MOUSEBUTTONUP:
                (mx, my) = pygame.mouse.get_pos()

                if event.button == 1 :
                    for row in grid :
                        for cell in row :
                            if mx > cell.x and mx < cell.x + CELL_WIDTH and my > cell.y and my < cell.y + CELL_WIDTH :
                                if cell.reveal(WIN, grid) == -1 :
                                    endGame()
                elif event.button == 3 :
                    for row in grid :
                        for cell in row :
                            if mx > cell.x and mx < cell.x + CELL_WIDTH and my > cell.y and my < cell.y + CELL_WIDTH :
                                cell.placeFlag(WIN)

    
    pygame.quit()

if __name__ == "__main__" :
    main()
  