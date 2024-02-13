import pygame
import sys
from math import sin, cos, pi;

# Initialize Pygame
pygame.init()


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (235, 52, 225)

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")

center_x = WIDTH // 2
center_y = HEIGHT // 2

UPPER_ARM_LENGTH = 100;
FOREARM_LENGTH = UPPER_ARM_LENGTH * 0.88 # typical proportions




elbow_angle = (3.0 * pi / 2.0) 

def get_elbow_coord():
  og_x = UPPER_ARM_LENGTH * cos(elbow_angle)
  og_y = UPPER_ARM_LENGTH * sin(elbow_angle)

  return (og_x + center_x, og_y + center_y)
    
elbow_x = center_x - UPPER_ARM_LENGTH
elbow_y = center_y - UPPER_ARM_LENGTH



# Game loop
clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)  # Fill the screen with white color
    elbow_angle += 0.01
    print(get_elbow_coord())
    pygame.draw.line(screen, WHITE, (center_x, center_y), get_elbow_coord(), 5)



    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

    clock.tick(60)
