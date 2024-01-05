import pygame
from pygame import mixer

pygame.init()

# variables to set the size of the main window
windowWidth = 539
windowHeight = 286

frame = 0  # Not the FPS but the frame of our animation
gravity = 0
floor = 160
FPS = 60
clock = pygame.time.Clock()  # Create a clock object

moving = False
mousePressed = False
sprite_speed = 3
gameState = "menu"

sprite1Display = pygame.image.load("Knight1.png")

spritesrectwidth = 64
spritesrectheight = 64
sprite1rect = pygame.Rect(100, 220, spritesrectwidth, spritesrectheight)
spriteCoords = (100, 100)
sprite_speed = 3

# Initial position of sprite1Display
x_position_display1 = 0
y_position_display1 = 85

# Initial position of sprite2Display
x_position_display2 = 140
y_position_display2 = 57

# Initial position of sprite3Display
x_position_display3 = 320
y_position_display3 = 60

mouseX, mouseY = pygame.mouse.get_pos()


#Menu Window dimensions and background
menuwindow = pygame.display.set_mode((windowWidth, windowHeight))
menubackground_image = pygame.image.load("OpenGrass.jpg")

#Main Window dimensions and background
mainwindow = pygame.display.set_mode((windowWidth, windowHeight))
mainbackground_image = pygame.image.load("PlayingBackground.png")


sprite1 = pygame.image.load("Knight1.png")
sprite1rect = sprite1.get_rect()  # Returns information about our sprite1
sprite2 = pygame.image.load("Knight2.png")
sprite2rect = sprite2.get_rect()  # Returns information about our sprite2

# Choosing Characters Pictures
sprite1Display = pygame.image.load("Knight1.png")
sprite1Displayrect = sprite1Display.get_rect()  # Returns information about our sprite1

sprite2Display = pygame.image.load("Knight2.png")
sprite2Displayrect = sprite2Display.get_rect()  # Returns information about our sprite2

sprite3Display = pygame.image.load("Knight3.png")
sprite3Displayrect = sprite3Display.get_rect()  # Returns information about our sprite3

# Idle Animations
Idle1Knight1 = pygame.image.load("Idle animation1 knight1.png")
Idle2Knight1 = pygame.image.load("Idle animation2 knight1.png")
Idle3Knight1 = pygame.image.load("Idle animation3 knight1.png")
Idle4Knight1 = pygame.image.load("Idle animation4 knight1.png")
Idle5Knight1 = pygame.image.load("Idle animation5 knight1.png")

Idle1Knight2 = pygame.image.load("Idle Animation1 Knight2.png")
Idle2Knight2 = pygame.image.load("Idle Animation2 Knight2.png")
Idle3Knight2 = pygame.image.load("Idle Animation3 Knight2.png")
Idle4Knight2 = pygame.image.load("Idle Animation4 Knight2.png")
Idle5Knight2 = pygame.image.load("Idle Animation5 Knight2.png")

Idle1Knight3 = pygame.image.load("Idle Animation1 Knight3.png")
Idle2Knight3 = pygame.image.load("Idle Animation2 Knight3.png")
Idle3Knight3 = pygame.image.load("Idle Animation3 Knight3.png")
Idle4Knight3 = pygame.image.load("Idle Animation4 Knight3.png")
Idle5Knight3 = pygame.image.load("Idle Animation5 Knight3.png")


# Running Animations
Running1Knight1 = pygame.image.load("Running Animation1 Knight1.png")
Running2Knight1 = pygame.image.load("Running Animation2 Knight1.png")
Running3Knight1 = pygame.image.load("Running Animation3 Knight1.png")
Running4Knight1 = pygame.image.load("Running Animation4 Knight1.png")
Running5Knight1 = pygame.image.load("Running Animation5 Knight1.png")
Running6Knight1 = pygame.image.load("Running Animation6 Knight1.png")
Running7Knight1 = pygame.image.load("Running Animation7 Knight1.png")
Running8Knight1 = pygame.image.load("Running Animation8 Knight1.png")

font_path1 = "DUNGEONFONT.ttf"
font1 = pygame.font.Font(font_path1, 35)

font_path2 = "TITLEFONT.otf"
font2 = pygame.font.Font(font_path2, 40)

