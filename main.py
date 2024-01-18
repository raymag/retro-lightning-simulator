import random
import pygame, sys
from pygame import gfxdraw
from lightning import Lightning
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Lightning")
        self.screen = pygame.display.set_mode(WIN_SIZE)
        self.clock = pygame.time.Clock()

        self.rendering_lightning = True
        self.sky = self.get_sky_map()
        self.lightning = Lightning(self)

    def get_sky_map(self):
        sky = [[0 for y in range(LIGHT_HEIGHT)] for x in range(LIGHT_WIDTH)]

        return sky

    def shuffle(self, i):
        if random.random() > 0.75:
            return random.randint(1, len(self.lightning.pallete) - 1)
        return i

    def draw_sky(self):
        for x in range(LIGHT_WIDTH - 1):
            for y in range(LIGHT_HEIGHT - 1):
                if self.sky[x][y]:
                    gfxdraw.box(
                        self.screen,
                        (
                            x * PIXEL_SIZE,
                            y * PIXEL_SIZE,
                            PIXEL_SIZE,
                            PIXEL_SIZE,
                        ),
                        pygame.Color(
                            self.lightning.pallete[self.shuffle(self.sky[x][y])]
                        ),
                    )
                    
                    # gfxdraw.box(
                    #     self.screen,
                    #     (
                    #         x * PIXEL_SIZE+4,
                    #         y * PIXEL_SIZE,
                    #         PIXEL_SIZE,
                    #         PIXEL_SIZE,
                    #     ),
                    #     pygame.Color(
                    #         self.lightning.pallete[self.shuffle(self.sky[x][y])]
                    #     ),
                    # )

                    gfxdraw.box(
                        self.screen,
                        (
                            (x * PIXEL_SIZE)+2,
                            y * PIXEL_SIZE,
                            PIXEL_SIZE-4,
                            PIXEL_SIZE-4,
                        ),
                        pygame.Color(
                            self.lightning.pallete[self.shuffle(len(self.lightning.pallete)-1)]
                        ),
                    )

    def draw(self):
        self.draw_sky()
        self.lightning.draw()

    def update(self):
        pygame.display.set_caption(f"Lightning = {self.clock.get_fps():.1f}")

        self.lightning.update()

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.update()
            self.draw()

            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
