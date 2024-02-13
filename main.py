import pygame
import sys
from math import sin, cos, pi, radians;


RECORDING = False 
REPLAY = True
FILE_PATH = 'output.txt'

if RECORDING:
    f = open(FILE_PATH, 'w')
    f.write('Elbow Angle, Wrist Angle\n')
if REPLAY:
    f = open(FILE_PATH, 'r')
    print(f.readline().strip()) # remove the title of columns





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
exit_simulation = False
while True:
    screen.fill(BLACK)  # Fill the screen with white color

    # start recording 
    if RECORDING:
        f.write(f'{elbow_angle},{wrist_angle}\n')
    elif REPLAY:
        line = f.readline()
        if line:
            angles = line.strip().split(",")
            elbow_angle = int(angles[0])
            wrist_angle = int(angles[1])
        else:
            exit_simulation = True
        

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or exit_simulation:
            f.close()
            pygame.quit()
            sys.exit()

        if RECORDING: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_pressed = True
                elif event.key == pygame.K_s:
                    s_pressed = True
                elif event.key == pygame.K_UP:
                    up_pressed = True
                elif event.key == pygame.K_DOWN:
                    down_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    w_pressed = False
                elif event.key == pygame.K_s:
                    s_pressed = False
                elif event.key == pygame.K_UP:
                    up_pressed = False
                elif event.key == pygame.K_DOWN:
                    down_pressed = False

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
