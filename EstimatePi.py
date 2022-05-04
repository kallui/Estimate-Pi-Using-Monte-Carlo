# Estimating Pi using Monte Carlo Simulation
# By Nicholas Januar - https://github.com/kallui

import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Estimate Pi using Monte Carlo simulation')

# Global variables for Pi Estimation
global circle_points, pi_estimation
points = []
circle_points = 0
pi_estimation = 0

# Simulation rectangle
sim_rect = pygame.Rect(20, 20, 300, 300)
sim_color = pygame.Color('black')

# Estimation texts
formula_text = 'Estimation of Pi = 4 * (circle_points/square_points)'
circle_points_text = 'Circle points = '
circle_points_number = '0'
estimation_text = 'Estimation of Pi = '
estimation_number = '0'

# Input text box
input_rect = pygame.Rect(340, 200, 140, 35)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
text_color = color_passive

base_font = pygame.font.Font(None, 28)
points_text = 'Number of points:'
user_text = '0'
input_number = 0
active = False

# Run button
run_rect = pygame.Rect(340, 240, 50, 30)
run_color = pygame.Color('azure4')
run_text = 'Run'

# Clear button
clear_rect = pygame.Rect(400, 240, 60, 30)
clear_color = pygame.Color('azure4')
clear_text = 'Clear'

sim_running = False

# Run simulation by appending random generated points into the points array and returns the number of points inside circle


def runSimulation(input_number):
    circle_points = 0
    points.clear()
    for i in range(input_number):
        x = random.randint(1, 300) + 20
        y = random.randint(1, 300) + 20
        points.append((x, y))
        if (((x-170)*(x-170) + (y-170)*(y-170)) <= 150*150):
            circle_points = circle_points + 1
    return circle_points


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True

            elif run_rect.collidepoint(event.pos):
                input_number = int(user_text)
                if input_number > 0:
                    circle_points = runSimulation(input_number)
                    sim_running = True
                    circle_points_number = str(circle_points)
                    estimation_number = str(4*(circle_points/input_number))

            elif clear_rect.collidepoint(event.pos):
                sim_running = False
                user_text = '0'
                circle_points_number = '0'
                estimation_number = '0'
                circle_points = 0
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]

                elif event.key == pygame.K_RETURN:
                    input_number = int(user_text)
                    circle_points = runSimulation(input_number)
                    sim_running = True
                    circle_points_number = str(circle_points)
                    estimation_number = str(4*(circle_points/input_number))

                else:
                    if event.unicode.isdigit():
                        if user_text == '0':
                            user_text = ''
                        user_text += event.unicode

    screen.fill((255, 255, 255))

    if active:
        text_color = color_active
    else:
        text_color = color_passive

    text_surface1 = base_font.render(points_text, True, (0, 0, 0))
    screen.blit(text_surface1, (340, 170))

    # Draw rectangle and circle for the simulation
    pygame.draw.rect(screen, sim_color, sim_rect, 2)
    pygame.draw.circle(screen, sim_color, (170, 170), (150), 2)

    # Estimate part
    text_surface4 = base_font.render(formula_text, True, (0, 0, 0))
    screen.blit(text_surface4, (340, 20))

    text_surface5 = base_font.render(circle_points_text, True, (0, 0, 0))
    screen.blit(text_surface5, (340, 50))

    text_surface6 = base_font.render(circle_points_number, True, (0, 0, 0))
    screen.blit(text_surface6, (490, 50))

    text_surface7 = base_font.render(estimation_text, True, (0, 0, 0))
    screen.blit(text_surface7, (340, 80))

    text_surface8 = base_font.render(estimation_number, True, (0, 0, 0))
    screen.blit(text_surface8, (520, 80))

    # Draw rectangle and text input for number of points
    pygame.draw.rect(screen, text_color, input_rect, 2)
    text_surface2 = base_font.render(user_text, True, (0, 0, 0))
    screen.blit(text_surface2, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(100, text_surface2.get_width() + 10)

    # For visual purposes
    if user_text == '':
        user_text = '0'

    # Draw run button
    pygame.draw.rect(screen, run_color, run_rect)
    text_surface3 = base_font.render(run_text, True, (0, 0, 0))
    screen.blit(text_surface3, (run_rect.x + 5, run_rect.y + 5))

    # Draw clear button
    pygame.draw.rect(screen, clear_color, clear_rect)
    text_surface4 = base_font.render(clear_text, True, (0, 0, 0))
    screen.blit(text_surface4, (clear_rect.x + 5, clear_rect.y + 5))

    # If simulation is running, draw the points
    if sim_running == True:
        for p in points:
            pygame.draw.circle(screen, pygame.Color('firebrick1'), p, 2)

    pygame.display.flip()
    clock.tick(60)
