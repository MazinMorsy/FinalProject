import pygame
from pygame import mixer

pygame.init()

# variables to set the size of the main window
windowWidth = 539
windowHeight = 286

frame = 0  # Not the FPS but the frame of our animation
gravity = 0
FPS = 60
gravity = 0
current_time = 0  # Initialize the timer variable
clock = pygame.time.Clock()  # Create a clock object

moving = False
mousePressed = False
sprite_speed = 3
gameState = "IntroScreen"

sprite1Display = pygame.image.load("Knight1.png")

spritesRectwidth = 64
spritesRectheight = 64
sprite1rect = pygame.Rect(100, 185, spritesRectwidth, spritesRectheight)
floor = 185
spriteSize = (64, 64)
sprite_speed = 3
SpacePressed = False  # Initialize SpacePressed variable
MonsterRoar = pygame.mixer.Sound("TitanROAR.wav")
MonsterRoarPlayed = False

doorsrectwidth = 64
doorsrectheight = 64
Doorrect = pygame.Rect(485,110, doorsrectwidth,doorsrectheight )

# Initial position of sprite1Display
x_position_display1 = 0
y_position_display1 = 85

# Initial position of sprite2Display
x_position_display2 = 140
y_position_display2 = 57

# Initial position of sprite3Display
x_position_display3 = 320
y_position_display3 = 60

mouseX, mouseY = pygame.mouse.get_pos() # Getting the position of our mouse

#Intro Window dimensions and background
Introwindow = pygame.display.set_mode((windowWidth, windowHeight))
Introbackground_image = pygame.image.load("IntroBackground.jpg")

#Menu Window dimensions and background
menuwindow = pygame.display.set_mode((windowWidth, windowHeight))
menubackground_image = pygame.image.load("OpenGrass.jpg")

#Main Window dimensions and background
mainwindow = pygame.display.set_mode((windowWidth, windowHeight))
mainbackground_image = pygame.image.load("PlayingBackground.png")

#Game Intro Window dimensions and background
GameIntrowindow = pygame.display.set_mode((windowWidth, windowHeight))
GameIntroScreenbg = pygame.image.load("GameIntroScreen.png")

# Instructions window bg
InstructionsWindowbg = pygame.image.load("starrysky.png")


sprite1 = pygame.image.load("Knight1.png")
sprite1rect = sprite1.get_rect()  # Returns information about our sprite1
sprite2 = pygame.image.load("Knight2.png")
sprite2rect = sprite2.get_rect()  # Returns information about our sprite2
sprite3 = pygame.image.load("Knight3.png")
sprite3rect = sprite3.get_rect()  # Returns information about our sprite2


FrogEnemy = pygame.image.load("FrogEnemyRun1.png")
FrogEnemyrect = FrogEnemy.get_rect() # Returns information about our FrogEnemy

Heart1 = pygame.image.load("Heart1.png")
Heart2 = pygame.image.load("Heart2.png")
Heart3 = pygame.image.load("Heart3.png")

Door = pygame.image.load("Door.png")
Doorrect = Door.get_rect()


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


# Running Animations for our characters
Running1Knight1 = pygame.image.load("Running Animation1 Knight1.png")
Running2Knight1 = pygame.image.load("Running Animation2 Knight1.png")
Running3Knight1 = pygame.image.load("Running Animation3 Knight1.png")
Running4Knight1 = pygame.image.load("Running Animation4 Knight1.png")
Running5Knight1 = pygame.image.load("Running Animation5 Knight1.png")
Running6Knight1 = pygame.image.load("Running Animation6 Knight1.png")
Running7Knight1 = pygame.image.load("Running Animation7 Knight1.png")
Running8Knight1 = pygame.image.load("Running Animation8 Knight1.png")

Running1Knight2 = pygame.image.load("Knight2RunningAnimation1.png")
Running2Knight2 = pygame.image.load("Knight2RunningAnimation2.png")
Running3Knight2 = pygame.image.load("Knight2RunningAnimation3.png")
Running4Knight2 = pygame.image.load("Knight2RunningAnimation4.png")
Running5Knight2 = pygame.image.load("Knight2RunningAnimation5.png")
Running6Knight2 = pygame.image.load("Knight2RunningAnimation6.png")
Running7Knight2 = pygame.image.load("Knight2RunningAnimation7.png")
Running8Knight2 = pygame.image.load("Knight2RunningAnimation8.png")

