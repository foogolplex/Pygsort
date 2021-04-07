import pygame
import time
import insertionsort, bubblesort, quicksort, mergesort, drawing
from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_caption("algorchan")
    
    alive = True
    font = pygame.font.SysFont(None, 24)
    mainSurface = pygame.display.set_mode((1024, 768))
    while(alive == True):
        drawing.draw_top(mainSurface, 0, font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    bubblesort.bubblesort(mainSurface, font)
                elif event.key == pygame.K_2:
                    insertionsort.insertionsort(mainSurface, font)
                elif event.key == pygame.K_3:
                    mergesort.mergesort(mainSurface, font)
                elif event.key == pygame.K_4:
                    quicksort.quicksort(mainSurface, font)
        pygame.display.flip()
main()