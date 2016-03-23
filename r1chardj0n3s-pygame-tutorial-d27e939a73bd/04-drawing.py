import pygame

class Game(object):
    def main(self, screen):
        image = pygame.image.load('player.png')
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            screen.fill((200, 200, 200)) #clearing whatever is currently on the screen
            screen.blit(image, (320, 240)) #display the image. BLock Image Transfer.
            pygame.display.flip() #displays what was drawn to the buffer. Prevents tearing.

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Game().main(screen)

