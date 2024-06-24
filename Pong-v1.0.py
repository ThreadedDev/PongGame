import pygame
import random

pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle dimensions
paddle_width = 10
paddle_height = 100

# Ball dimensions
ball_size = 10

# Paddle positions
paddle1_x = 50
paddle1_y = height // 2 - paddle_height // 2
paddle2_x = width - 50 - paddle_width
paddle2_y = height // 2 - paddle_height // 2

# Ball position and velocity
ball_x = width // 2
ball_y = height // 2
ball_vel_x = random.choice([-4, 4])
ball_vel_y = random.choice([-4, 4])

# Paddle velocity
paddle1_vel = 0
paddle2_vel = 0
paddle_speed = 6

# Score
score1 = 0
score2 = 0
font = pygame.font.SysFont(None, 55)

def draw_paddle(x, y):
    pygame.draw.rect(screen, white, (x, y, paddle_width, paddle_height))

def draw_ball(x, y):
    pygame.draw.rect(screen, white, (x, y, ball_size, ball_size))

def draw_score(score, x, y):
    score_text = font.render(str(score), True, white)
    screen.blit(score_text, (x, y))

def game_loop():
    global paddle1_y, paddle2_y, ball_x, ball_y, ball_vel_x, ball_vel_y, score1, score2, paddle1_vel, paddle2_vel

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle1_vel = -paddle_speed
                if event.key == pygame.K_s:
                    paddle1_vel = paddle_speed
                if event.key == pygame.K_UP:
                    paddle2_vel = -paddle_speed
                if event.key == pygame.K_DOWN:
                    paddle2_vel = paddle_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle1_vel = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle2_vel = 0

        paddle1_y += paddle1_vel
        paddle2_y += paddle2_vel

        # Ensure paddles stay on the screen
        paddle1_y = max(min(paddle1_y, height - paddle_height), 0)
        paddle2_y = max(min(paddle2_y, height - paddle_height), 0)

        ball_x += ball_vel_x
        ball_y += ball_vel_y

        # Ball collision with top and bottom
        if ball_y <= 0 or ball_y >= height - ball_size:
            ball_vel_y = -ball_vel_y

        # Ball collision with paddles
        if (ball_x <= paddle1_x + paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height) or \
           (ball_x >= paddle2_x - ball_size and paddle2_y < ball_y < paddle2_y + paddle_height):
            ball_vel_x = -ball_vel_x

        # Ball goes out of bounds
        if ball_x <= 0:
            score2 += 1
            ball_x, ball_y = width // 2, height // 2
            ball_vel_x, ball_vel_y = random.choice([-4, 4]), random.choice([-4, 4])
        if ball_x >= width - ball_size:
            score1 += 1
            ball_x, ball_y = width // 2, height // 2
            ball_vel_x, ball_vel_y = random.choice([-4, 4]), random.choice([-4, 4])

        screen.fill(black)
        draw_paddle(paddle1_x, paddle1_y)
        draw_paddle(paddle2_x, paddle2_y)
        draw_ball(ball_x, ball_y)
        draw_score(score1, width // 4, 20)
        draw_score(score2, 3 * width // 4, 20)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    quit()

game_loop()
