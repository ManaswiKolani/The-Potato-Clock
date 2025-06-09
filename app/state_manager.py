from app.screens.menu import MenuScreen
from app.screens.timer import TimeScreen

class StateManager:
    def __init__(self, screen):
        self.screen = screen
        self.current_state = "menu"
        self.recipe = None
        self.states = {
            "menu": MenuScreen(screen, self.change_state),
        }
        
    def change_state(self, new_state, recipe=None):
        self.current_state = new_state
        self.recipe = recipe
        
        if new_state == "menu":
            self.states["menu"] = MenuScreen(self.screen, self.change_state)

        elif new_state == "timer" and recipe:
            self.states["timer"] = TimeScreen(self.screen, recipe, self.change_state)


    def handle_event(self, event):
        if self.current_state in self.states:
            self.states[self.current_state].handle_event(event)
            
    def draw(self):
        if self.current_state in self.states:
            self.states[self.current_state].draw()
        
    