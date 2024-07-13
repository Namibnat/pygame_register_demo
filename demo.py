"""Register Demo"""

import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 1060
EDGE_GAP = 20
FPS = 6

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RAM_COLOUR = (25, 25, 25)
ALU_COLOR = (60, 60, 60)
TEXT_COLOR = (255, 128, 0)
RAM = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
)



class RegisterGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pygame Class-Based Template')
        self.clock = pygame.time.Clock()
        self.running = True
        self.event_handler = EventHandler(self)
        self.screen_title_font = pygame.font.SysFont('Arial', 30)
        self.code_font = pygame.font.SysFont('Arial', 12)

        self.ram_screen = None
        self.registers_screen = None
        self.alu_screen = None

    def draw_text(self, screen, text, font, text_color, x, y):
        img = font.render(text, True, text_color)
        screen.blit(img, (x, y))

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
        self.ram_block()
        self.registers_block()
        self.alu_block()
        self.fill_ram_block()
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

    def alu_block(self):
        alu_screen_height = (SCREEN_HEIGHT // 2) - EDGE_GAP
        alu_screen_top_offset = (SCREEN_HEIGHT // 2)
        alu_screen_left_offset = 900 + (2 * EDGE_GAP)
        alu_screen_width = (SCREEN_WIDTH - alu_screen_left_offset) - EDGE_GAP

        self.alu_screen = pygame.draw.rect(
            self.screen,
            ALU_COLOR,
            (alu_screen_left_offset, alu_screen_top_offset, alu_screen_width, alu_screen_height))

        self.draw_text(
            self.screen,
            "ALU",
            self.screen_title_font,
            TEXT_COLOR,
            alu_screen_left_offset + EDGE_GAP,
            alu_screen_top_offset + EDGE_GAP)

    def registers_block(self):
        reg_screen_height = (SCREEN_HEIGHT // 2) - (2 * EDGE_GAP)
        reg_screen_top_offset = EDGE_GAP
        reg_screen_left_offset = 900 + (2 * EDGE_GAP)
        reg_screen_width = (SCREEN_WIDTH - reg_screen_left_offset) - EDGE_GAP

        self.registers_screen = pygame.draw.rect(
            self.screen,
            BLACK,
            (reg_screen_left_offset, reg_screen_top_offset, reg_screen_width, reg_screen_height))

        self.draw_text(
            self.screen,
            "Registers",
            self.screen_title_font,
            TEXT_COLOR,
            reg_screen_left_offset + EDGE_GAP,
            reg_screen_top_offset + EDGE_GAP)

    def ram_block(self):
        ram_screen_top_offset = EDGE_GAP
        ram_screen_left_offset = EDGE_GAP
        ram_screen_height = SCREEN_HEIGHT - (2 * EDGE_GAP)
        ram_screen_width = 900

        self.ram_screen = pygame.draw.rect(
            self.screen,
            RAM_COLOUR,
            (ram_screen_left_offset, ram_screen_top_offset, ram_screen_width, ram_screen_height))

        self.draw_text(
            self.screen,
            "RAM",
            self.screen_title_font,
            TEXT_COLOR,
            (2 * EDGE_GAP),
            (2 * EDGE_GAP))

    def fill_ram_block(self):
        y = 4 * EDGE_GAP
        x = 0
        for i in range(0, (2**11) + 20):
            if i % 44 == 0:
                x = 0
                y += 20
            self.draw_text(
                self.screen,
                random.choice(('0', '1'),),
                self.code_font,
                TEXT_COLOR,
                (x * 20) + (2 * EDGE_GAP),
                y)
            x += 1



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

