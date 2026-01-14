import pygame
#initialization of pygame
pygame.init()
WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Rajat's Chess Board")
font = pygame.font.Font('freesansbold.ttf',20)
medium_font = pygame.font.Font('freesansbold.ttf', 35)
big_font = pygame.font.Font('freesansbold.ttf',50)
timer = pygame.time.Clock()
fps = 60

captured_piece_white = []
captured_piece_black = []

turn_step = 0
selection = 100
valid_moves = []
#white pieces and locations
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

#black_pieces and locations
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

#game images laoding 
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

piece_list = ['pawn','queen','king','knight','rook','bishop']

#defined draw board function
def draw_board():
    for i in range(32):
        column  = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen,'ivory',[600-(column*200),row * 100, 100, 100])
        else:
            pygame.draw.rect(screen,'ivory',[700-(column*200),row * 100, 100, 100])
            pygame.draw.rect(screen,'gray',[0,800,WIDTH,1000])
            pygame.draw.rect(screen,'gray',[800,0,200,HEIGHT])
            pygame.draw.rect(screen,'black',[0,800,WIDTH,1000],5)
            pygame.draw.rect(screen,'black',[800,0,200,HEIGHT],5)

            status_text = ['White: Select a Piece to Move','White: Select a Destination to play',
                            'Black: Select a Piece  to Move', 'Black: Select a Destination to play']
            
            screen.blit(big_font.render(status_text[turn_step],True,'black'),(20,820))

            for i in range(9):
                pygame.draw.line(screen,'black',(0,100*i),(800,100*i),2)
                pygame.draw.line(screen,'black',(100*i,0),(100*i,800),2)

#defined draw pieces function
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])

run = True
#main game loop
while run:
    timer.tick(fps)
    screen.fill('chocolate')
    
    #draw_board
    draw_board()

    #draw_pieces
    draw_pieces()

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()