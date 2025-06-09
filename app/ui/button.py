import pygame

class Button:
    def __init__(self, x, y, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.original_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            enlarged_width = self.original_image.get_width() + 6
            enlarged_height = self.original_image.get_height() + 6
            enlarged_image = pygame.transform.scale(self.original_image, (enlarged_width, enlarged_height))

            enlarged_rect = enlarged_image.get_rect(center=self.rect.center)
            screen.blit(enlarged_image, enlarged_rect.topleft)
        else:
            screen.blit(self.original_image, self.rect.topleft)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