Running1Knight3 = pygame.image.load("RunningAnimation1Knight3.png")
Running2Knight3 = pygame.image.load("RunningAnimation2Knight3.png")
Running3Knight3 = pygame.image.load("RunningAnimation3Knight3.png")
Running4Knight3 = pygame.image.load("RunningAnimation4Knight3.png")
Running5Knight3 = pygame.image.load("RunningAnimation5Knight3.png")
Running6Knight3 = pygame.image.load("RunningAnimation6Knight3.png")
Running7Knight3 = pygame.image.load("RunningAnimation7Knight3.png")
Running8Knight3 = pygame.image.load("RunningAnimation8Knight3.png")



# Slash Attack Animations for our characters
Knight1SlashAnimation1 = pygame.image.load("Knight1SlashAnimation1.png")
Knight1SlashAnimation2 = pygame.image.load("Knight1SlashAnimation2.png")
Knight1SlashAnimation3 = pygame.image.load("Knight1SlashAnimation3.png")

Knight2SlashAnimation1 = pygame.image.load("Knight2SlashAnimation1.png")
Knight2SlashAnimation2 = pygame.image.load("Knight2SlashAnimation2.png")
Knight2SlashAnimation3 = pygame.image.load("Knight2SlashAnimation3.png")

Knight3SlashAnimation1 = pygame.image.load("Knight3SlashAnimation1.png")
Knight3SlashAnimation2 = pygame.image.load("Knight3SlashAnimation2.png")
Knight3SlashAnimation3 = pygame.image.load("Knight3SlashAnimation3.png")


font_path1 = "DUNGEONFONT.ttf"
font1 = pygame.font.Font(font_path1, 35)

font_path2 = "TITLEFONT.otf"
font2 = pygame.font.Font(font_path2, 40)

font_path3 = "TITLEFONT.otf"
font3 = pygame.font.Font(font_path2, 75)

font_path4 = "DUNGEONFONT.ttf"
font4 = pygame.font.Font(font_path1, 50)

