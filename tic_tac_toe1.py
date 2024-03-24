import pygame
import sys
pygame.init()
from tic_tac_toeNN import next_row, next_col

state_field = 0

def check_win(field, sign):
    zero = 0
    for row in field:
        zero += row.count(0)
        if row.count(sign)==3:
            return sign, False
    for col in range(3):
        if field[0] [col]==sign and field[1] [col]==sign and field[2] [col]==sign:
            return sign, False
    if field[0][0] == sign and field[1][1] == sign and field[2][2] == sign:
        return sign, False
    if field[2][0] == sign and field[1][1] == sign and field[0][2] == sign:
        return sign, False
    if zero ==0:
        return 'Ничья',True
    return False, False
def status_field(field):
    global state_field
    state_field = field
    print(state_field)
def update_score(winner):
    global nScore, pScore, numnSc, numpSc
    if winner == 1:
        pScore += 1
    elif winner == 2:
        nScore += 1
    numnSc = font.render(str(nScore), 1, GREEN)  # Обновление текста счета для нейросети
    numpSc = font.render(str(pScore), 1, GREEN)  # Обновление текста счета для человека

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
WHITE_GREEN = (190, 235, 175)
GREEN = (40, 114, 51)
PINK = (216, 105, 166)
PURPLE = (153, 102, 204)

nScore = 0 #счёт нейросети
pScore = 0 #счёт человека
font = pygame.font.SysFont('arialblack',18)
textnSc = font.render("нейросеть:", 1, GREEN)
textpSc = font.render("человек:", 1, GREEN)
numnSc = font.render(str(nScore), 1, GREEN)
numpSc = font.render(str(pScore), 1, GREEN)

pygame.init()

block = 100
margin = 15
margin_button = 100

width = block*3 + margin*4
height = block*3 + margin*4 + margin_button

rect_nnWin=pygame.Rect((15,360),(150,50)) #победа нейросети
rect_ppWin=pygame.Rect((195,360),(150,50)) #победа человека

window = (width, height)
screen = pygame.display.set_mode(window)
screen.fill(GREEN)
pygame.display.set_caption("Tic-tac-toe")

field = [[0]*3 for i in range (3)]
game_over = False
change = 0 #переменная, с помощью которой узнаём какой игрок сейчас ходит
counter = 0


while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    col = x_mouse // (block + margin)
                    row = y_mouse // (block + margin)
                    if field[row][col] == 0:
                        if change%2==0:
                            field[row][col] = 1
                            status_field(field)
                        else:
                            field[row][col] = 2
                            status_field(field)
                        change+=1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_over = False
                    field = [[0] * 3 for i in range(3)]
                    change = 0
                    screen.fill(GREEN)

        screen.fill(PINK,rect_nnWin)
        screen.fill(PINK,rect_ppWin)
        screen.blit(textnSc, ((15,355),(150,50)))
        screen.blit(textpSc, ((195,355),(150,50)))
        screen.blit(numnSc, ((15, 370), (150, 50)))
        screen.blit(numpSc, ((195, 370), (150, 50)))


        pygame.display.update()

        if not game_over:
            for row in range(3):
                for col in range(3):
                    if field [row] [col] == 1:
                        color = PINK

                    elif field[row][col] == 2:
                        color = PURPLE

                    else:
                        color = WHITE_GREEN
                    x = col*block + (col + 1)*margin
                    y = row*block + (row + 1)*margin
                    pygame.draw.rect(screen, color, (x, y, block, block))
                    if color == PINK:
                        pygame.draw.line(screen, WHITE, (x + 5, y + 5), (x + block - 5, y + block - 5), 7)
                        pygame.draw.line(screen, WHITE, (x + block - 5, y + 5), (x + 5, y + block - 5), 7)
                    elif color == PURPLE:
                        pygame.draw.circle(screen, WHITE, (next_row + block//2, next_col + block//2), block//2 - 3, 5)

        if not game_over:
            if (change - 1) % 2 == 0:
                game_over, is_draw = check_win(field, 1)
                counter = 1

            else:
                game_over, is_draw = check_win(field, 2)
                counter = 2


        if game_over and not is_draw:
            if counter == 1:
                update_score(1)
                counter = -1  # Сброс счетчика
            elif counter == 2:
                update_score(2)
                counter = -1  # Сброс счетчика

        pygame.display.update()
