import pygame
import random

#Initialise pygame
pygame.init()
#Displaying screen
screen = pygame.display.set_mode((1300, 800))

#Setting frame rate
clock = pygame.time.Clock()

#Background Image
background = pygame.image.load('jlwd_2ucy_201006.jpg').convert() #Will help if game is lagging
TransBack = pygame.transform.scale(background, (1300, 800))

#Floor
floor = pygame.image.load('Flappy-Bird-Floor1.png').convert()
TransFloor = pygame.transform.scale(floor, (525, 150)).convert()

#Font
game_font = pygame.font.Font('animeace2bb_tt\\animeace2_bld.ttf', 30)


#Bird
bird_downflap = pygame.transform.scale2x(pygame.image.load('bird_downflap.png')).convert_alpha()
bird_upflap = pygame.transform.scale2x(pygame.image.load('bird_upflap.png')).convert_alpha()
bird_midflap = pygame.transform.scale2x(pygame.image.load('bird.png')).convert_alpha()
bird_frames = [bird_downflap, bird_upflap, bird_midflap]
bird_index = 0
bird = bird_frames[bird_index]
bird_rect = bird.get_rect(center = (100, 250))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

#Pipe
pipe = pygame.image.load('pipe1.png').convert_alpha()
pipe = pygame.transform.scale(pipe, (150, 800))
pipe_lst = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1400)
pipe_height = [i for i in range(200, 650, 50)]
#Background Movement
floor_moveX = 0

#Game Variables
gravity = 0.20
bird_movement = 0 
game_active = True
score = 0
high_score = 0

flap_sound = pygame.mixer.Sound("Sound\\sound_sfx_wing.wav")
dead_sound = pygame.mixer.Sound("Sound\\sound_sfx_hit.wav")

def draw_floor():
    screen.blit(TransFloor, (floor_moveX ,650))
    screen.blit(TransFloor, (floor_moveX + 525, 650))
    screen.blit(TransFloor, (floor_moveX + 1050, 650))
    #2nd floor for continuous movement
    screen.blit(TransFloor, (floor_moveX + 1575 ,650))
    screen.blit(TransFloor, (floor_moveX + 2100, 650))
    screen.blit(TransFloor, (floor_moveX + 2625, 650))

def create_pipe():
    random_pipe = random.choice(pipe_height)
    top_pipe = pipe.get_rect(midbottom = (1400, random_pipe - 250))
    bottom_pipe = pipe.get_rect(midtop = (1400, random_pipe))
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for i in pipes: # i is pipe but we already have a functionname pipe
        if i.bottom >= 800:
            screen.blit(pipe, i)
        else:
            flip_pipe = pygame.transform.flip(pipe, False, True)
            screen.blit(flip_pipe, i)

def check_collision(pipes):
    for i in pipes:
        if bird_rect.colliderect(i):
            dead_sound.play()
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 650:
        return False
    
    return True

def rotate_bird(image):
    new_bird = pygame.transform.rotozoom(image, -bird_movement*3, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect

def Score_text(game_state):
    if game_state == "active":
        score_set = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_set.get_rect(center = (625, 100))
        screen.blit(score_set, score_rect)

    elif game_state == "game_over":
        score_set = game_font.render("Score: " + str(int(score)), True, (255, 255, 255))
        score_rect = score_set.get_rect(center = (625, 100))
        screen.blit(score_set, score_rect)
        #High Score
        high_score_set = game_font.render("High Score: " + str(int(high_score)), True, (255, 255, 255))
        high_score_rect = high_score_set.get_rect(center = (625, 150))
        screen.blit(high_score_set, high_score_rect)

def update_score():
    global score, high_score
    if score > high_score:
        high_score = score

def game_over():
    global game_active
    if game_active == False:
        gameOverText = game_font.render("GAME OVER", True, (255, 255, 255))
        gameOverRect = gameOverText.get_rect(center = (625, 400))
        screen.blit(gameOverText, gameOverRect)
        #Restart
        restart = game_font.render("Press R to restart the game", True, (255, 255, 255))
        restartRect = restart.get_rect(center = (625, 450))
        screen.blit(restart, restartRect)

#Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(TransBack, (0, 0))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 8
                    flap_sound.play()
                if event.key == pygame.K_r and game_active == False:
                    game_active = True
                    pipe_lst.clear()
                    bird_movement = 0
                    bird_rect.center = (100, 250)
                    score = 0
            if event.type == SPAWNPIPE:
                pipe_lst.extend(create_pipe())
            if event.type == BIRDFLAP:
                if bird_index == 2:
                    bird_index = 0
                else:
                    bird_index += 1
                bird, bird_rect = bird_animation()

    if game_active:
        #Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        game_active = check_collision(pipe_lst)
        screen.blit(rotated_bird, bird_rect)

        #Pipe
        pipe_lst = move_pipe(pipe_lst)
        draw_pipes(pipe_lst)

        #Score
        score += 0.01
        Score_text('active')
    else:
        update_score()
        Score_text('game_over')
        game_over()

    floor_moveX -= 1
    if floor_moveX <= -1575:
        floor_moveX = 0
    draw_floor()
           
    pygame.display.update()
    clock.tick(120)