import pygame

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

white_moved = {'king': False, 'rook_left': False, 'rook_right': False}
black_moved = {'king': False, 'rook_left': False, 'rook_right': False}

en_passant_target = None
game_over = False
winner = None

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                   (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

black_queen = pygame.image.load('assets/images/bQ.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/bK.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/bR.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/bB.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/bN.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/bp.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/wQ.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/wK.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/wR.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/wB.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/wN.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/wp.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]

piece_list = ['pawn','queen','king','knight','rook','bishop']


def draw_board():
    for i in range(32):
        column  = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen,'ivory',[600-(column*200),row * 100, 100, 100])
        else:
            pygame.draw.rect(screen,'ivory',[700-(column*200),row * 100, 100, 100])
    
    pygame.draw.rect(screen,'gray',[0,800,WIDTH,100])
    pygame.draw.rect(screen,'gray',[800,0,200,HEIGHT])
    pygame.draw.rect(screen,'black',[0,800,WIDTH,100],5)
    pygame.draw.rect(screen,'black',[800,0,200,HEIGHT],5)

    status_text = ['White: Select a Piece to Move','White: Select a Destination to play',
                   'Black: Select a Piece to Move', 'Black: Select a Destination to play']
    
    screen.blit(medium_font.render(status_text[turn_step],True,'black'),(20,820))

    for i in range(9):
        pygame.draw.line(screen,'black',(0,100*i),(800,100*i),2)
        pygame.draw.line(screen,'black',(100*i,0),(100*i,800),2)


def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn,(white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index],(white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen,'green',[white_locations[i][0] * 100 + 1,white_locations[i][1] * 100 + 1, 100, 100],2)
        
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn,(black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100, 100], 2)


def check_pawn(position, color):
    moves_list = []

    if color == 'white':
        direction = 1
        start_row = 1
        enemy = black_locations
        friend = white_locations
    else:
        direction = -1
        start_row = 6
        enemy = white_locations
        friend = black_locations

    if (position[0], position[1] + direction) not in enemy + friend and 0 <= position[1] + direction <= 7:
        moves_list.append((position[0], position[1] + direction))

        if position[1] == start_row and (position[0], position[1] + 2*direction) not in enemy + friend:
            moves_list.append((position[0], position[1] + 2*direction))

    for dx in [-1, 1]:
        target = (position[0] + dx, position[1] + direction)
        if 0 <= target[0] <= 7 and 0 <= target[1] <= 7 and target in enemy:
            moves_list.append(target)

    if en_passant_target:
        if abs(en_passant_target[0] - position[0]) == 1 and en_passant_target[1] == position[1] + direction:
            moves_list.append(en_passant_target)

    return moves_list


def check_rook(position,color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations
    
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


def check_bishop(position,color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations

    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
            
    return moves_list


def check_knight(position,color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations

    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


def check_queen(position,color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


def check_king(position, color):
    moves_list = []

    if color == 'white':
        friends = white_locations
        enemies = black_locations
        moved = white_moved
        row = 0
    else:
        friends = black_locations
        enemies = white_locations
        moved = black_moved
        row = 7

    # normal king moves
    targets = [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(0,1),(0,-1)]
    for dx, dy in targets:
        target = (position[0] + dx, position[1] + dy)
        if 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            if target not in friends:
                moves_list.append(target)

    # castling (ONLY board emptiness + moved flags)
    if not moved['king']:
        # king side
        if not moved['rook_right']:
            if all((x, row) not in friends + enemies for x in [5, 6]):
                moves_list.append((6, row))

        # queen side
        if not moved['rook_left']:
            if all((x, row) not in friends + enemies for x in [1, 2, 3]):
                moves_list.append((2, row))

    return moves_list




def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


def draw_valid(moves):
    if turn_step < 2:
        color = 'green'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


def get_king_position(color):
    if color == 'white':
        king_index = white_pieces.index('king')
        return white_locations[king_index]
    else:
        king_index = black_pieces.index('king')
        return black_locations[king_index]


def is_in_check(color):
    king_pos = get_king_position(color)

    if color == 'white':
        enemy_moves = check_options(black_pieces, black_locations, 'black')
    else:
        enemy_moves = check_options(white_pieces, white_locations, 'white')

    for moves in enemy_moves:
        if king_pos in moves:
            return True
    return False


def is_square_attacked(square, by_color):
    if by_color == 'white':
        enemy_moves = check_options(white_pieces, white_locations, 'white')
    else:
        enemy_moves = check_options(black_pieces, black_locations, 'black')

    for moves in enemy_moves:
        if square in moves:
            return True
    return False


def check_valid_moves():
    if turn_step <= 1:
        color = 'white'
        options_list = white_options
        pieces = white_pieces
        locations = white_locations
        enemy_pieces = black_pieces
        enemy_locations = black_locations
        enemy_color = 'black'
    else:
        color = 'black'
        options_list = black_options
        pieces = black_pieces
        locations = black_locations
        enemy_pieces = white_pieces
        enemy_locations = white_locations
        enemy_color = 'white'

    legal_moves = []
    piece = pieces[selection]
    original_pos = locations[selection]

    for move in options_list[selection]:
        locations[selection] = move

        captured_piece = None
        captured_index = None
        captured_location = None

        if move in enemy_locations:
            captured_index = enemy_locations.index(move)
            captured_piece = enemy_pieces.pop(captured_index)
            captured_location = enemy_locations.pop(captured_index)

        in_check = is_in_check(color)

        # restore captured piece
        if captured_piece:
            enemy_pieces.insert(captured_index, captured_piece)
            enemy_locations.insert(captured_index, captured_location)

        locations[selection] = original_pos

        if not in_check:
            # extra castling safety: king cannot pass through check
            if piece == 'king' and abs(move[0] - original_pos[0]) == 2:
                row = 0 if color == 'white' else 7
                mid_square = (5, row) if move[0] == 6 else (3, row)
                if not is_square_attacked(mid_square, enemy_color):
                    legal_moves.append(move)
            else:
                legal_moves.append(move)

    return legal_moves



def draw_captured():
    for i in range(len(captured_piece_white)):
        captured_piece = captured_piece_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50 * i))
    for i in range(len(captured_piece_black)):
        captured_piece = captured_piece_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50 * i))