#Background Music
pygame.mixer.music.load("DungeonMusic.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1) # The value -1 keeps it so it loops the bg music forever




# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        # Load projectile image
        original_image = pygame.image.load("Slash.png") 
        self.image =  pygame.transform.scale(original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10  # Set the projectile speed

    def update(self):
        self.rect.x += self.speed
        
# FrogEnemy class
class FrogEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.running_images = [
            pygame.image.load("FrogEnemyRun1.png"),
            pygame.image.load("FrogEnemyRun2.png"),
            pygame.image.load("FrogEnemyRun3.png"),
            # Add more frames as needed
        ]

        self.index = 0
        self.image = self.running_images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3  # Set the frog enemy speed

    def update(self):
        self.rect.x -= self.speed  # Move frog enemy towards the left

        # Update frog enemy animation
        self.index += 1
        if self.index >= len(self.running_images):
            self.index = 0
        self.image = self.running_images[self.index]

# Projectile group
projectile_group = pygame.sprite.Group()

# FrogEnemy group
frog_enemy_group = pygame.sprite.Group()


# *********GAME LOOP**********
while True:
    # *********EVENTS**********
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            if event.button == 1:  # Check for left mouse button
                if gameState == "Axe Warrior Playing":
                    new_projectile = Projectile(sprite1rect.x + sprite1rect.width, sprite1rect.y + sprite1rect.height // 2, 20, 20)
                    projectile_group.add(new_projectile)
                if gameState == "Brave Knight Playing":
                    new_projectile = Projectile(sprite2rect.x + sprite2rect.width, sprite2rect.y + sprite2rect.height // 2, 20, 20)
                    projectile_group.add(new_projectile)
                if gameState == "Dark Knight Playing":
                    new_projectile = Projectile(sprite3rect.x + sprite3rect.width, sprite3rect.y + sprite3rect.height // 2, 20, 20)
                    projectile_group.add(new_projectile)
                mousePressed = True  # Set the flag to True when the left mouse button is pressed
                
    # Update the timer
    current_time += clock.get_rawtime() / 1000


                
    # Check for collisions between projectiles and frog enemies
    frog_enemy_hit_list = pygame.sprite.groupcollide(frog_enemy_group, projectile_group, True, True)
    
    # If frog enemy is hit by a projectile, remove the frog enemy
    for frog_enemy_hit in frog_enemy_hit_list:
        # Perform any actions you want when an enemy is hit, such as playing a sound, updating score, etc.
        pass
            

    # Game States if statements            
    if gameState == "IntroScreen":
        if mousePressed == True:
            # Checking if our boxes are pressed and if they are, switch the gamestate accordingly
            if mouseX > 180 and mouseX < 380 and mouseY > 220 and mouseY < 270:
                gameState = "instructions"
                print(gameState)   
            elif mouseX > 180 and mouseX < 380 and mouseY > 150 and mouseY < 195:
                gameState = "menu"
                print(gameState)
                
        # Drawing the background for the Intro window
        Introwindow.blit(Introbackground_image, (0, 0))
        # Drawing the instructions button with text
        pygame.draw.rect(Introwindow, pygame.Color("Red"), (180, 220, 200, 50)) # The Box
        instrText = font4.render("Instructions", 1, "black")
        Introwindow.blit(instrText, (187, 220)) # The Text
        # Drawing the play button with text
        pygame.draw.rect(Introwindow, pygame.Color("firebrick"), (180, 150, 200, 50)) # The Box
        playText = font4.render("Play", 1, "black")
        Introwindow.blit(playText, (234, 145)) # The Text
    
        word1 = "Dungeon"
        renderedText = font3.render(word1, 1, pygame.Color("red"))
        Introwindow.blit(renderedText, (10,10))
        word2 = "Survival"
        renderedText = font3.render(word2, 1, pygame.Color("firebrick"))
        Introwindow.blit(renderedText, (80,60))
    
    
    elif gameState == "menu":
        if mousePressed == True:
            # Checking if our boxes are pressed and if they are, switch the gamestate accordingly
            if mouseX > 5 and mouseX < 155 and mouseY > 240 and mouseY < 290:
                gameState = "Axe Warrior Play GIS"
                print(gameState)
            elif mouseX > 175 and mouseX < 325 and mouseY > 240 and mouseY < 290:
                gameState = "Brave Knight Play GIS"
                print(gameState)
            elif mouseX > 345 and mouseX < 495 and mouseY > 240 and mouseY < 290:
                gameState = "Dark Knight Play GIS"
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
        
    elif gameState == "instructions":
        if mousePressed == True:
            # Checking if our boxes are pressed and if they are, switch the gamestate accordingly
            if mouseX > 400 and mouseX < 500 and mouseY > 120 and mouseY < 170:
                gameState = "IntroScreen"
                print(gameState)
                
            menuwindow.blit(InstructionsWindowbg,(0,0))
            # Drawing our title
            titleText = font3.render("Instructions", 1, "white")
            mainwindow.blit(titleText, (40, 10))
            
            # Drawing each line of instructions
            line1 = font1.render("1. Use 'A' and 'D' keys to move left and right.", 1, pygame.Color("white"))
            mainwindow.blit(line1, (10, 70))
            line2 = font1.render("2. Press 'SPACE' to jump.", 1, pygame.Color("white"))
            mainwindow.blit(line2, (10, 110))
            line3 = font1.render("3. Press 'r' to shoot projectiles. ", 1, pygame.Color("white"))
            mainwindow.blit(line3, (10, 150))
            line4 = font1.render("4. Retrieve The magical gem to save the kingdom.).", 1, pygame.Color("white"))
            mainwindow.blit(line4, (10, 190))
            line5 = font1.render("Good Luck!", 1, pygame.Color("white"))
            mainwindow.blit(line5, (10, 230))
        
            # Drawing the menu button
            pygame.draw.rect(mainwindow, pygame.Color("dark blue"), (400, 120, 100, 50)) # The Box
            menuText = font1.render("Menu", 1, "white")
            mainwindow.blit(menuText, (417, 128)) # The Text
            
    elif gameState == "Axe Warrior Play GIS":
        if mousePressed == True:
            
            # Drawing the background for the menu window
            mainwindow.blit(GameIntroScreenbg, (0, 0))
            mainwindow.blit(Door, (485,110))
            mainwindow.blit(Heart1, (400,0))
            mainwindow.blit(Heart2, (425,0))
            mainwindow.blit(Heart3, (450,0))
            mainwindow.blit(sprite1, sprite1rect.topleft)  # Use topleft attribute for blit
            
            # Play the game over sound effect only once
            if not MonsterRoarPlayed:
                MonsterRoar.play()
                MonsterRoarPlayed = True
            
            if gameState == "Axe Warrior Play GIS":
                moving = True
                key = pygame.key.get_pressed()
                if key[pygame.K_d] == True:
                    sprite1rect.x = sprite1rect.x + sprite_speed
                elif key[pygame.K_a] == True:
                    sprite1rect.x = sprite1rect.x - sprite_speed
                elif key[pygame.K_SPACE] == True:
                    sprite1rect.y = sprite1rect.y - sprite_speed
                    SpacePressed = True
                else:
                    SpacePressed = False
                    moving = False
                # Causes our character to fall
                gravity = gravity + 1
                sprite1rect.y = sprite1rect.y + gravity
                # Stops our sprite from falling when it hits the coordinates that we chose for the floor
            if gameState == "Axe Warrior Play GIS":
                floor = 150
                sprite_speed = 2
                if sprite1rect.y > floor:
                    gravity = 0
                    sprite1rect.y = floor
                # Making our sprite jump
                if SpacePressed == True and sprite1rect.y >= floor:
                    gravity = -12
                    continue

            if sprite1rect.colliderect(Doorrect):
                gameState = "Axe Warrior Play GIS"
                
    elif gameState == "Brave Knight Play GIS":
        if mousePressed == True:
            
            # Drawing the background for the menu window
            mainwindow.blit(GameIntroScreenbg, (0, 0))
            mainwindow.blit(Door, (485,110))
            mainwindow.blit(Heart1, (400,0))
            mainwindow.blit(Heart2, (425,0))
            mainwindow.blit(Heart3, (450,0))
            mainwindow.blit(sprite2, sprite2rect.topleft)  # Use topleft attribute for blit
            
            # Play the game over sound effect only once
            if not MonsterRoarPlayed:
                MonsterRoar.play()
                MonsterRoarPlayed = True
            
            if gameState == "Brave Knight Play GIS":
                moving = True
                key = pygame.key.get_pressed()
                if key[pygame.K_d] == True:
                    sprite2rect.x = sprite2rect.x + sprite_speed
                elif key[pygame.K_a] == True:
                    sprite2rect.x = sprite2rect.x - sprite_speed
                elif key[pygame.K_SPACE] == True:
                    sprite2rect.y = sprite2rect.y - sprite_speed
                    SpacePressed = True
                else:
                    SpacePressed = False
                    moving = False
                # Causes our character to fall
                gravity = gravity + 1
                sprite2rect.y = sprite2rect.y + gravity
                # Stops our sprite from falling when it hits the coordinates that we chose for the floor
            if gameState == "Brave Knight Play GIS":
                floor = 157
                sprite_speed = 2
                if sprite2rect.y > floor:
                    gravity = 0
                    sprite2rect.y = floor
                # Making our sprite jump
                if SpacePressed == True and sprite2rect.y >= floor:
                    gravity = -12
                    continue

            if sprite3rect.colliderect(Doorrect):
                gameState = "Brave Knight Play GIS"
            
    elif gameState == "Dark Knight Play GIS":
        if mousePressed == True:
            
            # Drawing the background for the menu window
            mainwindow.blit(GameIntroScreenbg, (0, 0))
            mainwindow.blit(Door, (485,110))
            mainwindow.blit(Heart1, (400,0))
            mainwindow.blit(Heart2, (425,0))
            mainwindow.blit(Heart3, (450,0))
            mainwindow.blit(sprite3, sprite3rect.topleft)  # Use topleft attribute for blit
            
            # Play the game over sound effect only once
            if not MonsterRoarPlayed:
                MonsterRoar.play()
                MonsterRoarPlayed = True
            
            if gameState == "Dark Knight Play GIS":
                moving = True
                key = pygame.key.get_pressed()
                if key[pygame.K_d] == True:
                    sprite3rect.x = sprite3rect.x + sprite_speed
                elif key[pygame.K_a] == True:
                    sprite3rect.x = sprite3rect.x - sprite_speed
                elif key[pygame.K_SPACE] == True:
                    sprite3rect.y = sprite3rect.y - sprite_speed
                    SpacePressed = True
                else:
                    SpacePressed = False
                    moving = False
                # Causes our character to fall
                gravity = gravity + 1
                sprite3rect.y = sprite3rect.y + gravity
                # Stops our sprite from falling when it hits the coordinates that we chose for the floor
            if gameState == "Dark Knight Play GIS":
                floor = 157
                sprite_speed = 1
                if sprite3rect.y > floor:
                    gravity = 0
                    sprite3rect.y = floor
                # Making our sprite jump
                if SpacePressed == True and sprite3rect.y >= floor:
                    gravity = -12
                    continue

            if sprite3rect.colliderect(Doorrect):
                gameState = "Dark Knight Playing"
                
    elif gameState == "Axe Warrior Playing":
        floor = 190
        sprite_speed = 3
        if mousePressed == True:
            mainwindow.blit(mainbackground_image,(0,0))
            mainwindow.blit(sprite1, sprite1rect.topleft)  # Use topleft attribute for blit
        # Update and draw projectiles
        projectile_group.update()
        projectile_group.draw(mainwindow)  # Draw s on the game window
        # Create frog enemy at the right edge of the screen
        if frame % 120 == 0:  # Add a new frog enemy every 120 frames (adjust as needed)
            new_frog_enemy = FrogEnemy(windowWidth, floor)
            frog_enemy_group.add(new_frog_enemy)
                
        # Update and draw frog enemies
        frog_enemy_group.update()
        frog_enemy_group.draw(mainwindow)

            
    elif gameState == "Brave Knight Playing":
        floor = 190
        sprite_speed = 3
        if mousePressed == True:
            # Drawing the background for the menu window
            mainwindow.blit(mainbackground_image, (0, 0))
            mainwindow.blit(sprite2, sprite2rect.topleft)  # Use topleft attribute for blit
        # Update and draw projectiles
        projectile_group.update()
        projectile_group.draw(mainwindow)  # Draws on the game window
            
    elif gameState == "Dark Knight Playing":
        floor = 190
        sprite_speed = 3
        if mousePressed == True:
            # Drawing the background for the menu window
            mainwindow.blit(mainbackground_image, (0, 0))
            mainwindow.blit(sprite3, sprite3rect.topleft)  # Use topleft attribute for blit
        # Update and draw projectiles
        projectile_group.update()
        projectile_group.draw(mainwindow)  # Draws on the game window
            
    elif gameState == "Game Over You Lost":
        # Checking if our boxes are pressed and if they are, switch the gamestate accordingly
        if mouseX > 180 and mouseX < 380 and mouseY > 200 and mouseY < 200:
            gameState = "menu"
            print(gameState)
        elif mouseX > 180 and mouseX < 325 and mouseY > 200 and mouseY < 270:
            pygame.quit()

        Introwindow.fill((255,0,0))
            
        pygame.draw.rect(Introwindow, pygame.Color("White"), (180, 150, 200, 50)) # The Box
        instrText = font4.render("Play Again", 1, "black")
        Introwindow.blit(instrText, (200, 145 )) # The Text
        # Drawing the play button with text
        pygame.draw.rect(Introwindow, pygame.Color("White"), (180, 220, 200, 50)) # The Box
        playText = font4.render("Quit", 1, "black")
        Introwindow.blit(playText, (243, 220)) # The Text
            
        word3 = "Game"
        renderedText = font3.render(word3, 1, pygame.Color("Black"))
        Introwindow.blit(renderedText, (60,50))
        word4 = "Over"
        renderedText = font3.render(word4, 1, pygame.Color("Black"))
        Introwindow.blit(renderedText, (300,50))

    # *********GAME LOGIC**********
    # Setting our keybinds to see if a specific key is pressed to subtract or add to the Sprites x and y coordinates
    # to move by sprite speed variable that we created
    moving = True
    key = pygame.key.get_pressed()
    if key[pygame.K_d] == True:
        sprite3rect.x = sprite3rect.x + sprite_speed
    elif key[pygame.K_a] == True:
        sprite3rect.x = sprite3rect.x - sprite_speed
    elif key[pygame.K_SPACE] == True:
        sprite3rect.y = sprite3rect.y - sprite_speed
        SpacePressed = True
    else:
        SpacePressed = False
        moving = False
    # Causes our character to fall
    gravity = gravity + 1
    sprite3rect.y = sprite3rect.y + gravity
    # Stops our sprite from falling when it hits the coordinates that we chose for the floor
    if sprite3rect.y > floor:
        gravity = 0
        sprite3rect.y = floor
    # Making our sprite jump
    if SpacePressed == True and sprite3rect.y >= floor:
        gravity = -12
        continue
        
    # Running Animation logic for Knight1
    frame = frame + 1
    if moving == True:
        if frame == 0:
            sprite1 = pygame.transform.scale(Running1Knight1, (80,80))
        elif frame == 7:
            sprite1 = pygame.transform.scale(Running2Knight1, (80,80))
        elif frame == 14:
            sprite1 = pygame.transform.scale(Running3Knight1, (80,80))
        elif frame == 21:
            sprite1 = pygame.transform.scale(Running4Knight1, (80,80))
        elif frame == 28:
            sprite1 = pygame.transform.scale(Running5Knight1, (80,80))
        elif frame == 35:
            sprite1 = pygame.transform.scale(Running6Knight1, (80,80))
        elif frame == 42:
            sprite1 = pygame.transform.scale(Running7Knight1, (80,80))
        elif frame == 49:
            sprite1 = pygame.transform.scale(Running8Knight1, (80,80))
            frame = 0
    else:
        # Idle Animation for Knight1
        if frame == 0:
            sprite1 = pygame.transform.scale(Idle1Knight1, spriteSize)
        elif frame == 10:
            sprite1 = pygame.transform.scale(Idle2Knight1, spriteSize)
        elif frame == 20:
            sprite1 = pygame.transform.scale(Idle3Knight1, spriteSize)
        elif frame == 30:
            sprite1 = pygame.transform.scale(Idle4Knight1, spriteSize)
        elif frame == 40:
            sprite1 = pygame.transform.scale(Idle5Knight1, spriteSize)
            frame = 0
    if frame > 49:
        frame = 0
        
    # Running Animation logic for Knight2
    if moving == True:
        if frame == 0:
            sprite2 = pygame.transform.scale(Running1Knight2, spriteSize)
        elif frame == 7:
            sprite2 = pygame.transform.scale(Running2Knight2, spriteSize)
        elif frame == 14:
            sprite2 = pygame.transform.scale(Running3Knight2, spriteSize)
        elif frame == 21:
            sprite2 = pygame.transform.scale(Running4Knight2, spriteSize)
        elif frame == 28:
            sprite2 = pygame.transform.scale(Running5Knight2, spriteSize)
        elif frame == 35:
            sprite2 = pygame.transform.scale(Running6Knight2, spriteSize)
        elif frame == 42:
            sprite2 = pygame.transform.scale(Running7Knight2, spriteSize)
        elif frame == 49:
            sprite2 = pygame.transform.scale(Running8Knight2, spriteSize)
            frame = 0
    else:
        # Idle Animation for Knight2
        if frame == 0:
            sprite2 = pygame.transform.scale(Idle1Knight2, spriteSize)
        elif frame == 10:
            sprite2 = pygame.transform.scale(Idle2Knight2, spriteSize)
        elif frame == 20:
            sprite2 = pygame.transform.scale(Idle3Knight2, spriteSize)
        elif frame == 30:
            sprite2 = pygame.transform.scale(Idle4Knight2, spriteSize)
        elif frame == 40:
            sprite2 = pygame.transform.scale(Idle5Knight2, spriteSize)
            frame = 0
    if frame > 49:
        frame = 0
            # Running Animation logic for Knight3
    if moving == True:
        if frame == 0:
            sprite3 = pygame.transform.scale(Running1Knight3, spriteSize)
        elif frame == 7:
            sprite3 = pygame.transform.scale(Running2Knight3, spriteSize)
        elif frame == 14:
            sprite3 = pygame.transform.scale(Running3Knight3, spriteSize)
        elif frame == 21:
            sprite3 = pygame.transform.scale(Running4Knight3, spriteSize)
        elif frame == 28:
            sprite3 = pygame.transform.scale(Running5Knight3, spriteSize)
        elif frame == 35:
            sprite3 = pygame.transform.scale(Running6Knight3, spriteSize)
        elif frame == 42:
            sprite3 = pygame.transform.scale(Running7Knight3, spriteSize)
        elif frame == 49:
            sprite3 = pygame.transform.scale(Running8Knight3, spriteSize)
            frame = 0
    else:
        # Idle Animation for Knight3
        if frame == 0:
            sprite3 = pygame.transform.scale(Idle1Knight3, spriteSize)
        elif frame == 10:
            sprite3 = pygame.transform.scale(Idle2Knight3, spriteSize)
        elif frame == 20:
            sprite3 = pygame.transform.scale(Idle3Knight3, spriteSize)
        elif frame == 30:
            sprite3 = pygame.transform.scale(Idle4Knight3, spriteSize)
        elif frame == 40:
            sprite3 = pygame.transform.scale(Idle5Knight3, spriteSize)
            frame = 0
    if frame > 49:
        frame = 0
        
    # Giving our game boundaries for all our characters
    if sprite1rect.x <= -20:
        sprite1rect.x = -20
    elif sprite1rect.x >= windowWidth - 50:
        sprite1rect.x = windowWidth - 50
        
    if sprite2rect.x <= -20:
        sprite2rect.x = -20
    elif sprite2rect.x >= windowWidth - 40:
        sprite2rect.x = windowWidth - 40
        
    if sprite3rect.x <= -20:
        sprite3rect.x = -20
    elif sprite3rect.x >= windowWidth - 45:
        sprite3rect.x = windowWidth - 45
        
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
    
    # Character slash animations
    if gameState == "Axe Warrior Play GIS":
        if event.type == pygame.MOUSEBUTTONDOWN:
            if frame == 0:
                sprite1 = pygame.transform.scale(Knight1SlashAnimation1, spriteSize)
            elif frame == 3:
                sprite1 = pygame.transform.scale(Knight1SlashAnimation2, spriteSize)
            elif frame == 6:
                sprite1 = pygame.transform.scale(Knight1SlashAnimation3, spriteSize)
            elif frame == 9:
                frame = 0
        if frame > 30:
            frame = 0
    
    if gameState == "Brave Knight Playing":
        if event.type == pygame.MOUSEBUTTONDOWN:
            if frame == 0:
                sprite2 = pygame.transform.scale(Knight2SlashAnimation1, spriteSize)
            elif frame == 3:
                sprite2 = pygame.transform.scale(Knight2SlashAnimation2, spriteSize)
            elif frame == 6:
                sprite2 = pygame.transform.scale(Knight2SlashAnimation3, spriteSize)
            elif frame == 9:
                frame = 0
        if frame > 30:
            frame = 0
            
    if gameState == "Dark Knight Playing":
        if event.type == pygame.MOUSEBUTTONDOWN:
            if frame == 0:
                sprite3 = pygame.transform.scale(Knight3SlashAnimation1, spriteSize)
            elif frame == 10:
                sprite3 = pygame.transform.scale(Knight3SlashAnimation2, spriteSize)
            elif frame == 20:
                sprite3 = pygame.transform.scale(Knight3SlashAnimation3, spriteSize)
            elif frame == 30:
                frame = 0
        if frame > 30:
            frame = 0
    
    #Drawing the time string on the screen of the given gamestates
    if gameState == "Axe Warrior Playing" or gameState == "Brave Knight Playing" or gameState == "Dark Knight Playing":
        # Draw the timer
        timer_font = pygame.font.Font(None, 36)
        timer_text = timer_font.render(f"Time: {int(current_time)}s", True, (255, 255, 255))
        mainwindow.blit(timer_text, (10, 10))
        

    # *********DRAW THE FRAME**********
    pygame.display.flip()
    clock.tick(FPS)  # Force frame rate to 60fps or lower