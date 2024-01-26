import pygame
import time
import random

ss = 15
winx = 720
winy = 480

black = pygame.Color(0 , 0 , 0)
white = pygame.Color(255 , 255 , 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()
pygame.display.set_caption('Snakes')
game_window = pygame.display.set_mode((winx, winy))
fps = pygame.time.Clock()
sp = [100 , 50]

# defining first 4 blocks of snake body
snb = [  [100 , 50] ,
                [90 , 50] ,
                [80 , 50] ,
                [70 , 50]
            ]
fr_pos = [random.randrange(1, (winx//10)) * 10, random.randrange(1, (winy//10)) * 10] #Calculation value (720,480)
fr_spwn = True
# setting default snake direction
direction = 'RIGHT'
change_to = direction
score = 0
color1 = green
# Score function
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score) , True , color1)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
    
    
def game_over():
    my_font = pygame.font.SysFont('italic', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score) , True , red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (winx/2, winy/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
    
# Main Function
while True:
   
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously we don't want snake to move into two directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        sp[1] -= 10      #sp =[100,50]
    if direction == 'DOWN':
        sp[1] += 10
    if direction == 'LEFT':
        sp[0] -= 10
    if direction == 'RIGHT':
        sp[0] += 10
 
    # Snake body growing mechanism if fruits and snakes collide then scores will be incremented by 10
    snb.insert(0, list(sp))
    if sp[0] == fr_pos[0] and sp[1] == fr_pos[1]:
        score += 10
        fr_spwn = False
    else:
        snb.pop()
         
    if not fr_spwn:
        fr_pos = [random.randrange(1, (winx//10)) * 10, random.randrange(1, (winy//10)) * 10]
         
    fr_spwn = True
    game_window.fill(black)
     
    for pos in snb:
        pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(game_window, green, pygame.Rect(fr_pos[0], fr_pos[1], 10, 10))
 
    # Game Over conditions
    if sp[0] < 0 or sp[0] > winx-10:
        game_over()
    if sp[1] < 0 or sp[1] > winy-10:
        game_over()

    for block in snb[1:]:
        if sp[0] == block[0] and sp[1] == block[1]:
            game_over()
    show_score(1, white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(ss)