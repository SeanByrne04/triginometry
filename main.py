import pygame
import math


winX = 1000
winY = 1000
win = pygame.display.set_mode((winX, winY))
pygame.display.set_caption("Trigonometry & Shit")


# side1
side1 = 300  # changes the lenght
angle1 = 60  # changes the angle
startX = 200
startY = 700
startPos1 = (startX, startY)
distanceX1 = (side1 * (math.cos(math.radians(angle1))))  # distance in the x direction (eg 7cos30)
distanceY1 = (side1 * (math.sin(math.radians(angle1))))  # distance in the y direction (eg 10sin50)
endX1 = (startX + distanceX1)
endY1 = (startY - distanceY1)
endPos1 = (endX1, endY1)

# side2
side2 = 500  # changes the side length
angle2 = 30  # changes the side angle
startPos2 = endPos1
distanceX2 = (side2 * (math.cos(math.radians(angle2))))
distanceY2 = (side2 * (math.sin(math.radians(angle2))))
endPos2 = (endX1 + distanceX2, endY1 + distanceY2)

# side3
side3Len = (math.sqrt((side1 ** 2) + (side2 ** 2))) # pythagros therom to find the final distance
angle3 = 180 - (angle1 + angle2)
startPos3 = endPos2
endPos3 = startPos1
print("len=", side3Len)
print("angle", angle3)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.init()
        pygame.draw.line(win, (255, 255, 255), startPos1, endPos1, width=5)
        pygame.draw.line(win, (255, 255, 255), startPos2, endPos2, width=5)
        pygame.draw.line(win, (255, 255, 255), startPos3, endPos3, width=5)
        pygame.display.update()
