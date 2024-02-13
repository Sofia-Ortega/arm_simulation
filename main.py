import pygame
import sys
from math import sin, cos, pi, radians;

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


# SHOULDER
shoulder_x = center_x
shoulder_y = center_y

# ELBOW 
elbow_x = 0
elbow_y = 0
elbow_angle = 0 
elbow_angle_speed = 3

# WRIST
wrist_x = 0
wrist_y = 0
wrist_angle = 0
wrist_angle_speed = 3


def set_elbow_coord():
  global elbow_x, elbow_y
  elbow_x = (UPPER_ARM_LENGTH * cos(radians(elbow_angle))) + shoulder_x
  elbow_y = (-1 * UPPER_ARM_LENGTH * sin(radians(elbow_angle))) + shoulder_y
    
def set_wrist_coord():
  global wrist_x, wrist_y
  wrist_x = (FOREARM_LENGTH * cos(radians(wrist_angle))) + elbow_x
  wrist_y = (-1 * FOREARM_LENGTH * sin(radians(wrist_angle))) + elbow_y


w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False


# Game loop
clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)  # Fill the screen with white color

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                # Set the "w_pressed" flag to True when "w" key is pressed
                w_pressed = True
            elif event.key == pygame.K_s:
                # Set the "s_pressed" flag to True when "s" key is pressed
                s_pressed = True
            elif event.key == pygame.K_UP:
                # Set the "up_pressed" flag to True when up arrow key is pressed
                up_pressed = True
            elif event.key == pygame.K_DOWN:
                # Set the "down_pressed" flag to True when down arrow key is pressed
                down_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                # Set the "w_pressed" flag to False when "w" key is released
                w_pressed = False
            elif event.key == pygame.K_s:
                # Set the "s_pressed" flag to False when "s" key is released
                s_pressed = False
            elif event.key == pygame.K_UP:
                # Set the "up_pressed" flag to False when up arrow key is released
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                # Set the "down_pressed" flag to False when down arrow key is released
                down_pressed = False

    # Update elbow_angle
    if w_pressed:
        elbow_angle += elbow_angle_speed
        print("Elbow Angle (Incremented):", elbow_angle)

    if s_pressed:
        elbow_angle -= elbow_angle_speed 
        print("Elbow Angle (Decremented):", elbow_angle)

    # Update wrist_angle
    if up_pressed:
        wrist_angle += wrist_angle_speed
        print("Wrist Angle (Incremented):", wrist_angle)

    if down_pressed:
        wrist_angle -= wrist_angle_speed
        print("Wrist Angle (Decremented):", wrist_angle)

    elbow_angle %= 360
    wrist_angle %= 360

    set_elbow_coord()
    set_wrist_coord()


    pygame.draw.line(screen, WHITE, (shoulder_x, shoulder_y), (elbow_x, elbow_y), 5)
    pygame.draw.line(screen, WHITE, (elbow_x, elbow_y), (wrist_x, wrist_y), 5)




    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

    clock.tick(60)
