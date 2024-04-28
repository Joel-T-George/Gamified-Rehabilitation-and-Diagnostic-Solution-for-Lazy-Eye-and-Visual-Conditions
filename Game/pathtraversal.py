import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 105, 180)

# Set font
font = pygame.font.SysFont(None, 36)

# Function to display text
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to generate random points
def generate_points(num_points):
    return [(random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50)) for _ in range(num_points)]

# Function to draw smooth path
def draw_smooth_path(points):
    if len(points) < 2:
        return

    for i in range(len(points) - 1):
        pygame.draw.line(screen, WHITE, points[i], points[i + 1], 10)

# Function to check if mouse is over the player
def is_mouse_over_player(player_pos, mouse_pos):
    return math.sqrt((player_pos[0] - mouse_pos[0]) ** 2 + (player_pos[1] - mouse_pos[1]) ** 2) < 25

# Initialize Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Path Traversal Game")

# Generate points
points = generate_points(10)
start_point = points[0]
end_point = points[-1]

# Set player position to starting point
player_pos = start_point

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black color
    screen.fill(BLACK)

    # Draw smooth path
    draw_smooth_path(points)

    # Draw starting and ending points
    pygame.draw.circle(screen, PINK, start_point, 10)
    pygame.draw.circle(screen, PINK, end_point, 10)

    # Draw player element
    pygame.draw.circle(screen, YELLOW, player_pos, 25)

    # Move player element if mouse is over it
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if is_mouse_over_player(player_pos, mouse_pos):
            player_pos = mouse_pos

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
