import pygame
from app.ui.title_bar import TitleBar
from app.ui.button import Button
from app.constants import WIDTH, HEIGHT, RECIPES

class TimeScreen():
    def __init__(self, screen, recipe_name, change_state_callback):
        self.screen = screen
        self.recipe_name = recipe_name
        self.change_state_callback = change_state_callback
        self.title_bar = TitleBar()
        # Sound
        pygame.mixer.init()
        self.ding_sound = pygame.mixer.Sound("assets/ding.wav")
        self.has_played = False
        # Font
        pygame.font.init()
        self.font_small = pygame.font.SysFont("arialroundedmtbold", 30)
        self.font_timer = pygame.font.SysFont("arialroundedmtbold", 150)
        # Recipe Info
        self.recipe_info = RECIPES[recipe_name]
        self.time_seconds = self.recipe_info["time"]
        self.temperature = self.recipe_info["temp"]
        self.method = self.recipe_info["method"]

        # Buttons
        self.start_img = pygame.image.load("assets/start_button.PNG")
        self.menu_img = pygame.image.load("assets/menu_button.png")

        self.start_button = Button(WIDTH // 2 - 90, HEIGHT - 140, self.start_img, scale=1.5)
        self.menu_button = Button(WIDTH // 2 - 70, HEIGHT - 80, self.menu_img, scale=1)

        self.timer_started = False
        self.start_ticks = 0

    def draw_text_center(self, text, y, font, color=(130, 73, 71)):
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=(WIDTH // 2, y))
        self.screen.blit(surface, rect)

    def draw(self):
        self.screen.fill((255, 243, 207))
        self.title_bar.draw(self.screen)

        # Draw info panel background
        panel_rect = pygame.Rect(200, 230, WIDTH - 400, 130)
        pygame.draw.rect(self.screen, (255, 230, 180), panel_rect, border_radius=15)

        # Draw compact text block in panel
        self.draw_text_center(self.recipe_name, 250, self.font_small)
        self.draw_text_center(f"Method: {self.method}", 270, self.font_small)
        self.draw_text_center(f"Temperature: {self.temperature}", 290, self.font_small)
        if self.method == "Oven":
            self.draw_text_center("Make sure to preheat your oven!", 310, self.font_small)
        self.draw_text_center(f"Total Time: {self.time_seconds / 60} Minutes", 330, self.font_small)
        # Timer display
        if self.timer_started:
            elapsed = (pygame.time.get_ticks() - self.start_ticks) // 1000
            remaining = max(self.time_seconds - elapsed, 0)
            minutes = remaining // 60
            seconds = remaining % 60
            time_str = f"{minutes:02}:{seconds:02}"

            if remaining == 0:
                flash = (pygame.time.get_ticks() // 500) % 2 == 0
                timer_color = (179, 61, 57) if flash else (255, 243, 207)
            else:
                timer_color = (75, 113, 94)

            self.draw_text_center(time_str, 420, self.font_timer, timer_color)
        else:
            self.draw_text_center("--:--", 420, self.font_timer)

        # Draw buttons
        self.start_button.draw(self.screen)
        self.menu_button.draw(self.screen)
        
        # Sound
        elapsed = (pygame.time.get_ticks() - self.start_ticks) // 1000
        remaining = max(self.time_seconds - elapsed, 0)
        if self.timer_started and remaining == 0 and not self.has_played_ding:
            self.ding_sound.play()
            self.has_played_ding = True


    def handle_event(self, event):
        if self.menu_button.is_clicked(event):
            self.timer_started = False
            self.has_played_ding = False 
            self.change_state_callback("menu")
        if self.start_button.is_clicked(event) and not self.timer_started:
            self.timer_started = True
            self.start_ticks = pygame.time.get_ticks()
            self.has_played_ding = False  

