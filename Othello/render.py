import pygame
import numpy as np
from othello import OthelloEnv
from players import *

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
active_player = 1
while not done:
    if game.getGameOver():
        print("Game Over")
        print(game.score_board())
        time.sleep(1)
        pygame.quit()
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            legal_moves = game._legal_moves(active_player)
            

            (x,y) = pygame.mouse.get_pos()
            row_id = np.floor((y+30)/55)
            col_id = np.floor(x/55)
            match np.floor(x/55):
                case 2:
                    column = 'A'
                case 3:
                    column = 'B'
                case 4:
                    column = 'C'
                case 5:
                    column = 'D'
                case 6:
                    column = 'E'
                case 7:
                    column = 'F'
                case 8:
                    column = 'G'
                case 9:
                    column = 'H'
            # print("{}{}".format(column,int(row_id)))
            if (0<row_id<9) and (1<col_id<10):
                try_move = (int(row_id-1),int(col_id-2))
                if legal_moves[try_move[0]][try_move[1]]==active_player:
                    game.make_move(try_move,active_player)
                    active_player = -active_player
                else:
                    print("Illegal Move")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print(legal_moves)
    # Update the screen
    clock.tick()
    pygame.display.flip()