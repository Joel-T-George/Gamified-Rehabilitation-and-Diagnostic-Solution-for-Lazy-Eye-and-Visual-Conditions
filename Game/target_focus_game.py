import pygame
import random
import time
import pyautogui

# Initialize Pygame
pygame.init()
w,h = pyautogui.size()
# Set screen dimensions
SCREEN_WIDTH = w
SCREEN_HEIGHT = h

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set font
font = pygame.font.SysFont(None, 36)

# Function to display text
def display_text(text, color, x, y, angle=0):
    text_surface = pygame.transform.rotate(font.render(text, True, color), angle)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to generate random alphabet
def generate_alphabet():
    alphabets =[]
    for i in range(10):
        alphabets.append((random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50), random.randint(0, 360)))
    print(alphabets)
    return alphabets

# Function to generate random numbers
def generate_numbers():
    numbers = []
    for i in range(10):
        numbers.append((random.randint(1, 9), random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50), random.randint(0, 360)))
    print(numbers)
    return numbers

# Function to check if a point is inside a rectangle
def is_inside_rect(point, rect):
    x, y = point
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh

# Initialize Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Alphabet and Numbers Game")

# Main game loop
running = True
clock = pygame.time.Clock()
start_time = None
fade_time = 3
numbers = generate_numbers()
alphabets = generate_alphabet()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # Fill the background with black color
    screen.fill(BLACK)

    # Display random alphabet
    #alphabet = generate_alphabet()
    #display_text(alphabet, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    for letter, x, y, angle in alphabets:
        display_text(letter, WHITE, x, y, angle)

    # Display random numbers
    for num, x, y, angle in numbers:
        num_text = str(num)
        display_text(num_text, WHITE, x, y, angle)

        # Check if any number is clicked
        
        mouse_pos = pygame.mouse.get_pos()
        text_rect = font.render(num_text, True, WHITE).get_rect(center=(x, y))
        if is_inside_rect(mouse_pos, text_rect):
            if start_time is None:
                start_time = time.time()
            elif time.time() - start_time > fade_time:
                numbers.remove((num, x, y, angle))
                if not numbers:
                    running = False
            break

    # Update the display
    pygame.display.flip()
    clock.tick(60)


pygame.quit()