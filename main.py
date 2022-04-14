import math
import pygame

winX = 1000
winY = 1000
win = pygame.display.set_mode((winX, winY))
pygame.display.set_caption("Trigonometry")

# side1
side1 = int(input("Side 1 length: ", ))  # changes the length
angle1 = int(input("Angle 1 input: ", ))  # changes the angle
startX = 200
startY = 700
startPos1 = (startX, startY)
distanceX1 = (side1 * (math.cos(math.radians(angle1))))  # distance in the x direction (eg 7cos30)
distanceY1 = (side1 * (math.sin(math.radians(angle1))))  # distance in the y direction (eg 10sin50)
endX1 = (startX + distanceX1)  # moving right in the x axis
endY1 = (startY - distanceY1)  # moving down in the y axis
endPos1 = (endX1, endY1)

# side2
side2 = int(input("Side 2 length: ", ))  # changes the side length
angle2 = int(input("Angle 2 input: ", ))  # changes the side angle
startPos2 = endPos1
distanceX2 = (side2 * (math.cos(math.radians(angle2))))
# the distance it changes in the x axis is the cos of the angle times the length of the line
distanceY2 = (side2 * (math.sin(math.radians(angle2))))  # same as above but using sin instead
endPos2 = (endX1 + distanceX2, endY1 + distanceY2)  # moves down and right

# side3
side3Len = (math.sqrt((side1 ** 2) + (side2 ** 2)))  # pythagoras theorem to find the final distance
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
        win.fill((255, 255, 255))
        pygame.draw.line(win, (255, 0, 0), startPos1, endPos1, width=5)
        pygame.draw.line(win, (0, 255, 0), startPos2, endPos2, width=5)
        pygame.draw.line(win, (0, 0, 255), startPos3, endPos3, width=5)
        pygame.draw.circle(win, (200, 0, 170), startPos1, 10, 0)
        pygame.draw.circle(win, (255, 255, 0), startPos2, 10, 0)
        pygame.draw.circle(win, (0, 255, 255), startPos3, 10, 0)
        pygame.display.update()
