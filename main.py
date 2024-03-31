import pygame
import random

pygame.init()

target_x = 0
target_y = 0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
def change_target_xy():
    global target_x , target_y
    global SCREEN_WIDTH, SCREEN_HEIGHT
    global target_x, target_y
    target_x = random.randrange(0, SCREEN_WIDTH - target_width)
    target_y = random.randrange(0, SCREEN_HEIGHT - target_height)

def calculate_points(click_x, click_y):
    # Размеры эллипсов и их координаты
    ellipses = [
        {"x": 23, "y": 46, "width": 4, "height": 5, "points": 500},
        {"x": 19, "y": 42, "width": 10, "height": 12, "points": 300},
        {"x": 16, "y": 38, "width": 17, "height": 20, "points": 200},
        {"x": 12, "y": 33, "width": 26, "height": 29, "points": 100},
        {"x": 0, "y": 0, "width": 51, "height": 100, "points": 50}
    ]

    # Проверяем, попал ли клик в какой-либо из эллипсов
    for ellipse in ellipses:
        dx = (click_x - (ellipse["x"] + ellipse["width"] / 2)) / (ellipse["width"] / 2)
        dy = (click_y - (ellipse["y"] + ellipse["height"] / 2)) / (ellipse["height"] / 2)
        if dx**2 + dy**2 <= 1:
            return ellipse["points"]

    # Если не попал ни в один эллипс, начисляем -50 очков
    return -50


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Cyber Rifle')
icon = pygame.image.load('image/icon_01.png')
pygame.display.set_icon(icon)


target_image = pygame.image.load('image/target_0.png')
target_width = 51
target_height = 100

change_target_xy()

# Загрузка изображения фона
bg_image = pygame.image.load('image/bg_0.jpg')
# Установка шрифта для счетчика очков


font = pygame.font.Font(None, 28)
score = 0
running = True
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
target_timer = 0

while running:
    # Отображение фоновой картинки
    screen.blit(bg_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)
            score += calculate_points(mouse_x-target_x, mouse_y-target_y)
            pygame.display.set_caption(f'Score: {score} x:{target_x} y:{target_y}')
            pygame.mouse.set_visible(True)
            change_target_xy()
            start_time = pygame.time.get_ticks()
            screen.blit(target_image, (target_x, target_y))


    target_timer = pygame.time.get_ticks() - start_time

    if target_timer < 3000:
        screen.blit(target_image, (target_x, target_y))
    else:
        change_target_xy()
        start_time = pygame.time.get_ticks()

    text_score = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text_score, (10, 10))

    text_time = font.render(" time left: " + "{:.2f}".format(3 - target_timer/1000), True, (255, 255, 255))
    screen.blit(text_time, (600, 10))

    pygame.display.update()
    clock.tick(200)


pygame.quite()