import pygame
import time
import drawing, insertionsort, mergesort, quicksort
import random

nums = []
def generate_nums():
    for i in range(49):
        nums.append(random.randint(50, 500))

def sort_iteration(nums, i):
    if nums[i + 1] < nums[i]:
        temp = nums[i]
        nums[i] = nums[i + 1]
        nums[i + 1] = temp

def is_sorted(nums):
    for i in range(len(nums)):
        if i != len(nums) - 1:
            if nums[i + 1] < nums[i]:
                return False
    return True

def bubblesort(mainSurface, font):
    nums.clear()
    generate_nums()
    bool_sorted = False
    index = 0

    while(bool_sorted == False):
        # Check for events during loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    bubblesort(mainSurface, font)
                    return 0
                elif event.key == pygame.K_2:
                    insertionsort.insertionsort(mainSurface, font)
                    return 0
                elif event.key == pygame.K_3:
                    mergesort.mergesort(mainSurface, font)
                    return 0
                elif event.key == pygame.K_4:
                    quicksort.quicksort(mainSurface, font)
                    return 0


        # Refresh color to clear surface 
        mainSurface.fill(drawing.black)

        drawing.draw_top(mainSurface, 1, font)

        # Bubblesort iteration and sorted flag
        if index < len(nums) - 1:
            sort_iteration(nums, index)
        bool_sorted = is_sorted(nums)

        # Draw rectangles and refresh
        drawing.draw_bars(nums, mainSurface, index)
        pygame.display.flip()
        index += 1
        if index > len(nums):
            index = 0
        time.sleep(0.001)