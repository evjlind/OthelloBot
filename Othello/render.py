import pygame
import numpy as np
from othello import OthelloEnv
from players import *
# def render(self):
#     if self.render_mode == 'rgb_array':
#         return self._render_frame()
    
# def _render_frame(self):
#     if self.window is None and self.render_mode == "human":
#         pygame.init()
#         pygame.display.init()
#         self.window = pygame.display.set_mode(
#             (self.window_size, self.window_size)
#         )
#     if self.clock is None and self.render_mode == "human":
#         self.clock = pygame.time.Clock()

#     canvas = pygame.Surface((self.window_size, self.window_size))
#     canvas.fill((255, 255, 255))
#     pix_square_size = (
#         self.window_size / self.size
#     )  # The size of a single grid square in pixels

#     # First we draw the target
#     pygame.draw.rect(
#         canvas,
#         (255, 0, 0),
#         pygame.Rect(
#             pix_square_size * self._target_location,
#             (pix_square_size, pix_square_size),
#         ),
#     )
#     # Now we draw the agent
#     pygame.draw.circle(
#         canvas,
#         (0, 0, 255),
#         (self._agent_location + 0.5) * pix_square_size,
#         pix_square_size / 3,
#     )

#     # Finally, add some gridlines
#     for x in range(self.size + 1):
#         pygame.draw.line(
#             canvas,
#             0,
#             (0, pix_square_size * x),
#             (self.window_size, pix_square_size * x),
#             width=3,
#         )
#         pygame.draw.line(
#             canvas,
#             0,
#             (pix_square_size * x, 0),
#             (pix_square_size * x, self.window_size),
#             width=3,
#         )

#     if self.render_mode == "human":
#         # The following line copies our drawings from `canvas` to the visible window
#         self.window.blit(canvas, canvas.get_rect())
#         pygame.event.pump()
#         pygame.display.update()

#         # We need to ensure that human-rendering occurs at the predefined framerate.
#         # The following line will automatically add a delay to keep the framerate stable.
#         self.clock.tick(self.metadata["render_fps"])
#     else:  # rgb_array
#         return np.transpose(
#             np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
#         )
    
# def close(self):
#     if self.window is not None:
#         pygame.display.quit()
#         pygame.quit()


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
            print(legal_moves)
            (x,y) = pygame.mouse.get_pos()
            # print((x,y))
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
                # print(try_move)
    # Update the screen
    clock.tick()
    pygame.display.flip()