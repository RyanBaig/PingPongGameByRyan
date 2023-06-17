import pygame
from pygame.locals import *

# Initialize Pygame and set up the game window
pygame.init()
WIDTH, HEIGHT = 1366, 786
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

# Paddle variables
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
paddle1_x = 50
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_x = WIDTH - 50 - PADDLE_WIDTH
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle1_speed = 0
paddle2_speed = 0

# Ball variables
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_radius = 10
ball_speed_x = 3
ball_speed_y = 3

# Button variables
button_rect = pygame.Rect(WIDTH - 80, 10, 70, 30)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_w:
                paddle1_speed = -3
            elif event.key == K_s:
                paddle1_speed = 3
            elif event.key == K_UP:
                paddle2_speed = -3
            elif event.key == K_DOWN:
                paddle2_speed = 3
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                paddle1_speed = 0
            elif event.key == K_UP or event.key == K_DOWN:
                paddle2_speed = 0
        elif event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                running = False

    # Update paddle positions
    paddle1_y += paddle1_speed
    paddle2_y += paddle2_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collisions with paddles
    if (
        paddle1_x <= ball_x <= paddle1_x + PADDLE_WIDTH
        and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT
    ):
        ball_speed_x = abs(ball_speed_x)
    elif (
        paddle2_x <= ball_x <= paddle2_x + PADDLE_WIDTH
        and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT
    ):
        ball_speed_x = -abs(ball_speed_x)

    # Collisions with walls
    if ball_y <= 0 or ball_y >= HEIGHT - ball_radius:
        ball_speed_y *= -1

    # Check if the ball is outside the screen boundaries
    if ball_x <= 0 or ball_x >= WIDTH:
        running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

    # Draw the "EXIT" button
    pygame.draw.rect(screen, WHITE, button_rect)
    font = pygame.font.Font(None, 24)
    exit_text = font.render("EXIT", True, (0, 0, 0))
    exit_text_rect = exit_text.get_rect(center=button_rect.center)
    screen.blit(exit_text, exit_text_rect)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
