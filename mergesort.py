import random
import time
import insertionsort, bubblesort, quicksort, drawing
import pygame

def generate_nums():
    for i in range(49):
        nums.append(random.randint(50, 600))

def is_sorted(nums):
    for i in range(len(nums)):
        if i != len(nums) - 1:
            if nums[i + 1] < nums[i]:
                return False
    return True

def mergesort(mainSurface, font):
    sorted_flag = False
    while(sorted_flag == False):
        # Check for events during loop
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        bubblesort.bubblesort(mainSurface, font)
                        return 0
                    elif event.key == pygame.K_2:
                        insertionsort.insertionsort(mainSurface, font)
                        return 0
                    elif event.key == pygame.K_3:
                        mergesort(mainSurface, font)
                        return 0
                    elif event.key == pygame.K_4:
                        quicksort.quicksort(mainSurface, font)
                        return 0
        drawing.draw_top(mainSurface, 3, font)
        pygame.display.flip()