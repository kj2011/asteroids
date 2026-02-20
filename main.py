import pygame
from player import Player
from constants import *
from logger import log_state
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    player = Player((SCREEN_WIDTH //2), (SCREEN_HEIGHT //2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        #player.update(dt)
        updatable.update(dt)
        #player.draw(screen)
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()

        #Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        #Log after the frame is rendered
        log_state()

if __name__ == "__main__":
    main()
