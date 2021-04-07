import pygame

selectedcolor = pygame.Color(255, 255, 255)
rectcolor = pygame.Color(255, 0, 0)
black = pygame.Color(0, 0, 0)

def draw_bars(nums, mainSurface, index):
    for i in range(len(nums)):
        rect_width = (float(mainSurface.get_width()) / float(len(nums))) - 1
        rectangle = pygame.Rect(float(i) + float((i * rect_width)), mainSurface.get_height() - nums[i], float(rect_width), nums[i])
        if i != index:
            pygame.draw.rect(mainSurface, rectcolor, rectangle)
        else:
            pygame.draw.rect(mainSurface, selectedcolor, rectangle)

def draw_top(mainSurface, index, font):
    bubblecolor = insertioncolor = mergecolor = quickcolor = rectcolor

    if index == 1:
        bubblecolor = selectedcolor
    elif index == 2:
        insertioncolor = selectedcolor
    elif index == 3:
        mergecolor = selectedcolor
    elif index == 4:
        quickcolor = selectedcolor

    UI_1 = font.render('1 - bubble sort', True, bubblecolor)
    UI_2 = font.render('2 - insertion sort', True, insertioncolor)
    UI_3 = font.render('3 - merge sort', True, mergecolor)
    UI_4 = font.render('4 - quick sort', True, quickcolor)

    mainSurface.blit(UI_1, (20, 20))
    mainSurface.blit(UI_2, (200, 20))
    mainSurface.blit(UI_3, (380, 20))
    mainSurface.blit(UI_4, (560, 20))
