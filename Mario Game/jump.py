import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Character variables
player_rect = pygame.Rect(100, 500, 50, 50)
vel_y = 0
gravity = 0.8
jump_strength = -16
is_jumping = False 

run = True
while run:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                vel_y = jump_strength
                is_jumping = True

    # 2. Physics & Gravity
    vel_y += gravity  # Gravity pulls character down
    player_rect.y += vel_y

    # 3. Ground Collision
    if player_rect.bottom >= 550:
        player_rect.bottom = 550
        vel_y = 0
        is_jumping = False

    # 4. Rendering
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 0), player_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()