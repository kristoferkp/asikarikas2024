import random
import pygame

pygame.font.init()

# global variables

col = 10  # 10 columns
row = 20  # 20 rows
s_width = 300 # window width
s_height = 600  # window height
play_width = 300 
play_height = 600
block_size = 30  # size of block

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

fontpath = 'arcade.ttf'
fontpath_mario = 'mario.ttf'

# shapes formats

CrossBlock = [['.....',
      '.....',
      '..0..',
      '.000.',
      '..0..']]

LBlock = [['.....',
      '.....',
      '.00..',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '.....',
      '.....'],
      ['.....',
       '.....',
       '..0..',
       '.00..',
       '.....'],
       ['.....',
        '.0...',
        '.00..',
        '.....',
        '.....']]

I = [['.....',
      '..0..',
      '..0..',
      '..0..',
      '..0..'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

TZBlock = [['.....',
      '..0..',
      '.000.',
      '.0...',
      '.....'],
      ['.....',
       '.00..',
       '..00.',
       '..0..',
       '.....'],
       ['.....',
        '.....',
        '...0.',
        '.000.',
        '..0..'],
        ['.....',
         '..0..',
         '.00..',
         '..00.',
         '.....']]

OneBlock = [['.....',
      '.00..',
      '..0..',
      '.000.',
      '.....'],
     ['.....',
      '.0.0.',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '..00.'],
     ['.....',
      '...0.',
      '.000.',
      '.0.0.',
      '.....']]

UBlock = [['.....',
      '.000.',
      '.0.0.',
      '.....',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '.00..',
      '.....'],
     ['.....',
      '.0.0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..00.',
      '.....']]

RectangleBlock = [['.....',
      '.000.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..00.',
      '..00.',
      '.....']]


shapes = [CrossBlock, LBlock, I, TZBlock, OneBlock, UBlock, RectangleBlock]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]




class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)] 
        self.rotation = 0  


# initialise the grid
def create_grid(locked_pos={}):
    grid = [[(0, 0, 0) for x in range(col)] for y in range(row)]  

    for y in range(row):
        for x in range(col):
            if (x, y) in locked_pos:
                color = locked_pos[
                    (x, y)]  
                grid[y][x] = color 

    return grid


def convert_shape_format(piece):
    positions = []
    shape_format = piece.shape[piece.rotation % len(piece.shape)] 

    '''
    e.g.
       ['.....',
        '.....',
        '..00.',
        '.00..',
        '.....']
    '''
    for i, line in enumerate(shape_format):
        row = list(line)  
        for j, column in enumerate(row):  
            if column == '0':
                positions.append((piece.x + j, piece.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4) 

    return positions


# checks if current position of piece in grid is valid
def valid_space(piece, grid):
    accepted_pos = [[(x, y) for x in range(col) if grid[y][x] == (0, 0, 0)] for y in range(row)]
    accepted_pos = [x for item in accepted_pos for x in item]

    formatted_shape = convert_shape_format(piece)

    for pos in formatted_shape:
        if pos not in accepted_pos:
            if pos[1] >= 0:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


# draws text in the middle
def draw_text_middle(text, size, color, surface):
    font = pygame.font.Font(fontpath, size)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + play_height/2 - (label.get_height()/2)))


# draws the lines of the grid for the game
def draw_grid(surface):
    r = g = b = 0
    grid_color = (r, g, b)

    for i in range(row):
        pygame.draw.line(surface, grid_color, (top_left_x, top_left_y + i * block_size),
                         (top_left_x + play_width, top_left_y + i * block_size))
        for j in range(col):
            pygame.draw.line(surface, grid_color, (top_left_x + j * block_size, top_left_y),
                             (top_left_x + j * block_size, top_left_y + play_height))



def clear_rows(grid, locked):
    increment = 0
    for i in range(len(grid) - 1, -1, -1):      
        grid_row = grid[i]                      
        if (0, 0, 0) not in grid_row:           
            increment += 1
            index = i                           
            for j in range(len(grid_row)):
                try:
                    del locked[(j, i)]          
                except ValueError:
                    continue

    # shift every row one step down
    # delete filled bottom row
    # add another empty row on the top
    # move down one step
    if increment > 0:
        for key in sorted(list(locked), key=lambda a: a[1])[::-1]:
            x, y = key
            if y < index:                       
                new_key = (x, y + increment)    
                locked[new_key] = locked.pop(key)

    return increment


def draw_window(surface, grid, score=0, last_score=0):
    surface.fill((0, 0, 0))  # fill the surface with black

    pygame.font.init()  # initialise font
    font = pygame.font.Font(fontpath_mario, 65)
    label = font.render('TETRIS', 1, (255, 255, 255))  # initialise 'Tetris' text with white

    font = pygame.font.Font(fontpath, 30)
    label = font.render('SCORE   ' + str(score) , 1, (255, 255, 255))

    start_x = top_left_x + play_width + 50
    start_y = top_left_y + (play_height / 2 - 100)


    start_x_hi = top_left_x - 240
    start_y_hi = top_left_y + 200

   
    for i in range(row):
        for j in range(col):
            pygame.draw.rect(surface, grid[i][j],
                             (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)

    draw_grid(surface)

    border_color = (255, 255, 255)
    pygame.draw.rect(surface, border_color, (top_left_x, top_left_y, play_width, play_height), 4)





def main(window):
    locked_positions = {}
    create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.35
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)

        fall_time += clock.get_rawtime()  
        level_time += clock.get_rawtime()

        clock.tick()  

        if level_time/1000 > 5:    # make the difficulty harder every 10 seconds
            level_time = 0
            if fall_speed > 0.15:  
                fall_speed -= 0.005

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1  
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1  
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1

                elif event.key == pygame.K_DOWN:
                    
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                elif event.key == pygame.K_UP:
                    
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

        piece_pos = convert_shape_format(current_piece)

        for i in range(len(piece_pos)):
            x, y = piece_pos[i]
            if y >= 0:
                grid[y][x] = current_piece.color

        if change_piece:  # if the piece is locked
            for pos in piece_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color       # add the key and value in the dictionary
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10    # increment score by 10 for every row cleared

            if last_score < score:
                last_score = score

        draw_window(window, grid, score)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    # Clear the screen
    window.fill((0, 0, 0))
    pygame.display.update()

    draw_text_middle(f'Score {score}', 40, (255, 255, 255), window)
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()


def main_menu(window):
    run = True
    while run:
        draw_text_middle('Start', 50, (255, 255, 255), window)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                main(window)

    pygame.quit()


if __name__ == '__main__':
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Tetris')

    main_menu(win) 
