import pygame
from constants import *
from player import *
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=(SCREEN_WIDTH/2), y=(SCREEN_HEIGHT/2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)     
        pygame.display.update()
        dt = clock.tick(60) * 0.001 


if __name__ == "__main__":
    main()