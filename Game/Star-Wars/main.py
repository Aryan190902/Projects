import pygame
import random
import math
from pygame import mixer
#Initialising the game
pygame.init()
#creating the screen
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1000,700))

running = True

#Title and Icon
pygame.display.set_caption("Star Wars")

#BackGround Image
background = pygame.image.load('background.jpg')

#Background Music
mixer.music.load('Avengers.mp3')
mixer.music.play(-1)
#Player
Player = pygame.image.load('spaceship.png')
playerX = 460
playerY = 600
playerX_change = 0
playerY_change = 0

#Enemy
Enemy = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemy = 3
for i in range(num_of_enemy):
    Enemy.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 935))
    enemyY.append(random.randint(50, 200))
    enemyX_change.append(0.3)
    enemyY_change.append(0.3)

#Laser
Laser = pygame.image.load('laser1.png')
laserX = playerX
laserX_change = 0
laserY_change = -5
laser_state = "ready"
#ready - cannot see the bullet
#fire - bulllet is moving

#Score

score = 0
font = pygame.font.Font('animeace2bb_tt\\animeace2_bld.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
    score_value = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))


#Strike
strike = 0

def Move(x, y):
    screen.blit(Player, (x, y))

def UFO(x, y, i):
    screen.blit(Enemy[i], (x, y)) 

def Fire(x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(Laser, (x+16, y+10))

def Collision(enemyX, enemyY, laserX, laserY):
    distance = math.sqrt((enemyX - laserX)**2 + (enemyY - laserY)**2)
    if distance <= 30:
        return True
    else:
        return False
strike_font = pygame.font.Font('animeace2bb_tt\\animeace2_bld.ttf', 32)
over_font = pygame.font.Font('animeace2bb_tt\\animeace2_bld.ttf', 64)

def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (400, 300))
def Strike(x, y):
    strike_text = font.render("Strike: " + str(strike), True, (255, 255, 255))
    screen.blit(strike_text, (x, y))

#Game Loop
while running:
    #Background Color
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -1.2
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 1.2
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -1.2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 1.2
            if event.key == pygame.K_SPACE:
                laserX = playerX
                Fire(laserX, playerY)
                laserY = playerY
                laser_sound = mixer.Sound('laser.wav')
                laser_sound.play()                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or \
            event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w or \
            event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0
            
        
    #For Movement
    playerX += playerX_change
    playerY += playerY_change
    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        enemyY[i] += enemyY_change[i]
    #Adding Borders
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936
    if playerY <= 0:
        playerY = 0
    elif playerY >= 636:
        playerY = 636

    #Enemy's movement 
    for i in range(num_of_enemy):
        #Game Over
        if enemyY[i] >= 636:
            strike += 1

        if strike >= 3:
            for j in range(num_of_enemy):
                enemyY[i] = 2000
            game_over_text()
            strike = 3
            break 
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_change[i] = 0.3
        elif enemyX[i] >= 936:
            enemyX[i] = 936
            enemyX_change[i] = -0.3
        if enemyY[i] <= 0:
            enemyY[i] = 0
            enemyY_change[i] = 0.3
        elif enemyY[i] >= 636:
            enemyY[i] = 636
            enemyY_change[i] = -0.3
        #Laser Movement
        if laser_state == "fire":
            Fire(laserX, laserY)
            laserY += laserY_change
            if laserY <=0:
                laser_state = "ready"
            #Collision
            collided = Collision(enemyX[i], enemyY[i], laserX, laserY)
            if collided:
                laser_state = "ready"
                score += 50
                enemyX[i] = random.randint(0, 1000)
                enemyY[i] = random.randint(50, 200)
                explosion_sound = mixer.Sound('explosion.wav')
                explosion_sound.play()
            #Blitting enemies
        UFO(enemyX[i], enemyY[i], i)
    Move(playerX, playerY)
    show_score(textX, textY)
    Strike(10, 50)
    pygame.display.update()