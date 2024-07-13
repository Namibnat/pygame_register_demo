"""Register Demo"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 1060
EDGE_GAP = 20
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class RegisterGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pygame Class-Based Template')
        self.clock = pygame.time.Clock()
        self.running = True
        self.event_handler = EventHandler(self)

    def run(self):
        while self.running:
            self.event_handler.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        self.quit()

    def update(self):
        # Update game objects
        pass

    def draw(self):
        self.screen.fill(WHITE)
        # Draw game objects
        self.ram_block()
        self.registers_block()
        self.alu_block()
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

    def alu_block(self):
        alu_screen_width = EDGE_GAP
        alu_screen_height = EDGE_GAP
        alu_screen_top_offset = SCREEN_HEIGHT - alu_screen_height - EDGE_GAP
        alu_screen_left_offset = SCREEN_WIDTH - alu_screen_width - EDGE_GAP
        pygame.draw.rect(
            self.screen,
            BLACK,
            (alu_screen_left_offset, alu_screen_top_offset, alu_screen_width, alu_screen_height))

    def registers_block(self):
        reg_screen_width = EDGE_GAP
        reg_screen_height = EDGE_GAP
        reg_screen_top_offset = EDGE_GAP
        reg_screen_left_offset = SCREEN_WIDTH - reg_screen_width - EDGE_GAP
        pygame.draw.rect(
            self.screen,
            BLACK,
            (reg_screen_left_offset, reg_screen_top_offset, reg_screen_width, reg_screen_height))


    def ram_block(self):
        ram_screen_top_offset = EDGE_GAP
        ram_screen_left_offset = EDGE_GAP
        ram_screen_width = 900
        ram_screen_height = SCREEN_HEIGHT - 40
        pygame.draw.rect(
            self.screen,
            BLACK,
            (ram_screen_left_offset, ram_screen_top_offset, ram_screen_width, ram_screen_height))



class EventHandler:
    def __init__(self, game):
        self.game = game

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.running = False
                # Add other key event handlers here
            # Add other event types here


def main():
    game = RegisterGame()
    game.run()


if __name__ == '__main__':
    main()

