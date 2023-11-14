import pygame
import sys
import random

# Pygame initialization
pygame.init()

# Setting variables
width, height = 800, 400
ground_height = 50
initial_game_speed = 15
initial_jump_speed = 20
gravity = 1.5
acceleration_rate = 0.02
max_speed = 30
color_change_interval = 6 * 1000  # 6 seconds

# Color setting
black = (0, 0, 0)
green = (0, 255, 0)

# Player setup
player_width, player_height = 50, 50
player_x, player_y = 100, height - ground_height - player_height
player_y_velocity = 0
jump_speed = initial_jump_speed

# Prepare obstacles
obstacle_width, obstacle_height = 30, 30
obstacle_x, obstacle_y = width, height - ground_height - obstacle_height
obstacle_color = green

#Screen setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino Game")

# Font setting
font = pygame.font.Font(None, 36)

def jump():
	global player_y_velocity
	if player_y==height-ground_height-player_height:player_y_velocity=-jump_speed

# Main game
game_speed = initial_game_speed
color_change_timer = pygame.time.get_ticks() + color_change_interval
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    # History movement
    player_y_velocity += gravity
    player_y += player_y_velocity

    if player_y > height - ground_height - player_height:
        player_y = height - ground_height - player_height
        player_y_velocity = 0

    # Movement of obstacles
    obstacle_x -= game_speed
    if obstacle_x < 0:
        obstacle_x = width
        obstacle_height = random.randint(20, 100)
        obstacle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Crash inspection
    if (
        player_x < obstacle_x + obstacle_width
        and player_x + player_width > obstacle_x
        and player_y < obstacle_y + obstacle_height
        and player_y + player_height > obstacle_y
    ):
        print("Game Over!")
        obstacle_x = width  # Reset the obstacle location
        player_y = height - ground_height - player_height  # Reset player location
        player_y_velocity = 0  # Reset appointment date
        jump_speed = initial_jump_speed  # Reset jump speed
        game_speed = initial_game_speed  # Reset game speed
        color_change_timer = pygame.time.get_ticks() + color_change_interval  #Reset timer to change color

    # Gradually updating game speed
    if game_speed < max_speed:
        game_speed += acceleration_rate

    # Update cube color every 6 seconds
    current_time = pygame.time.get_ticks()
    if current_time > color_change_timer:
        obstacle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        color_change_timer = current_time + color_change_interval

    # Screen setup
    screen.fill(black)

    # Player drawing
    pygame.draw.rect(screen, green, (player_x, player_y, player_width, player_height))

    # Obstacle drawing
    pygame.draw.rect(screen, obstacle_color, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Land drawing
    pygame.draw.rect(screen, green, (0, height - ground_height, width, ground_height))

    # Screen refresh
    pygame.display.flip()

    # Hour sports
    pygame.time.Clock().tick(30)
