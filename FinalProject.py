import pygame
from pygame import mixer

pygame.init()

# variables to set the size of the main window
windowWidth = 539
windowHeight = 286

moving = False
mousePressed = False
sprite_speed = 3
gameState = "menu"

menuwindow = pygame.display.set_mode((windowWidth, windowHeight))
mouseX, mouseY = pygame.mouse.get_pos()
background_image = pygame.image.load("OpenGrass.jpg")

sprite1 = pygame.image.load("Knight1.png")

# Idle Animations
Idle1Knight1 = pygame.image.load("Idle animation1 knight1.png")
Idle2Knight1 = pygame.image.load("Idle animation2 knight1.png")
Idle3Knight1 = pygame.image.load("Idle animation3 knight1.png")
Idle4Knight1 = pygame.image.load("Idle animation4 knight1.png")
Idle5Knight1 = pygame.image.load("Idle animation5 knight1.png")

# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    for event in pygame.event.get():  # Iterate over the list of events
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            mousePressed = True
        else:
            mousePressed = False
            
        #Game States if statements
        if gameState == "menu":
            # Drawing the background for the menu window
            menuwindow.blit(background_image, (0, 0))
            
    pygame.display.flip()
pygame.quit()
    
    
    
    
    
