import pygame

class TitleBar:
    def __init__(self):
        self.image = pygame.image.load("assets/title_icon.PNG").convert_alpha()
        self.image = pygame.transform.scale(self.image, (788,266))  

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
