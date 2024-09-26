# in progress
import pygame
import numpy as np
from othello import OthelloEnv
from wthor.wthor_parser import *

pygame.init()
game = OthelloEnv()
screen = pygame.display.set_mode((640, 480))

black = (0, 0, 0)
white = (255, 255, 255)
green = (21, 122, 33)
dark_grey = (48, 48, 48)
board = pygame.Surface((440, 440))
board.fill(green)

myfont = pygame.font.SysFont('Times New Roman',16)


cols = ['a             b            c            d            e            f            g            h']
for i in range(1, 8):
    pygame.draw.rect(board, dark_grey, (0, i*55, 440, 2))
    pygame.draw.rect(board, dark_grey, (i*55, 0, 2, 440))



x, y = (0, 0)
done = False
clock = pygame.time.Clock()
text_surface = myfont.render(cols[0],False,(0,0,0))
text_surface2 = myfont.render('1',False,(0,0,0))
text_surface3 = myfont.render('2',False,(0,0,0))
text_surface4 = myfont.render('3',False,(0,0,0))
text_surface5 = myfont.render('4',False,(0,0,0))
text_surface6 = myfont.render('5',False,(0,0,0))
text_surface7 = myfont.render('6',False,(0,0,0))
text_surface8 = myfont.render('7',False,(0,0,0))
text_surface9 = myfont.render('8',False,(0,0,0))

move_num = 0
while not done:
    
    # Clear the screen
    screen.fill(black)

    # Draw board
    screen.blit(board,(105, 20))
    screen.blit(text_surface,(106,18))
    screen.blit(text_surface2,(106,55))
    screen.blit(text_surface3,(106,110))
    screen.blit(text_surface4,(106,165))
    screen.blit(text_surface5,(106,220))
    screen.blit(text_surface6,(106,275))
    screen.blit(text_surface7,(106,330))
    screen.blit(text_surface8,(106,385))
    screen.blit(text_surface9,(106,440))

    for i in range(8):
        for j in range(8):
            if game.board[i][j] == 1:
                pygame.draw.circle(screen,black,(133+j*55,50+i*55),20)
            elif game.board[i][j] == -1:
                pygame.draw.circle(screen,white,(133+j*55,50+i*55),20)
    
    # Handle events
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
                done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_num -= 1
            elif event.key == pygame.K_RIGHT:
                move_num += 1
    # Update the screen
    clock.tick()
    pygame.display.flip()