run = True
black_options = check_options(black_pieces,black_locations,'black')
white_options = check_options(white_pieces,white_locations,'white')

while run:
    timer.tick(fps)
    screen.fill('chocolate')

    draw_board()
    draw_pieces()
    draw_captured()

    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coord = (x_coord, y_coord)

            if turn_step <= 1:
                if click_coord in white_locations:
                    selection = white_locations.index(click_coord)
                    if turn_step == 0:
                        turn_step = 1

                elif click_coord in valid_moves and selection != 100:
                    piece = white_pieces[selection]
                    old_x, old_y = white_locations[selection]
                    new_x, new_y = click_coord

                    white_locations[selection] = click_coord

                    if piece == 'king':
                        white_moved['king'] = True
                        if abs(old_x - new_x) == 2:
                            if new_x == 6:
                                for i, loc in enumerate(white_locations):
                                    if loc == (7, 0) and white_pieces[i] == 'rook':
                                        white_locations[i] = (5, 0)
                                        break
                        
                            elif new_x == 2:
                                for i, loc in enumerate(white_locations):
                                    if loc == (0, 0) and white_pieces[i] == 'rook':
                                        white_locations[i] = (3, 0)
                                        break
                            white_moved['rook_right'] = True if new_x == 6 else white_moved['rook_right']
                            white_moved['rook_left'] = True if new_x == 2 else white_moved['rook_left']

                    
                    if piece == 'rook':
                        if old_x == 0 and old_y == 0:
                            white_moved['rook_left'] = True
                        elif old_x == 7 and old_y == 0:
                            white_moved['rook_right'] = True

                    if piece == 'pawn' and abs(old_y - new_y) == 2:
                        en_passant_target = (new_x, (old_y + new_y) // 2)
                    else:
                        en_passant_target = None

                    if click_coord in black_locations:
                        black_piece = black_locations.index(click_coord)
                        captured_piece_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    elif piece == 'pawn' and old_y == 4 and new_y == 5:
                        captured_pos = (new_x, 4)
                        if captured_pos in black_locations and black_pieces[black_locations.index(captured_pos)] == 'pawn':
                            black_piece = black_locations.index(captured_pos)
                            captured_piece_white.append(black_pieces[black_piece])
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)

                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

            else:
                if click_coord in black_locations:
                    selection = black_locations.index(click_coord)
                    if turn_step == 2:
                        turn_step = 3

                elif click_coord in valid_moves and selection != 100:
                    piece = black_pieces[selection]
                    old_x, old_y = black_locations[selection]
                    new_x, new_y = click_coord

                    black_locations[selection] = click_coord

                    if piece == 'king':
                        black_moved['king'] = True
                        if abs(old_x - new_x) == 2:
                            if new_x == 6:
                                for i, loc in enumerate(black_locations):
                                    if loc == (7, 7) and black_pieces[i] == 'rook':
                                        black_locations[i] = (5, 7)
                                        break
                            elif new_x == 2:
                                for i, loc in enumerate(black_locations):
                                    if loc == (0, 7) and black_pieces[i] == 'rook':
                                        black_locations[i] = (3, 7)
                                        break
                            black_moved['rook_right'] = True if new_x == 6 else black_moved['rook_right']
                            black_moved['rook_left'] = True if new_x == 2 else black_moved['rook_left']

                    
                    if piece == 'rook':
                        if old_x == 0 and old_y == 7:
                            black_moved['rook_left'] = True
                        elif old_x == 7 and old_y == 7:
                            black_moved['rook_right'] = True

                    if piece == 'pawn' and abs(old_y - new_y) == 2:
                        en_passant_target = (new_x, (old_y + new_y) // 2)
                    else:
                        en_passant_target = None

                    if click_coord in white_locations:
                        white_piece = white_locations.index(click_coord)
                        captured_piece_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    elif piece == 'pawn' and old_y == 3 and new_y == 2:
                        captured_pos = (new_x, 3)
                        if captured_pos in white_locations and white_pieces[white_locations.index(captured_pos)] == 'pawn':
                            white_piece = white_locations.index(captured_pos)
                            captured_piece_black.append(white_pieces[white_piece])
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)

                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []

    pygame.display.flip()

pygame.quit()