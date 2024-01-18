import pygame, random, math
from settings import *

class Lightning:
    def __init__(self,game):
        self.game = game
        root = random.randint(0, LIGHT_WIDTH-1),0
        self.roots = [root]
        self.game.sky[root[0]][root[1]] = len(COLORS)-1
        self.splits = 1
        self.went_sideways_count = 0
        self.pallete = self.get_pallete()

    @staticmethod
    def get_pallete():
        pallete = [(0, 0, 0)]
        for i, color in enumerate(COLORS[:-1]):
            c1, c2 = color, COLORS[i + 1]
            for step in range(STEPS_BETWEEN_COLORS):
                c = pygame.Color(c1).lerp(c2, (step + 0.5) / STEPS_BETWEEN_COLORS)
                pallete.append(c)
        return pallete
    
    def check_neighbors(self, x,y):
        availability = [] 
        if x+1 < LIGHT_WIDTH-1:
            if self.game.sky[x+1][y] == 0:
                availability.append("r")
        if x-1 >= 0:
            if self.game.sky[x-1][y] == 0:
                availability.append("l")
        if y+1 < LIGHT_HEIGHT:
            if self.game.sky[x][y+1] == 0:
                availability.append("b")
        return availability

    def get_next_point(self, x, y):
        neighbors = self.check_neighbors(x,y)
        if len(neighbors) == 0:
            return None
        if self.went_sideways_count >= MAX_SIDEWAYS and "b" in neighbors:
            self.went_sideways_count = 0
            return (x, y+1)

        direction = random.choice(neighbors)
        if direction == "l":
            self.went_sideways_count+=1
            return (x-1, y)
        elif direction == "b":
            self.went_sideways_count = 0
            return (x, y+1)
        elif direction == "r":
            self.went_sideways_count+=1
            return (x+1, y)


    def draw(self):
        pass

                
    def update(self):
        for root in self.roots:
            if root[1] == LIGHT_HEIGHT-1:
                self.roots = []
                break
            next_point = self.get_next_point(root[0], root[1])
            if next_point:
                old_color = self.game.sky[root[0]][root[1]]
                self.game.sky[next_point[0]][next_point[1]] = old_color-1 if old_color-1>0 else len(self.pallete)-1
                self.roots.append(next_point)
                if random.random() > 0.9 and self.splits < MAX_SPLITS:
                    self.splits += 1
                else:
                    self.roots.remove(root)
