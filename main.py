import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidField import AsteroidField
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()  
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
    player = Player(x=(SCREEN_WIDTH/2), y=(SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for item in updatable:
            item.update(dt)
        screen.fill((0, 0, 0))
        for item in drawable:
            item.draw(screen)     
        pygame.display.update()
        for item in asteroids:
            if player.check_collisions(item):
                print("Game Over!")
                sys.exit()
        
        dt = clock.tick(60) * 0.001 

if __name__ == "__main__":
    main()