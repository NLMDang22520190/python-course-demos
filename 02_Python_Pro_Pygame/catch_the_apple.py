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
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Apple - Pro Level")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)

# Game Variables
def reset_game():
    global basket_x, apple_y, apple_x, apple_speed, score, lives, game_over
    basket_x = WIDTH // 2 - 50
    apple_y = -15
    apple_x = random.randint(15, WIDTH - 15)
    apple_speed = 5
    score = 0
    lives = 3
    game_over = False

# Basket Properties
basket_width = 100
basket_height = 20
basket_y = HEIGHT - 40
basket_speed = 7

apple_radius = 15

# Initialize the first game state
reset_game()

# -------------------------------------------------------------------
# 1. The Game Loop
# -------------------------------------------------------------------
running = True
while running:
    # -------------------------------------------------------------------
    # 2. Event Handling
    # -------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle restarting the game with the 'R' key if game is over
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                reset_game()

    # Check for held down keys for moving the basket (only if playing!)
    keys = pygame.key.get_pressed()
    
    # -------------------------------------------------------------------
    # 3. Game Logic: States, Collisions & Scoring
    # -------------------------------------------------------------------
    if not game_over:
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
            
        if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
            basket_x += basket_speed

        # Update Apple position (falling down)
        apple_y += apple_speed
        
        # Check if apple hit the ground (missed)
        if apple_y > HEIGHT:
            lives -= 1
            apple_y = -apple_radius
            apple_x = random.randint(apple_radius, WIDTH - apple_radius)
            
            # Change state to Game Over if lives hit 0
            if lives <= 0:
                game_over = True

        # Collision detection: Check for overlap
        if (basket_y < apple_y + apple_radius < basket_y + basket_height and
                basket_x < apple_x < basket_x + basket_width):
            score += 1
            apple_speed += 0.3  # Increase difficulty slightly
            
            # Reset apple at the top
            apple_y = -apple_radius
            apple_x = random.randint(apple_radius, WIDTH - apple_radius)

    # -------------------------------------------------------------------
    # 4. Drawing Phase
    # -------------------------------------------------------------------
    screen.fill(BLACK)  # Clear the screen every frame

    if not game_over:
        # Draw the target (Apple) as a circle
        pygame.draw.circle(screen, RED, (int(apple_x), int(apple_y)), apple_radius)

        # Draw the player (Basket) as a rectangle
        pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))

        # Draw Heads Up Display (HUD) - Score and Lives
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, YELLOW)
        
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))
        
    else:
        # Draw Game Over Screen
        game_over_text = large_font.render("GAME OVER", True, RED)
        restart_text = font.render("Press 'R' to Restart", True, WHITE)
        final_score = font.render(f"Final Score: {score}", True, YELLOW)
        
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        screen.blit(final_score, (WIDTH // 2 - 80, HEIGHT // 2 + 20))
        screen.blit(restart_text, (WIDTH // 2 - 110, HEIGHT // 2 + 70))

    # Update the display
    pygame.display.flip()

    # Maintain frame rate (60 FPS)
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()
