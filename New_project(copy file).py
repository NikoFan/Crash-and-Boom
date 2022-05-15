import pygame
import time

pygame.init()
# Константы
WIDTH = 1100  # Ширина экрана
HEIGHT = 800  # Высота экрана
GROUND_HEIGHT = 650  # Уровень земли, по которому ходят модельки

SPEED = 10  # Скорость при перемещении
moving_speed = SPEED

# display
display = pygame.display.set_mode((WIDTH, HEIGHT))  # Создается окно по заданным параметрам

# Параметры игрока
userX = WIDTH // 4  # Координата персонажа по х
userY = GROUND_HEIGHT  # Координата персонажа по у
userWidth = 82  # Ширина персонажа
userHeight = 94  # Высота персонажа
combo_counter = 2

attackBoost = 100
attackCount = False

clock = pygame.time.Clock()  # Установка частоты обновления кадров в секунду
jump_counter = 20  # Высота прыжка

jump_R = False  # Идентификатор прыжка вправо
jump_L = False  # Идентификатор прыжка влево
jump_up = False  # Идентификатор прыжка вверх
user_up = 2  # Идентификатор движения вверх
user_down = 2  # Идентификатор движения вниз
choiceX = 2  # Идентификатор движения по горизонтали
stay_sit = 2

pause_time = False
pygame.display.set_caption('Crush and Bomb')
picture = pygame.image.load('background\icon.jpg')  # Редактирование окна
pygame.display.set_icon(picture)

userUp = [[pygame.image.load('модельки персонажа\стоит на месте 1.png'),  # Список с модельками
           pygame.image.load('модельки персонажа\стоит на месте 2.png'),
           pygame.image.load('модельки персонажа\стоит на месте 3.png')],
          [pygame.image.load('модельки персонажа\шифт стоит 1.png'),
           pygame.image.load('модельки персонажа\шифт стоит 2.png'),
           pygame.image.load('модельки персонажа\шифт стоит 3.png'),
           pygame.image.load('модельки персонажа\шифт стоит 4.png'),
           pygame.image.load('модельки персонажа\шифт стоит 5.png')],  # Список состоит из нескольких списков,
          [pygame.image.load('модельки персонажа\бот идет лево.png'),
           # каждый из которых включает в себя отдельные состояния
           pygame.image.load('модельки персонажа\бот идет лево 2.png'),
           # Всего состояний 8(перечислены в порядке, указанном в списке):  # 0. Стоит на месте
           pygame.image.load('модельки персонажа\бот идет лево 3.png')],  # 1. Присел
          [pygame.image.load('модельки персонажа\бот идет вправо.png'),  # 2. Идет влево
           pygame.image.load('модельки персонажа\бот идет вправо 2.png'),  # 3. Идет вправо
           pygame.image.load('модельки персонажа\бот идет вправо 3.png')],  # 4. Прыжок вправо
          [pygame.image.load('модельки персонажа\бот летит вправо.png'),  # 5. Прыжок влево
           pygame.image.load('модельки персонажа\бот летит вправо 2.png'),  # 6. Атака влево
           pygame.image.load('модельки персонажа\бот летит вправо.png')],  # 7. Атака вправо
          [pygame.image.load('модельки персонажа\бот летит лево.png'),  # 8. Движение в присяде
           pygame.image.load('модельки персонажа\бот летит лево 2.png'),
           pygame.image.load('модельки персонажа\бот летит лево.png')],
          [pygame.image.load('модельки персонажа\Attack.png'),
           pygame.image.load('модельки персонажа\Attack_2.png')],
          [pygame.image.load('модельки персонажа\Attack_R.png'),
           pygame.image.load('модельки персонажа\Attack_R_2.png')],
          [pygame.image.load('модельки персонажа\шифт движение 1.png'),
           pygame.image.load('модельки персонажа\шифт движение 2.png'),
           pygame.image.load('модельки персонажа\шифт движение 3.png'),
           pygame.image.load('модельки персонажа\шифт движение 4.png'),
           pygame.image.load('модельки персонажа\шифт движение 5.png'),
           pygame.image.load('модельки персонажа\шифт движение 6.png'),
           pygame.image.load('модельки персонажа\шифт движение 7.png')]]

userID = 0  # UserID означает состояние персонажа(отдельный список с состоянием)
n = 0  # n помогает перебирать все модельки в списке состояния, чтобы получилась полноценная анимация(кроме присяда)
n_sit = 0  # n_sit помогает перебирать все модельки в списке состояния, чтобы получилась полноценная анимация(в присяде)
right_sit = 0
left_sit = 0

sit_anim_counter1 = 0
sit_anim_counter2 = 0

font_color = (0, 0, 0)

