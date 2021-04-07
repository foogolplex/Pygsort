import pygame
import time
import bubblesort, mergesort, quicksort, drawing
import random

nums = []
def generate_nums():
    for i in range(49):
        nums.append(random.randint(50, 600))

def is_sorted(nums):
    for i in range(len(nums)):
        if i != len(nums) - 1:
            if nums[i + 1] < nums[i]:
                return False
    return True

def insertionsort(mainSurface, font):
    i = 1
    sorted_flag = False

    nums.clear()
    generate_nums()

    while(sorted_flag == False and i != len(nums)):
        # Check for events during loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    bubblesort.bubblesort(mainSurface, font)
                    return 0
                elif event.key == pygame.K_2:
                    insertionsort(mainSurface, font)
                    return 0
                elif event.key == pygame.K_3:
                    mergesort.mergesort(mainSurface, font)
                    return 0
                elif event.key == pygame.K_4:
                    quicksort.quicksort(mainSurface, font)
                    return 0

        # Refresh color to clear surface
        mainSurface.fill(drawing.black)

        drawing.draw_top(mainSurface, 2, font)

        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            temp = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = temp
            drawing.draw_bars(nums, mainSurface, j)
            pygame.display.flip()
            time.sleep(0.01)
            j -= 1
        sorted_flag = is_sorted(nums)
        i += 1

        # Draw rectangles and refresh
        drawing.draw_bars(nums, mainSurface, i)
        pygame.display.flip()
        time.sleep(0.2)
