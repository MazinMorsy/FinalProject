import pygame
import random
from pygame import mixer

pygame.init()

# variables to set the size of the main window
windowWidth = 539
windowHeight = 286

frame = 0  # Not the FPS but the frame of our animation
gravitysprite1 = 0
gravitysprite2 = 0
gravitysprite3 = 0

FPS = 60
current_time = 0  # Initialize the timer variable
clock = pygame.time.Clock()  # Create a clock object

moving = False
mousePressed = False

# variable to track the music state
music_paused = False

# variable to track the button state
music_button_pressed = False

sprite_speed = 3
gameState = "IntroScreen"


sprite1Display = pygame.image.load("Knight1.png")

spritesRectwidth = 64
spritesRectheight = 64
floor = 185
spriteSize = (64, 64)
sprite_speed = 3
SpacePressed = False  # Initialize SpacePressed variable
MonsterRoar = pygame.mixer.Sound("TitanROAR.wav")
MonsterRoarPlayed = False

doorsrectwidth = 44
doorsrectheight = 64
Doorrect = pygame.Rect(485,110, doorsrectwidth,doorsrectheight )

Portalrectwidth = 44
Portalrectheight = 84
Portalrect = pygame.Rect(400,168, Portalrectwidth,Portalrectheight )

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

#Capturing Gem bg dimensions and background
CaptureGemwindow = pygame.display.set_mode((windowWidth, windowHeight))
CaptureGembg = pygame.image.load("CaptureGembg.jpg")

# Initial appearance of all our characters
sprite1 = pygame.image.load("Knight1.png")
sprite1rect = sprite1.get_rect()  # Returns information about our sprite1
sprite2 = pygame.image.load("Knight2.png")
sprite2rect = sprite2.get_rect()  # Returns information about our sprite2
sprite3 = pygame.image.load("Knight3.png")
sprite3rect = sprite3.get_rect()  # Returns information about our sprite2


Wizard = pygame.image.load("Wizard.png")
SpeechBubble = pygame.image.load("SpeechBubble.png")

FrogEnemy = pygame.image.load("FrogEnemyRun1.png")
FrogEnemyrect = FrogEnemy.get_rect() # Returns information about our FrogEnemy

Heart1 = pygame.image.load("Heart1.png")
Heart2 = pygame.image.load("Heart2.png")
Heart3 = pygame.image.load("Heart3.png")

Door = pygame.image.load("Door.png")
Doorrect = Door.get_rect()

Portal = pygame.image.load("Portal.png")
Portalrect = Portal.get_rect()

Ruby = pygame.image.load("Ruby.png")
Rubyrect = Ruby.get_rect(topleft=(506, floor))


Chest = pygame.image.load("Chest.png")

# Choosing Characters Pictures
sprite1Display = pygame.image.load("Knight1.png")
sprite2Display = pygame.image.load("Knight2.png")
sprite3Display = pygame.image.load("Knight3.png")

# Idle Animations
Idle1Knight1 = pygame.image.load("Idle Animation1 Knight1.png")
Idle2Knight1 = pygame.image.load("Idle Animation2 Knight1.png")
Idle3Knight1 = pygame.image.load("Idle Animation3 Knight1.png")
Idle4Knight1 = pygame.image.load("Idle Animation4 Knight1.png")
Idle5Knight1 = pygame.image.load("Idle Animation5 Knight1.png")

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

Running1Knight2 = pygame.image.load("Running Animation1 Knight2.png")
Running2Knight2 = pygame.image.load("Running Animation2 Knight2.png")
Running3Knight2 = pygame.image.load("Running Animation3 Knight2.png")
Running4Knight2 = pygame.image.load("Running Animation4 Knight2.png")
Running5Knight2 = pygame.image.load("Running Animation5 Knight2.png")
Running6Knight2 = pygame.image.load("Running Animation6 Knight2.png")
Running7Knight2 = pygame.image.load("Running Animation7 Knight2.png")
Running8Knight2 = pygame.image.load("Running Animation8 Knight2.png")

Running1Knight3 = pygame.image.load("Running Animation1 Knight3.png")
Running2Knight3 = pygame.image.load("Running Animation2 Knight3.png")
Running3Knight3 = pygame.image.load("Running Animation3 Knight3.png")
Running4Knight3 = pygame.image.load("Running Animation4 Knight3.png")
Running5Knight3 = pygame.image.load("Running Animation5 Knight3.png")
Running6Knight3 = pygame.image.load("Running Animation6 Knight3.png")
Running7Knight3 = pygame.image.load("Running Animation7 Knight3.png")
Running8Knight3 = pygame.image.load("Running Animation8 Knight3.png")


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


