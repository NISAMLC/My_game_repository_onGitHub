import pygame
import random

##initializing the pygame
pygame.init()

# creating screen for our game
screen = pygame.display.set_mode((800, 600))

##background image setting
background = pygame.image.load("galaxy.jpg")
##setting title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

##adding a player as an image
playerImg = pygame.image.load("player.png")
playerX = 360
playerY = 480
playerX_change = 0

##adding a enemy as an image
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 40

##bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
# ready state you can't see the bullet on the screen
# fire bullet is currently moving
bullet_state = "ready"
bulletX_change = 0
bulletY_change = 10


##creating a function to add playe into our surface of the game
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


##creating a function to add playe into our surface of the game
def player(x, y):
    screen.blit(playerImg, (x, y))


##creating a function to fire the bullet
def bulletfire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


##creating a looping and event management for quiting from the screen
running = True
while running:
    ##anything am i want to be persistant or need to be used continuously or appear it has to go in this while loop
    ##changing the background by filling RGB value and make sure everything get updated
    screen.fill((255, 156, 0))
    ##background image
    screen.blit(background, (0, 0))
    # for controlling the movement we increamenting the values of coordinates
    # if keystroke is pressed check it's into which direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                bulletfire(playerX,playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    ##we are setting the boarder here
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    ##we are setting the boarder here for enemy so it not go out
    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change
    #bullet movement
    if bullet_state is "fire":
        bulletfire(playerX,bulletY)
        bulletY-= bulletY_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
