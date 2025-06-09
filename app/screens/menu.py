import pygame
from app.constants import WIDTH, HEIGHT, RECIPES
from app.ui.button import Button
from app.ui.title_bar import TitleBar

class MenuScreen:
    def __init__(self, screen, change_state_callback):
        self.screen = screen
        self.change_state_callback = change_state_callback
        self.title_bar = TitleBar()
        pygame.font.init()
        self.font = pygame.font.SysFont("arialroundedmtbold", 24)


        self.buttons = []
        self.recipe_names = list(RECIPES.keys())

        button_size = 140
        scaled_images = []
        for recipe in self.recipe_names:
            img_path = f"assets/{recipe.lower().replace(' ', '_')}.PNG"
            original_img = pygame.image.load(img_path).convert_alpha()
            
            scaled_img = pygame.transform.scale(original_img, (button_size, button_size))
            scaled_images.append(scaled_img)

        total_button_width = len(scaled_images) * button_size
        gap = (WIDTH - total_button_width) // (len(scaled_images) + 1)
        y = HEIGHT // 2 + 40  

        for i, (recipe, img) in enumerate(zip(self.recipe_names, scaled_images)):
            x = gap + i * (button_size + gap)
            btn = Button(x, y, img, scale=1) 
            self.buttons.append({"button": btn, "label": recipe})
            
    def draw(self):
        self.screen.fill((234, 213, 163))
        self.title_bar.draw(self.screen)

        for entry in self.buttons:
            btn = entry["button"]
            recipe = entry["label"]

            btn.draw(self.screen)

            text_surface = self.font.render(recipe, True, (130, 73, 71))
            text_rect = text_surface.get_rect(
                center=(btn.rect.centerx, btn.rect.bottom + 20)
            )
            self.screen.blit(text_surface, text_rect)
            
            
    
    def handle_event(self, event):
        for entry in self.buttons:
            btn = entry["button"]
            recipe = entry["label"]
            if btn.is_clicked(event):
                self.change_state_callback("timer", recipe)

