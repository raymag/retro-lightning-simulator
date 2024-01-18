import pygame, sys
from pygame import gfxdraw
from random import randint, choice
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Lightning")
        self.screen = pygame.display.set_mode(WIN_SIZE)
        self.clock = pygame.time.Clock()

        self.roots = [(randint(0, LIGHT_WIDTH), 0)]
        self.rendering_lightning = True
        self.lightning_array = self.get_lightning_array()
        print(LIGHT_WIDTH, LIGHT_HEIGHT)

    def do_lightning(self):
        if self.rendering_lightning:
            for root in self.roots:
                # split chance
                rnd = randint(0, 10)
                if rnd > 7:
                    rnd = choice([-1, 1])
                    if rnd == -1 and root[0] - 1 > 0:
                        self.lightning_array[(root[0] - 1)][root[1]] = len(COLORS) - 1
                        self.roots.append((root[0] - 1, root[1]))
                    elif root[0] + 1 < LIGHT_WIDTH:
                        self.lightning_array[(root[0] + 1)][root[1]] = len(COLORS) - 1
                        self.roots.append((root[0] + rnd, root[1]))
                else:
                    if root[1] + 1 < LIGHT_HEIGHT:
                        print(root[1], "y")
                        self.lightning_array[root[0]][
                            (root[1] + 1) % LIGHT_HEIGHT - 1
                        ] = (len(COLORS) - 1)
                        self.roots.append((root[0], root[1] + 1))

                #     self.lightning_array[(root[0] + rnd) % LIGHT_WIDTH][root[1]] = (
                #         len(COLORS) - 1
                #     )

                self.roots.remove(root)
                if len(self.roots) == 0:
                    self.rendering_lightning = False

            # for x in range(LIGHT_WIDTH):
            #     for y in range(LIGHT_HEIGHT):
            #         if self.lightning_array[x][y] != 0:
            #             self.lightning_array[x][(y + 1) % LIGHT_HEIGHT] = (
            #                 self.lightning_array[x][y] - 1
            #             )
            #             print("creu")

    def draw_lightning(self):
        for x in range(LIGHT_WIDTH):
            for y in range(LIGHT_HEIGHT):
                gfxdraw.box(
                    self.screen,
                    (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE - 1, PIXEL_SIZE - 1),
                    pygame.Color(COLORS[self.lightning_array[x][y]]),
                )

    def get_lightning_array(self):
        lightning_array = [[0 for y in range(LIGHT_HEIGHT)] for x in range(LIGHT_WIDTH)]
        lightning_array[self.roots[0][0]][0] = len(COLORS) - 1

        return lightning_array

    def draw(self):
        self.draw_lightning()

    def update(self):
        self.do_lightning()
        pygame.display.set_caption(f"Lightning = {self.clock.get_fps():.1f}")

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
