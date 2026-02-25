import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Apple")
clock = pygame.time.Clock()

# Basket (Player) properties
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 40
basket_speed = 7

# Apple properties
apple_radius = 15
apple_x = random.randint(apple_radius, WIDTH - apple_radius)
apple_y = -apple_radius
apple_speed = 5

score = 0
font = pygame.font.SysFont(None, 36)

# -------------------------------------------------------------------
# 1. The Game Loop
# A game loop runs continuously until the game is over or the window is closed.
# It processes inputs, updates game logic, and draws everything to the screen.
# -------------------------------------------------------------------
running = True
while running:
    # -------------------------------------------------------------------
    # 2. Event Handling
    # This loop checks for user inputs like key presses or clicking the 'X' button.
    # -------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for held down keys for moving the basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Update Apple position (falling down)
    apple_y += apple_speed

    # -------------------------------------------------------------------
    # 3. Collision Detection & Scoring
    # Check if the apple has touched the basket or hit the ground.
    # -------------------------------------------------------------------
    
    # Check if apple hit the ground (missed)
    if apple_y > HEIGHT:
        # Reset apple at the top
        apple_y = -apple_radius
        apple_x = random.randint(apple_radius, WIDTH - apple_radius)
        score = 0  # Reset score on miss

    # Collision detection: Check if the apple coordinates overlap with the basket rectangle
    # We use a simple bounding box logic check
    if (basket_y < apple_y + apple_radius < basket_y + basket_height and
            basket_x < apple_x < basket_x + basket_width):
        # Caught the apple!
        score += 1
        apple_speed += 0.2  # Increase difficulty slightly
        
        # Reset apple at the top
        apple_y = -apple_radius
        apple_x = random.randint(apple_radius, WIDTH - apple_radius)

    # --- Drawing ---
    screen.fill(BLACK)  # Clear the screen every frame

    # Draw the target (Apple) as a circle
    pygame.draw.circle(screen, RED, (int(apple_x), int(apple_y)), apple_radius)

    # Draw the player (Basket) as a rectangle
    pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))

    # Draw Score Text
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Maintain frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()