# Set up hearts and heart images
hearts = 3
heart_images = [Heart1, Heart2, Heart3]

font_path1 = "DUNGEONFONT.ttf"
font1 = pygame.font.Font(font_path1, 35)

font_path2 = "TITLEFONT.otf"
font2 = pygame.font.Font(font_path2, 40)

font_path3 = "TITLEFONT.otf"
font3 = pygame.font.Font(font_path2, 75)

font_path4 = "DUNGEONFONT.ttf"
font4 = pygame.font.Font(font_path1, 50)

font_path5 = "Pixel.ttf"
font5 = pygame.font.Font(font_path5, 15)

font_path6 = "Pixel.ttf"
font6 = pygame.font.Font(font_path6, 30)

#Background Music
pygame.mixer.music.load("DungeonMusic.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1) # The value -1 keeps it so it loops the bg music forever

# Our classes

# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        # Load projectile image
        original_image = pygame.image.load("Slash.png") 
        self.image =  pygame.transform.scale(original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x - 20
        self.rect.y = y + -20
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
        print("Frog enemy initialized at:", x, y)

        self.index = 0
        self.image = self.running_images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1  # Set the frog enemy speed
        self.jump_power = -15  # Jump power for frogs
        self.on_ground = False  # Flag to check if frog is on the ground

    def update(self, target_x, target_y):
        print("Updating frog enemy position")
        if self.rect.x < target_x:
            self.rect.x += self.speed
        elif self.rect.x > target_x:
            self.rect.x -= self.speed

        if self.rect.y < target_y:
            self.rect.y += self.speed
        elif self.rect.y > target_y:
            self.rect.y -= self.speed

        # Update frog enemy animation
        self.index += 1
        if self.index >= len(self.running_images):
            self.index = 0
        self.image = self.running_images[self.index]
        
        # Frog jump logic
        if self.on_ground and random.randint(0, 100) < 2:  # 2% chance to jump
            self.jump()

    def jump(self):
        self.rect.y += self.jump_power

# FrogEnemy group
frog_enemy_group = pygame.sprite.Group()


# Set up a timer for frog enemy spawning
spawn_timer = 0
spawn_interval = random.randint(500, 700)  # Initial spawn interval
spawn_delay = 3000  # The initial delay before frogs start spawning
max_frog_enemies = 15  # Adjust this value based on how many frog enemies you want

        
# Shaking window function
def shake_mainwindow(surface, duration, magnitude):
    start_time = pygame.time.get_ticks()
    original_position = surface.get_rect().topleft
    while pygame.time.get_ticks() - start_time < duration:
        offset = (random.randint(-magnitude, magnitude), random.randint(-magnitude, magnitude))
        # Update the main window with the back buffer
        mainwindow.blit(surface, (original_position[0] + offset[0], original_position[1] + offset[1]))
        pygame.display.update()

    # Restore the original position
    mainwindow.blit(surface, original_position)
    pygame.display.update()

# Function to toggle music state and button color
def toggle_music_mute():
    global music_paused, music_button_pressed
    music_paused = not music_paused  # Toggle between True and False
    music_button_pressed = not music_button_pressed  # Toggle between True and False

    if music_paused:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


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
                # Check if "Music" button is pressed
                if gameState == "IntroScreen":
                    if 10 < mouseX < 110 and 230 < mouseY < 280:
                        mousePressed = True  # Set the flag to True when the left mouse button is pressed
                        toggle_music_mute()

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
        # Drawing the button with color based on its state
        button_color = pygame.Color("green") if not music_button_pressed else pygame.Color("red")
        pygame.draw.rect(Introwindow, button_color, (10, 230, 100, 50))  # The Box
        MusicText = font6.render("Music", 1, "black")
        Introwindow.blit(MusicText, (17, 240))  # The Text
    
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
            line3 = font1.render("3. Press the mouse to shoot projectiles. ", 1, pygame.Color("white"))
            mainwindow.blit(line3, (10, 150))
            line4 = font1.render("4. Retrieve The magical gem to save the Kingdom.", 1, pygame.Color("white"))
            mainwindow.blit(line4, (10, 190))
            line5 = font1.render("Good Luck!", 1, pygame.Color("white"))
            mainwindow.blit(line5, (10, 230))
        
            # Drawing the menu button
            pygame.draw.rect(mainwindow, pygame.Color("dark blue"), (400, 120, 100, 50)) # The Box
            menuText = font1.render("Menu", 1, "white")
            mainwindow.blit(menuText, (417, 128)) # The Text
            
                    
    elif gameState == "Axe Warrior Play GIS" or gameState == "Brave Knight Play GIS" or gameState == "Dark Knight Play GIS":
        
        # Drawing the background for the menu window
        mainwindow.blit(GameIntroScreenbg, (0, 0))
        mainwindow.blit(Wizard, (400,167))
        mainwindow.blit(SpeechBubble, (280,40))
        mainwindow.blit(Door, (500,138))
        Doorrect = pygame.Rect(515,110, doorsrectwidth,doorsrectheight )

        # Drawing the wizards text within the speech bubble
        line1 = font5.render("Retrieve the", 1, pygame.Color("black"))
        mainwindow.blit(line1, (295, 70))
        line2 = font5.render("magical gem to", 1, pygame.Color("black"))
        mainwindow.blit(line2, (290, 85))
        line3 = font5.render("save our nation", 1, pygame.Color("black"))
        mainwindow.blit(line3, (285, 100))
        line4 = font5.render("young hero!", 1, pygame.Color("black"))
        mainwindow.blit(line4, (310, 115))
        
        if gameState == "Axe Warrior Play GIS":
            if mousePressed == True:
                mainwindow.blit(sprite1, sprite1rect.topleft)  # Use topleft attribute for blit

                
                if gameState == "Axe Warrior Play GIS":
                    # Stops our sprite from falling when it hits the coordinates that we chose for the floor
                    floor = 150
                    sprite_speed = 2
                    if sprite1rect.y > floor:
                        sprite1rect.y = floor
                    # Making our sprite jump
                    if SpacePressed == True and sprite1rect.y >= floor:
                        gravitysprite1 = -12
                    if sprite1rect.colliderect(Doorrect):
                        gameState = "Axe Warrior Playing"
               
        elif gameState == "Brave Knight Play GIS":
            if mousePressed == True:
                mainwindow.blit(sprite2, sprite2rect.topleft)  # Use topleft attribute for blit

                # Stops our sprite from falling when it hits the coordinates that we chose for the floor
                if gameState == "Brave Knight Play GIS":
                    floor = 157
                    sprite_speed = 2
                    if sprite2rect.colliderect(Doorrect):
                        gameState = "Brave Knight Playing"
                        
                    
        elif gameState == "Dark Knight Play GIS":
            if mousePressed == True:
                mainwindow.blit(sprite3, sprite3rect.topleft)  # Use topleft attribute for blit
                
                if gameState == "Dark Knight Play GIS":
                    floor = 157
                    sprite_speed = 2
                    if sprite3rect.colliderect(Doorrect):
                        gameState = "Dark Knight Playing"
                
        # Play the game over sound effect only once
        if not MonsterRoarPlayed:
            MonsterRoar.play()
            MonsterRoarPlayed = True
            
            # Shake the intro screen
            shake_mainwindow(GameIntroScreenbg, 9000, 10)  # Shake for 9000 milliseconds with a magnitude of 10
            
    
    elif gameState == "Axe Warrior Playing" or gameState == "Brave Knight Playing" or gameState == "Dark Knight Playing":
        
        mainwindow.blit(mainbackground_image,(0,0))
        #Drawing the time string on the screen according to the given gamestates
        timer_font = pygame.font.Font(None, 36)
        timer_text = timer_font.render(f"Time: {int(current_time)}s", True, (255, 255, 255))
        mainwindow.blit(timer_text, (10, 10))
        
        mainwindow.blit(Portal, (10,168))
        Portalrect = pygame.Rect(-20,168, Portalrectwidth,Portalrectheight )
        
        # Drawing the hearts
        mainwindow.blit(Heart1, (400,0))
        mainwindow.blit(Heart2, (425,0))
        mainwindow.blit(Heart3, (450,0))
        frog_enemy_group.draw(mainwindow)

        if gameState == "Axe Warrior Playing":
            if mousePressed == True:
                mainwindow.blit(sprite1, sprite1rect.topleft)  # Use topleft attribute for blit
                frog_enemy_group.update(sprite1rect.x, sprite1rect.y)

                
                if gameState == "Axe Warrior Playing":
                    # Stops our sprite from falling when it hits the coordinates that we chose for the floor
                    floor = 190
                    sprite_speed = 3
                    if sprite1rect.y > floor:
                        sprite1rect.y = floor
                    # Making our sprite jump
                    if SpacePressed == True and sprite1rect.y >= floor:
                        gravitysprite1 = -12
                    if sprite1rect.colliderect(Portalrect):
                        gameState = "Axe Warrior Capturing"
               
        elif gameState == "Brave Knight Playing":
            if mousePressed == True:
                mainwindow.blit(sprite2, sprite2rect.topleft)  # Use topleft attribute for blit
                frog_enemy_group.update(sprite2rect.x, sprite2rect.y)
                frog_enemy_group.draw(mainwindow)


                # Stops our sprite from falling when it hits the coordinates that we chose for the floor
                if gameState == "Brave Knight Playing":
                    floor = 190
                    sprite_speed = 3
                    if sprite2rect.colliderect(Portalrect):
                        print("Brave Knight collided with Portal")
                        gameState = "Brave Knight Capturing"
                    
        elif gameState == "Dark Knight Playing":
            if mousePressed == True:
                mainwindow.blit(sprite3, sprite3rect.topleft)  # Use topleft attribute for blit
                frog_enemy_group.update(sprite3rect.x, sprite3rect.y)
                
                if gameState == "Dark Knight Playing":
                    floor = 190
                    sprite_speed = 3
                    if sprite3rect.colliderect(Portalrect):
                        gameState = "Dark Knight Capturing"
        
        # Update and draw projectiles in the following gamestates
        projectile_group.update()
        projectile_group.draw(mainwindow)  # Draws on the game window
        
        # Create frog enemy at the right edge of the screen after spawn delay
        if frame % 120 == 0:  # Add a new frog enemy every 120 frames (adjust as needed)
            new_frog_enemy = FrogEnemy(windowWidth, floor)
            frog_enemy_group.add(new_frog_enemy)
                
        # Drawing frog enemies
        frog_enemy_group.draw(mainwindow)
        print("Drawing frog enemies")

                
        # Update frog positions
        for frog in frog_enemy_group:
            if gameState == "Axe Warrior Playing":
                target_x, target_y = sprite1rect.x, sprite1rect.y
                frog.update(target_x, target_y)  # Pass player character's position to frog update method
                # Check for collisions with player character
                if frog.rect.colliderect(sprite1rect):  # Assuming sprite2 is the player character
                    print("Sprite Hit!")
                    hearts -= 1
                    if hearts <= 0:
                        gameState = "Game Over You Lost"
                    else:
                        # Remove one heart image
                        heart_images.pop()
                        if len(heart_images) == 0:
                            gameState = "Game Over You Lost"

            if gameState == "Brave Knight Playing":
                target_x, target_y = sprite2rect.x, sprite2rect.y
                frog.update(target_x, target_y)  # Pass player character's position to frog update method
                # Check for collisions with player character
                if frog.rect.colliderect(sprite2rect):  # Assuming sprite2 is the player character
                    print("Sprite Hit!")
                    hearts -= 1
                    if hearts <= 0:
                        gameState = "Game Over You Lost"
                    else:
                        # Remove one heart image
                        heart_images.pop()
                        if len(heart_images) == 0:
                            gameState = "Game Over You Lost"
                            
            if gameState == "Dark Knight Playing":
                target_x, target_y = sprite3rect.x, sprite3rect.y
                frog.update(target_x, target_y)  # Pass player character's position to frog update method
                # Check for collisions with player character
                if frog.rect.colliderect(sprite3rect):  # Assuming sprite2 is the player character
                    print("Sprite Hit!")
                    hearts -= 1
                    if hearts <= 0:
                        gameState = "Game Over You Lost"
                    else:
                        # Remove one heart image
                        heart_images.pop()
                        if len(heart_images) == 0:
                            gameState = "Game Over You Lost"
                            
        # Check for game over condition
        if hearts <= 0:
            gameState = "Game Over You Lost"        
            if spawn_timer >= spawn_interval and len(frog_enemy_group) < max_frog_enemies:
                spawn_timer = 0
                spawn_interval = random.randint(2000, 5000)  # Reset spawn interval
            
            # Update and draw projectiles and frog enemies
            projectile_group.update()
            projectile_group.draw(mainwindow)
        
        # Update the timer
        current_time += clock.get_rawtime() / 1000
    
    elif gameState == "Axe Warrior Capturing" or gameState == "Brave Knight Capturing" or gameState == "Dark Knight Capturing":
        # Drawing the background for the menu window
        mainwindow.blit(CaptureGembg, (0, 0))
        mainwindow.blit(Chest, (490, 230))
        mainwindow.blit(Ruby, (495, 225))
        print(f"Mouse Position: ({mouseX}, {mouseY})")

        
        if gameState == "Axe Warrior Capturing":
            if mousePressed:
                mainwindow.blit(sprite1, sprite1rect.topleft)

                # Update sprite1 position
                sprite1rect.y += gravitysprite1
                gravitysprite1 += 0.5

                # Stop sprite from falling below the floor
                if sprite1rect.y > floor:
                    sprite1rect.y = floor

                # Check for collision with Rubyrect
                if sprite1rect.colliderect(Rubyrect):
                    gameState = "You Won"

        elif gameState == "Brave Knight Capturing":
            if mousePressed:
                mainwindow.blit(sprite2, sprite2rect.topleft)

                # Update sprite2 position
                sprite2rect.y += gravitysprite2
                gravitysprite2 += 0.5

                # Stop sprite from falling below the floor
                if sprite2rect.y > floor:
                    sprite2rect.y = floor

                # Check for collision with Rubyrect
                if sprite2rect.colliderect(Rubyrect):
                    gameState = "You Won"

        elif gameState == "Dark Knight Capturing":
            if mousePressed:
                mainwindow.blit(sprite3, sprite3rect.topleft)

                # Update sprite3 position
                sprite3rect.y += gravitysprite3
                gravitysprite3 += 0.5

                # Stop sprite from falling below the floor
                if sprite3rect.y > floor:
                    sprite3rect.y = floor

                # Check for collision with Rubyrect
                if sprite3rect.colliderect(Rubyrect):
                    gameState = "You Won"

        
    elif gameState == "Game Over You Lost":
        # Checking if our boxes are pressed and if they are, switch the gamestate accordingly
        if mouseX > 180 and mouseX < 380 and mouseY > 150 and mouseY < 200:
            gameState = "IntroScreen"
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
        
    elif gameState == "You Won":
        # Checking if our boxes are pressed and if they are, switch the gamestate accordingly
        if mouseX > 180 and mouseX < 380 and mouseY > 150 and mouseY < 200:
            gameState = "IntroScreen"
            print(gameState)
        elif mouseX > 180 and mouseX < 325 and mouseY > 200 and mouseY < 270:
            pygame.quit()

        Introwindow.fill((0,128,0))
            
        pygame.draw.rect(Introwindow, pygame.Color("White"), (180, 150, 200, 50)) # The Box
        instrText = font4.render("Play Again", 1, "black")
        Introwindow.blit(instrText, (200, 145 )) # The Text
        # Drawing the play button with text
        pygame.draw.rect(Introwindow, pygame.Color("White"), (180, 220, 200, 50)) # The Box
        playText = font4.render("Quit", 1, "black")
        Introwindow.blit(playText, (243, 220)) # The Text
            
        word5 = "You Won"
        renderedText = font3.render(word5, 1, pygame.Color("Black"))
        Introwindow.blit(renderedText, (130,30))
    
    elif gameState == "Game Over You Lost" or gameState == "You Won":
        # Reset hearts
        hearts = 3

        # Reset heart images
        heart_images = [HeartImage, HeartImage, HeartImage]

        # Reset timer
        current_time = 0
        
        
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
    gravitysprite3 = gravitysprite3 + 1
    sprite3rect.y = sprite3rect.y + gravitysprite3
    # Stops our sprite from falling when it hits the coordinates that we chose for the floor
    if sprite3rect.y > floor:
        gravitysprite3 = 0
        sprite3rect.y = floor
    # Making our sprite jump
    if SpacePressed == True and sprite3rect.y >= floor:
        gravitysprite3 = -12
    
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
    gravitysprite2 = gravitysprite2 + 1
    sprite2rect.y = sprite2rect.y + gravitysprite2
    # Stops our sprite from falling when it hits the coordinates that we chose for the floor
    if sprite2rect.y > floor:
        gravitysprite2 = 0
        sprite2rect.y = floor
    # Making our sprite jump
    if SpacePressed == True and sprite2rect.y >= floor:
        gravitysprite2 = -12
    
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
    gravitysprite1 = gravitysprite1 + 1
    sprite1rect.y = sprite1rect.y + gravitysprite1
    # Stops our sprite from falling when it hits the coordinates that we chose for the floor
    if sprite1rect.y > floor:
        gravitysprite1 = 0
        sprite1rect.y = floor
    # Making our sprite jump
    if SpacePressed == True and sprite1rect.y >= floor:
        gravitysprite1 = -12
        
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
    if gameState == "Axe Warrior Playing":
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

    # *********DRAW THE FRAME**********
    pygame.display.flip()
    clock.tick(FPS)  # Force frame rate to 60fps or lower