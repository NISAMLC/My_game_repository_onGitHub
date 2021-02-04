import pygame
##initializing the pygame
pygame.init()

#creating screen for our game
screen=pygame.display.set_mode((800,600))

##setting title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

##adding a player as an image
playerImg=pygame.image.load("player.png")
playerX=360
playerY=480
player_change = 0

##creating a function to add playe into our surface of the game
def player(x,y):
    screen.blit(playerImg,(x,y))

##creating a looping and event management for quiting from the screen
running=True
while running:
##anything am i want to be persistant or need to be used continuously or appear it has to go in this while loop
##changing the background by filling RGB value and make sure everything get updated
    screen.fill((255, 156, 0))
#for controlling the movement we increamenting the values of coordinates
#if keystroke is pressed check it's into which direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key ==pygame.K_LEFT:
                player_change = -0.3
            if event.key ==pygame.K_RIGHT:
                player_change = 0.3
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

    playerX += player_change

##we are setting the boarder here
    if playerX <=0:
        playerX = 0
    elif playerX>=736:
        playerX = 736
    player(playerX,playerY)
    pygame.display.update()