# Характеристики врага
enemyX = WIDTH // 2 - 500
enemyY = HEIGHT - GROUND_HEIGHT
enemyWidth = 715
enemyHeight = 564
enemy_jump_counter = 8
enemyColor = 150, 23, 65
enemy_throw = False
killcount = 0
enemy_health = 30

BLACK = (0, 0, 0)

enemyUp = [[pygame.image.load('босс\Хрю.png')],  # Список с состояниями босса
           [pygame.image.load('босс\Хрю сопли 1.png'),
            pygame.image.load('босс\Хрю сопли 2.png'),
            pygame.image.load('босс\Хрю сопли 3.png'),
            pygame.image.load('босс\Хрю сопли 4.png')],
           [pygame.image.load('босс\Хрю слюни 1.png'),
            pygame.image.load('босс\Хрю слюни 2.png'),
            pygame.image.load('босс\Хрю слюни 3.png'),
            pygame.image.load('босс\Хрю слюни 4.png'),
            pygame.image.load('босс\Хрю слюни 5.png'),
            pygame.image.load('босс\Хрю слюни 6.png'),
            pygame.image.load('босс\Хрю слюни 7.png'),
            pygame.image.load('босс\Хрю слюни 8.png'),
            pygame.image.load('босс\Хрю слюни 9.png'),
            pygame.image.load('босс\Хрю слюни 10.png')],
]
enemyID = 0  # enemyID означает состояние босса(отдельный список с состоянием)
m = 0  # n помогает перебирать все модельки в списке состояния, чтобы получилась полноценная анимация
m1 = 0  # n помогает перебирать все модельки в списке состояния, чтобы получилась полноценная анимация
m2 = 0  # n помогает перебирать все модельки в списке состояния, чтобы получилась полноценная анимация
m3 = 0  # n помогает перебирать все модельки в списке состояния, чтобы получилась полноценная анимация
anim_counter1 = 0
anim_counter2 = 0
anim_counter3 = 0

RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIFE_BAR_X = enemyX + enemyWidth / 2 - 150
LIFE_BAR_Y = enemyY - 50

pause_picture = pygame.image.load('background\pause.png')
menu_background = pygame.image.load('background\превью.png')
height_button = 70
width_button = 300
button_color = (0, 23, 150)
show = True