#Background Music
pygame.mixer.music.load("DungeonMusic.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1) # The value -1 keeps it so it loops the bg music forever



# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()  # Update mouse coordinates on button press
            mousePressed = True
            
    # Game States if statements
    if gameState == "menu":
        if mousePressed == True:
            # Checking if our boxes are pressed and if they are, switch the gamestate accordingly
            if mouseX > 5 and mouseX < 155 and mouseY > 240 and mouseY < 290:
                gameState = "Axe Warrior Playing"
                print(gameState)
            elif mouseX > 175 and mouseX < 325 and mouseY > 240 and mouseY < 290:
                gameState = "Brave Knight Playing"
                print(gameState)
            elif mouseX > 345 and mouseX < 495 and mouseY > 240 and mouseY < 290:
                gameState = "Dark Knight Playing"
                print(gameState)

                
        # Drawing the background for the menu window
        menuwindow.blit(menubackground_image, (0, 0))
        
        pygame.draw.rect(menuwindow, pygame.Color("white"), (5, 240, 150, 50)) # The Box
        instrText = font1.render("Axe Warrior", 1, "black")
        menuwindow.blit(instrText, (15, 245)) # The Text
        
        pygame.draw.rect(menuwindow, pygame.Color("white"), (175, 240, 150, 50)) # The Box
        instrText = font1.render("Brave Knight", 1, "black")
        menuwindow.blit(instrText, (185, 245)) # The Text
        
        pygame.draw.rect(menuwindow, pygame.Color("white"), (345, 240, 150, 50)) # The Box
        instrText = font1.render("Dark Knight", 1, "black")
        menuwindow.blit(instrText, (355, 245)) # The Text
        
        menutitleText = font2.render("Choose Your Character", 1, "black")
        menuwindow.blit(menutitleText, (40, 20))


        menuwindow.blit(sprite1Display, (x_position_display1, y_position_display1))  
        menuwindow.blit(sprite2Display, (x_position_display2, y_position_display2)) 
        menuwindow.blit(sprite3Display, (x_position_display3, y_position_display3))
        
        mousePressed = False  # Reset the flag after processing the click

        
    elif gameState == "Axe Warrior Playing":
        if mousePressed == True:
            # Drawing the background for the menu window
            mainwindow.blit(mainbackground_image, (0, 0))
            mainwindow.blit(sprite1, sprite1rect.topleft)  # Use topleft attribute for blit


    # *********GAME LOGIC**********
    # Setting our keybinds to see if the specific key is pressed to subtract or add to the Sprites x and y coordinates
    # to move by sprite speed variable that we created
    moving = False  # Reset moving flag
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        sprite1rect.x += sprite_speed
        moving = True
    elif key[pygame.K_a]:
        sprite1rect.x -= sprite_speed
        moving = True
    elif key[pygame.K_SPACE]:
        sprite1rect.y -= sprite_speed
    else:
        sprite1rect.y += gravity

    # Causes our character to fall
    gravity += 1
    # Stops our sprite from falling when it hits the coordinates that we chose for the floor
    if sprite1rect.y > floor:
        gravity = 0
        sprite1rect.y = floor
    # Making our sprite jump
    if key[pygame.K_SPACE] and sprite1rect.y == floor:
        gravity = -12


    frame = frame + 1
    
    # Running Animation logic
    if moving == True:
        if frame == 0:
            sprite1 = pygame.transform.scale(Running1Knight1, spriteCoords)
        elif frame == 7:
            sprite1 = pygame.transform.scale(Running2Knight1, spriteCoords)
        elif frame == 14:
            sprite1 = pygame.transform.scale(Running3Knight1, spriteCoords)
        elif frame == 21:
            sprite1 = pygame.transform.scale(Running4Knight1, spriteCoords)
        elif frame == 28:
            sprite1 = pygame.transform.scale(Running5Knight1, spriteCoords)
        elif frame == 35:
            sprite1 = pygame.transform.scale(Running6Knight1, spriteCoords)
        elif frame == 42:
            sprite1 = pygame.transform.scale(Running7Knight1, spriteCoords)
        elif frame == 49:
            sprite1 = pygame.transform.scale(Running8Knight1, spriteCoords)
            frame = 0
    else:
        # Idle Animation
        if frame == 0:
            sprite1 = pygame.transform.scale(Idle1Knight1, spriteCoords)
        elif frame == 10:
            sprite1 = pygame.transform.scale(Idle2Knight1, spriteCoords)
        elif frame == 20:
            sprite1 = pygame.transform.scale(Idle3Knight1, spriteCoords)
        elif frame == 30:
            sprite1 = pygame.transform.scale(Idle4Knight1, spriteCoords)
        elif frame == 40:
            sprite1 = pygame.transform.scale(Idle5Knight1, spriteCoords)
            frame = 0
    if frame > 49:
        frame = 0
        
    # Giving our game boundaries
    if sprite1rect.x <= 0:
        sprite1rect.x = 0
    elif sprite1rect.x >= windowWidth - 64:
        sprite1rect.x = windowWidth - 64
        
    # Display Animation for characters
    if moving == False:
        if frame == 0:
            sprite1Display = pygame.transform.scale(Idle1Knight1, (200,200))
        elif frame == 10:
            sprite1Display = pygame.transform.scale(Idle2Knight1, (200,200))
        elif frame == 20:
            sprite1Display = pygame.transform.scale(Idle3Knight1, (200,200))
        elif frame == 30:
            sprite1Display = pygame.transform.scale(Idle4Knight1, (200,200))
        elif frame == 40:
            sprite1Display = pygame.transform.scale(Idle5Knight1, (200,200))
            frame = 0
    if frame > 40:
        frame = 0
        
    if moving == False:
        if frame == 0:
            sprite2Display = pygame.transform.scale(Idle1Knight2, (270,270))
        elif frame == 10:
            sprite2Display = pygame.transform.scale(Idle2Knight2, (270,270))
        elif frame == 20:
            sprite2Display = pygame.transform.scale(Idle3Knight2, (270,270))
        elif frame == 30:
            sprite2Display = pygame.transform.scale(Idle4Knight2, (270,270))
        elif frame == 40:
            sprite2Display = pygame.transform.scale(Idle5Knight2, (270,270))
            frame = 0
    if frame > 40:
        frame = 0
        
    if moving == False:
        if frame == 0:
            sprite3Display = pygame.transform.scale(Idle1Knight3, (270,270))
        elif frame == 10:
            sprite3Display = pygame.transform.scale(Idle2Knight3, (270,270))
        elif frame == 20:
            sprite3Display = pygame.transform.scale(Idle3Knight3, (270,270))
        elif frame == 30:
            sprite3Display = pygame.transform.scale(Idle4Knight3, (270,270))
        elif frame == 40:
            sprite3Display = pygame.transform.scale(Idle5Knight3, (270,270))
            frame = 0
    if frame > 40:
        frame = 0

        
    # *********DRAW THE FRAME**********
    pygame.display.flip()
    clock.tick(FPS)  # Force frame rate to 60fps or lower
