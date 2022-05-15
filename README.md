# Crash-and-Boom
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
