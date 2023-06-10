import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

paddle_width = 10
paddle_height = 100
paddle_speed_a = 5
paddle_speed_b = 3

paddle_a_x = 50
paddle_a_y = HEIGHT / 2 - paddle_height / 2

paddle_b_x = WIDTH - 50 - paddle_width
paddle_b_y = HEIGHT / 2 - paddle_height / 2

ball_size = 10
ball_x = WIDTH / 2 - ball_size / 2
ball_y = HEIGHT / 2 - ball_size / 2
ball_speed_x = 3
ball_speed_y = 3

font = pygame.font.Font(None, 36)


def update():
    global paddle_a_y, paddle_b_y, ball_x, ball_y, ball_speed_x, ball_speed_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a_y > 0:
        paddle_a_y -= paddle_speed_a
    if keys[pygame.K_s] and paddle_a_y < HEIGHT - paddle_height:
        paddle_a_y += paddle_speed_a

    if paddle_b_y + paddle_height / 2 < ball_y:
        paddle_b_y += paddle_speed_b
    if paddle_b_y + paddle_height / 2 > ball_y:
        paddle_b_y -= paddle_speed_b

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= paddle_a_x + paddle_width and paddle_a_y <= ball_y <= paddle_a_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    if ball_x >= paddle_b_x - ball_size and paddle_b_y <= ball_y <= paddle_b_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y = -ball_speed_y

    if ball_x < 0:
        end_game("Гравець справа переміг!")
    elif ball_x > WIDTH - ball_size:
        end_game("Молодець! Ти переміг!")

    window.fill(BLUE)
    pygame.draw.rect(window, WHITE, (paddle_a_x, paddle_a_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (paddle_b_x, paddle_b_y, paddle_width, paddle_height))
    pygame.draw.ellipse(window, WHITE, (ball_x, ball_y, ball_size, ball_size))

    pygame.display.flip()


def end_game(result):
    pygame.quit()
    print(result)


running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()

pygame.quit()
