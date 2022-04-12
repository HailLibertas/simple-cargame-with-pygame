from turtle import width
import pygame
from pygame.locals import *
import random

# Setting the window  size
size =  width, height = (800, 800)
road_width = width // 1.6
roadmark_width = width // 80
right_lane = width/2 +  road_width/4
left_lane = width/2 - road_width/4 
speed = 10

pygame.init()
running = True
screen = pygame.display.set_mode(size)

# Setting the title 
pygame.display.set_caption('Car Game with Pygame')
# Background color
screen.fill((60, 220, 0))

# Applying changes
pygame.display.update()

# Loading car images
car = pygame.image.load('car.png')
car_location = car.get_rect()
car_location.center = right_lane, height*0.8

# Loading competition vehicle
car2 = pygame.image.load('WhiteCar.png')
car2_location = car2.get_rect()
car2_location.center = left_lane, height*0.2

counter = 0
# Game loop
while running:
    counter += 1
    if counter == 1024:
        speed += 0.25
        counter = 0
        print('Level passed ', speed)
    # animate the competiton vehicle
    car2_location[1] += speed
    if car2_location[1] > height:
        if random.randint(0, 1) == 0:
            car2_location.center = right_lane, -200
        else:
            car2_location.center = left_lane, -200
        # Event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_location = car_location.move([-road_width//2, 0])
            if event.key in [K_d, K_RIGHT]:
                car_location = car_location.move([road_width//2, 0])
    # collison and ending the game
        # width of cars                         height of cars                edge detection
    if car_location[0] == car2_location[0] and car2_location[1] > car_location[1] - 250:
        print("GAME OVER...MUAHAHAHHAHAHAHAHAA")
        pygame.quit()

    
        # Drawing graphics
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_width/2, 0, road_width, height)
    )

    pygame.draw.rect(
        screen,
        (255, 240, 60), # Yellow line in the middle
        (width/2-roadmark_width/2, 0, roadmark_width, height)
    )
    # Adjusting the white marks at the edge of the road
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_width/2 + roadmark_width*2, 0, roadmark_width, height)
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_width/2 - roadmark_width*3, 0, roadmark_width, height)
    )

    screen.blit(car, car_location)
    screen.blit(car2, car2_location)
    pygame.display.update()

pygame.quit()    