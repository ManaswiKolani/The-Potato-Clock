import pygame
import sys
from app.constants import  WIDTH, HEIGHT, FPS
from app.state_manager import StateManager

def main():
    pygame.init()
    
    #create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The Potato Clock 🍠")
    
    # Set custom window icon
    icon = pygame.image.load("assets/app_icon.PNG")
    pygame.display.set_icon(icon)
    
    #FPS clock
    clock = pygame.time.Clock()
    
    # State manager
    state_manager = StateManager(screen)
    
    # Main game loop
    running = True
    while running:
        clock.tick(FPS)
        
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # screen fill
        screen.fill((234, 213, 163))
        # Set background color
        state_manager.handle_event(event)
        
        # Draw rest here
        state_manager.draw()
        pygame.display.update()
        

    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()
