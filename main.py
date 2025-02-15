# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatables, drawables) 
    AsteroidField.containers = (updatables)
    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
   
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #All black
        screen.fill((0, 0, 0))
        ###
        for updatable in updatables:
            updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        
        handle_shot_asteroids(shots, asteroids)

        # detect game over
        if is_game_over(player, asteroids):
            print("Game over!")
            sys.exit(0)

        # flip (empty)
        pygame.display.flip()
        dt_ms = clock.tick(60)
        dt = dt_ms / 1000

def is_game_over(player, asteroids):
    for asteroid in asteroids:
        if player.is_colliding(asteroid):
            return True
    return False

def handle_shot_asteroids(shots, asteroids):
    for asteroid in asteroids:
        for shot in shots:
            if shot.is_colliding(asteroid):
                shot.kill()
                asteroid.split()



if __name__ == "__main__":
    main()