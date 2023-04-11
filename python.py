import pygame
import random

# инициализация пайгейм
pygame.init()

# обновление экрана
width = 640
height = 480
display = pygame.display.set_mode((width, height))

pygame.display.update()
pygame.display.set_caption("игра Змейка by M Hryhoriev")

# назначение цвета
colors = {
    "snake_head": (0, 255, 0),
    "snake_tail": (0, 200, 0),
    "apple": (255, 0, 0)
}

# snake позиция
snake_pos = {
    "x": width / 2 - 10,
    "y": height / 2 - 10,
    "x_change": 0,
    "y_change": 0
}

# snake роз мер
snake_size = (10, 10)

# snake скорость
snake_speed = 10

# snake хвост
snake_tails = []

snake_pos["x_change"] = -snake_speed
for i in range(75):
    snake_tails.append([snake_pos["x"] + 10 * i, snake_pos["y"]])

# еда
food_pos = {
    "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
    "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
}

food_size = (10, 10)
food_eaten = 0

# петля
game_end = False
clock = pygame.time.Clock()

while not game_end:
    # старт петли
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_pos["x_change"] == 0:
                # движение в лево
                snake_pos["x_change"] = -snake_speed
                snake_pos["y_change"] = 0

            elif event.key == pygame.K_RIGHT and snake_pos["x_change"] == 0:
                # движение в право
                snake_pos["x_change"] = snake_speed
                snake_pos["y_change"] = 0

            elif event.key == pygame.K_UP and snake_pos["y_change"] == 0:
                # в верх
                snake_pos["x_change"] = 0
                snake_pos["y_change"] = -snake_speed

            elif event.key == pygame.K_DOWN and snake_pos["y_change"] == 0:
                # в низ
                snake_pos["x_change"] = 0
                snake_pos["y_change"] = snake_speed

    # экран
    display.fill((0, 0, 0))

    # движение змеиного хвоста
    ltx = snake_pos["x"]
    lty = snake_pos["y"]

    for i, v in enumerate(snake_tails):
        _ltx = snake_tails[i][0]
        _lty = snake_tails[i][1]

        snake_tails[i][0] = ltx
        snake_tails[i][1] = lty

        ltx = _ltx
        lty = _lty

    # изображение хвоста
    for t in snake_tails:
        pygame.draw.rect(display, colors["snake_tail"], [
            t[0],
            t[1],
            snake_size[0],
            snake_size[1]])

    # изображение змеи
    snake_pos["x"] += snake_pos["x_change"]
    snake_pos["y"] += snake_pos["y_change"]

    # телепорт змеи
    if (snake_pos["x"] < -snake_size[0]):
        snake_pos["x"] = width

    elif (snake_pos["x"] > width):
        snake_pos["x"] = 0

    elif (snake_pos["y"] < -snake_size[1]):
        snake_pos["y"] = height

    elif (snake_pos["y"] > height):
        snake_pos["y"] = 0

    pygame.draw.rect(display, colors["snake_head"], [
        snake_pos["x"],
        snake_pos["y"],
        snake_size[0],
        snake_size[1]])

    # изображение еды
    pygame.draw.rect(display, colors["apple"], [
        food_pos["x"],
        food_pos["y"],
        food_size[0],
        food_size[1]])

    # столкновение змеи с едой
    if (snake_pos["x"] == food_pos["x"]
            and snake_pos["y"] == food_pos["y"]):
        food_eaten += 1
        snake_tails.append([food_pos["x"], food_pos["y"]])

        food_pos = {
            "x": round(random.randrange(0, width - snake_size[0]) / 10) * 10,
            "y": round(random.randrange(0, height - snake_size[1]) / 10) * 10,
        }

    # столкновение с хвостом
    for i, v in enumerate(snake_tails):
        if (snake_pos["x"] + snake_pos["x_change"] == snake_tails[i][0]
                and snake_pos["y"] + snake_pos["y_change"] == snake_tails[i][1]):
            snake_tails = snake_tails[:i]
            break

    pygame.display.update()

    # набор FPS
    clock.tick(30)

# конец игры
pygame.quit()
quit()