def show_headband():
    global menu_background
    # start_button = button(450, 450)

    while show:  # Запуск игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        display.blit(menu_background, (0, 0))

        button_text(WIDTH / 1.527, HEIGHT // 2 + 110, 'Start Game')
        button_text(WIDTH / 1.527, HEIGHT // 2, 'Store')
        pygame.display.update()
        clock.tick(250)
        mouse_button(WIDTH / 1.527, HEIGHT // 2 + 110)
        mouse_button(WIDTH / 1.527, HEIGHT // 2)


def run_game():  # Основная функция
    global n, jump_L, jump_R, jump_up, attackCount, moving_speed, userID, RED, GREEN
    global choiceX, user_down, user_up, userY, LIFE_BAR_X, LIFE_BAR_Y, n_sit, stay_sit, right_sit, left_sit
    global sit_anim_counter1, sit_anim_counter2
    game = True
    while game:  # Запуск игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  # Функция позволяет игроку закончить работу программы
        land = pygame.image.load('background\BackGround.png')  # Переменная для создания фона
        keys = pygame.key.get_pressed()

        userID = 0
        if n % 3 == 1:
            n = 0
        else:
            n += 1
        # Передвижение
        if keys[pygame.K_s]:  # При нажатии на кнопку s запускается функция движения вниз
            user_down = True
            user_move_down()
        if keys[pygame.K_w]:  # При нажатии на кнопку w запускается функция движения вниз
            user_up = True
            user_move_up()
        if keys[pygame.K_a] and userX > 0:  # При нажатии на кнопку а идентификатор движения по х срабатывает
            choiceX = True  # и приводит функцию user_mode_x() в действие
            user_move_x()
        if keys[pygame.K_d] and userX + userWidth < WIDTH:
            choiceX = False  # При нажатии на кнопку d идентификатор движения по х срабатывает
            user_move_x()  # и приводит функцию user_mode_x() в действие
        # Attack move
        pressed = pygame.mouse.get_pressed()  # Переменная ссылается на функцию, которая распознает нажатие мыши
        # fight
        if pressed[0] and userX + userWidth < WIDTH and userX > 0 and not (keys[pygame.K_LSHIFT]):
            attack_move()  # При нажатии на левую кнопку мыши производится атака
            attackCount = True  # Запускается функция attack_move(), анимация атаки
            fight_mode()
        if killcount >= enemy_health:
            enemy_death()
        if enemy_throw:
            enemy_jumping()
        # Прыжки
        if keys[pygame.K_SPACE] and keys[pygame.K_d] and not (keys[pygame.K_a]):
            jump_R = True  # Если производится соответствующих клавиш, производится прыжок
        if jump_L:  # в указанную сторону
            user_jump()
        if keys[pygame.K_SPACE] and keys[pygame.K_a] and not (keys[pygame.K_d]):
            jump_L = True
        if jump_R:
            user_jump()
        if keys[pygame.K_SPACE] and not (keys[pygame.K_a]) and not (keys[pygame.K_d]):
            jump_up = True
        if jump_up:
            user_jump()
        if userY + userHeight < GROUND_HEIGHT and jump_counter < -20:
            userY = GROUND_HEIGHT - userHeight
            jump_R = False
            jump_L = False
            jump_up = False
        # Пауза
        if keys[pygame.K_ESCAPE]:
            time.sleep(0.3)
            pause_background()

        display.blit(land, (0, 0))
        animation()
        pygame.draw.rect(display, RED, (LIFE_BAR_X, LIFE_BAR_Y, enemy_health * 10, 10))
        pygame.draw.rect(display, GREEN, (LIFE_BAR_X, LIFE_BAR_Y, (enemy_health - killcount) * 10, 10))

        if keys[pygame.K_LSHIFT] and not (keys[pygame.K_a]) and not (keys[pygame.K_d]):
            stay_sit = True
            user_sit_down()
            moving_speed = SPEED - 8
            display.blit(userUp[1][n_sit], (userX, userY))
        elif keys[pygame.K_LSHIFT] and keys[pygame.K_a] and not (keys[pygame.K_d]):
            left_sit = True
            user_sit_down()
            moving_speed = SPEED - 8
            display.blit(userUp[8][sit_anim_counter2], (userX + 50, userY + 65))
        elif keys[pygame.K_LSHIFT] and not (keys[pygame.K_a]) and keys[pygame.K_d]:
            right_sit = True
            user_sit_down()
            moving_speed = SPEED - 8
            display.blit(userUp[8][sit_anim_counter2], (userX + 50, userY + 65))
        if not keys[pygame.K_LSHIFT]:
            display.blit(userUp[userID][n], (userX, userY))
            moving_speed = SPEED
            n_sit = 0
            left_sit = 0
            right_sit = 0
            sit_anim_counter1 = 0
            sit_anim_counter2 = 0

        print_text(f'COMBO: {killcount}', WIDTH // 1.4, 20, BLACK)

        pygame.display.update()
        clock.tick(250)


def attack_move():
    global userID, n, attackBoost, userX, userWidth
    # Атака влево(в прыжке)
    if userID == 3:
        userX += attackBoost + userWidth
        userID = 7
        if n % 3 == 1:
            n = 0
        else:
            n += 1
    # Атака по земле
    elif userID == 2:
        userX -= attackBoost + userWidth
        userID = 6
        if n % 3 == 1:
            n = 0
        else:
            n += 1
    pygame.display.update()
    clock.tick(100)


def fight_mode():
    global enemyColor, enemyX, enemyY, enemyHeight, enemyWidth, userX, userY, attackBoost, userID
    global killcount, enemy_jump_counter, enemy_throw
    if attackCount:
        if ((enemyY <= userY + userHeight <= enemyY + enemyHeight) or (
                enemyY <= userY <= enemyY + enemyHeight)) and userID != 0:
            if (userX + userWidth / 2) <= enemyX + enemyWidth / 2 <= (userX + userWidth / 2) + attackBoost:
                killcount += 1
                enemy_throw = True
            elif (userX + userWidth / 2) - attackBoost <= enemyX + enemyWidth / 2 <= (
                    userX + userWidth / 2):
                killcount += 1
                enemy_throw = True


def user_jump():
    global userY, jump_counter, jump_L, userX, userID, n, jump_R, jump_up, attackCount
    if userY + userHeight > HEIGHT:
        jump_counter = - 21
        userY = HEIGHT - userHeight
    if attackCount:
        jump_counter = -21
        attackCount = False
    # jump up
    elif jump_up:
        time.sleep(0.01)
        if jump_counter >= -20:
            userY -= jump_counter / 1.8
            jump_counter -= 1
            userID = 4
            if n % 3 == 1:
                n = 0
            else:
                n += 1
        else:
            jump_counter = 20
            jump_up = False
    # left jump
    elif jump_L:
        if jump_counter >= -20:
            userY -= jump_counter / 1.8
            jump_counter -= 1
            userID = 5
            if n % 3 == 1:
                n = 0
            else:
                n += 1
        else:
            jump_counter = 20
            jump_L = False
    # right jump
    elif jump_R:
        if jump_counter >= -20:
            userY -= jump_counter / 1.8
            jump_counter -= 1
            userID = 4
            if n % 3 == 1:
                n = 0
            else:
                n += 1
        else:
            jump_counter = 20
            jump_R = False

    pygame.display.update()


def user_move_down():
    global userY, userID, n, userHeight
    if user_down and (userY + userHeight) < HEIGHT:
        userID = 0
        if n % 3 == 1:
            n = 0
        else:
            n += 1
        userY += moving_speed


def user_move_up():
    global userY, userID, n, userHeight
    if user_up and (userY + userHeight) > GROUND_HEIGHT:
        userID = 0
        if n % 3 == 1:
            n = 0
        else:
            n += 1
        userY -= moving_speed
    pygame.display.update()


def user_move_x():
    global choiceX, userX, userID, userY, n
    if choiceX:
        userX -= moving_speed
        userID = 2
        if n % 3 == 1:
            n = 0
        else:
            n += 1
    if not choiceX:
        userX += moving_speed
        userID = 3
        if n % 3 == 1:
            n = 0
        else:
            n += 1
    pygame.display.update()


def user_sit_down():
    global userID, n_sit, stay_sit, sit_anim_counter1, sit_anim_counter2, left_sit, right_sit
    if stay_sit:
        if sit_anim_counter1 >= 4 and n_sit != 4:
            sit_anim_counter1 = 0
            n_sit += 1
        sit_anim_counter1 += 1
    if left_sit:
        if sit_anim_counter2 == -7: # and left_sit == -6:
            sit_anim_counter2 = -1

            left_sit -= 1

            print(sit_anim_counter2)
        sit_anim_counter2 -= 1
        # sit_anim_counter2 = sit_anim_counter2 // 15
        time.sleep(0.01)
    if right_sit:
        if sit_anim_counter2 == 6: #and right_sit != 6:
            sit_anim_counter2 = 0
            right_sit += 1
            # sit_anim_counter2 = sit_anim_counter2 // 8
        sit_anim_counter2 += 1
        time.sleep(0.01)


def print_text(message, x, y, font_color, font_type='TEXT.otf', font_size=72):

    global killcount
    if killcount >= combo_counter and not pause_time:
        font_color = 120, 10, 30
    # font_color = 120, 10, 30
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))

"""    global killcount
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))
    if killcount == combo_counter:
        font_color = 120, 10, 30"""


def enemy_jumping():
    global enemy_jump_counter, enemyY, enemy_throw
    if enemy_jump_counter >= -8:
        enemyY -= enemy_jump_counter / 0.5
        enemy_jump_counter -= 1
    else:
        enemy_jump_counter = 8
        enemy_throw = False
    pygame.display.update()


def animation():
    global m, m1, m2, enemyUp, enemyY, enemyX, enemyID, m3, anim_counter1, anim_counter2, anim_counter3
    display.blit(enemyUp[enemyID][m], (enemyX, enemyY))
    display.blit(enemyUp[enemyID + 1][m3], (enemyX, enemyY))
    display.blit(enemyUp[enemyID + 2][m2], (enemyX, enemyY))
    if anim_counter1 == 2:
        m1 += 1
        anim_counter1 = 0
    if anim_counter3 == 12:
        m3 += 1
        anim_counter3 = 0
    if anim_counter2 == 7:
        m2 += 1
        anim_counter2 = 0
    if m1 == 4:
        m1 = 0
    if m2 == 10:  # Слюни
        m2 = 0
    if m3 == 4:  # Сопли
        m3 = 0
    anim_counter1 += 1
    anim_counter2 += 1
    anim_counter3 += 1


def enemy_death():
    global enemyY, enemy_jump_counter
    enemyY += SPEED * 1.1


def button(x, y):
    global height_button, width_button, button_color
    pygame.draw.rect(display, button_color, (x, y, width_button, height_button))


def button_text(x, y, message, font_type='TEXT.otf', font_size=72):
    global font_color, button_color, menu_background, width_button, height_button
    pygame.draw.rect(menu_background, button_color, (x, y, width_button, height_button))
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x + (len(message) / 1.5), y - 10))


def mouse_button(x, y):
    global width_button, height_button, show, menu_background
    mouse = pygame.mouse.get_pos()
    button_pressed = pygame.mouse.get_pressed()
    loc = [mouse[0], mouse[1]]
    if x < mouse[0] < x + width_button:
        if y < mouse[1] < y + height_button:
            if button_pressed[0]:
                show = False



def pause_background():
    global pause_picture, pause_time
    # start_button = button(450, 450)
    pause_time = True
    while pause_time:  # Запуск игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        display.blit(pause_picture, (0, 0))
        print_text('Paused. Press Esc to continue!', 0, HEIGHT / 1.9, BLACK)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause_time = False
            time.sleep(0.3)
        # start_button.draw(450, 450)
        # button_text(WIDTH / 1.527, HEIGHT // 2 + 110, 'Start (Press P)')
        pygame.display.update()
        clock.tick(250)


show_headband()

run_game()
