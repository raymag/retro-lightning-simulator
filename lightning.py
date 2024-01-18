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
        self.flashing = False

    def new_lightning(self):
        pygame.draw.rect(self.game.screen, "black", self.game.screen.get_rect())
        root = random.randint(0, LIGHT_WIDTH-1),0
        self.roots = [root]
        self.game.sky[root[0]][root[1]] = len(COLORS)-1
        self.splits = 1
        self.went_sideways_count = 0
        self.flashing = False
        
        for x in range(LIGHT_WIDTH):
            for y in range(LIGHT_HEIGHT):
                self.game.sky[x][y] = 0

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

    def get_next_point(self, x, y, color):
        neighbors = self.check_neighbors(x,y)
        if len(neighbors) == 0:
            return None
        if self.went_sideways_count >= MAX_SIDEWAYS and "b" in neighbors:
            self.went_sideways_count = 0
            return (x, y+1)

        direction = random.choice(neighbors)
        neighbors.remove(direction)
        self.paint_neighbors(x,y,neighbors,color)
        if direction == "l":
            self.went_sideways_count+=1
            return (x-1, y)
        elif direction == "b":
            self.went_sideways_count = 0
            return (x, y+1)
        elif direction == "r":
            self.went_sideways_count+=1
            return (x+1, y)

    def paint_neighbors(self, x, y, neighbors, color):
        return
        for neighbor in neighbors:
            if neighbor == 'l':
                self.game.sky[x-1][y] = color
            elif neighbor == 'b':
                self.game.sky[x][y+1] = color
            elif neighbor == 'r':
                self.game.sky[x+1][y] = len(self.pallete)-1

    def draw(self):
        pass
        # if self.flashing:
        #     pygame.draw.rect(self.game.screen, 'white', (0,0, WIDTH, HEIGHT))
        #     pygame.time.delay(1000)
        #     # pygame.time.wait(100)
        #     pygame.draw.rect(self.game.screen, 'black', (0,0, WIDTH, HEIGHT))
        #     self.new_lightning()
            
                
    def update(self):         
        for i in range(SPEED):
            for root in self.roots:
                if root[1] == LIGHT_HEIGHT-1:
                    self.roots = []
                    self.new_lightning()
                    break

                # if self.splits > 1 and random.random() < 0.1:
                    
                # current_fps = self.game.clock.get_fps()

                old_color = self.game.sky[root[0]][root[1]]
                next_point = self.get_next_point(root[0], root[1], old_color)

                if next_point:
                    self.game.sky[next_point[0]][next_point[1]] = old_color-1 if old_color-1>0 else len(self.pallete)-1
                    self.roots.append(next_point)
                    if len(self.roots) < MAX_SPLITS and random.random() <= 0.01 + (SPLIT_CHANCE_INCREASE_STEP * (next_point[1]//SPLIT_CHANCE_INCREASE_RATE)) :
                        pass
                    else:
                        self.roots.remove(root)
                else:
                    next_point = (root[0], root[1]+1)
                    self.roots.append(next_point)
                    self.roots.remove(root)
                    self.game.sky[next_point[0]][next_point[1]] = old_color-1 if old_color-1>0 else len(self.pallete)-1

                # print(self.roots, next_point)
                if len(self.roots) > 1 and random.random() <= 0.025:
                    self.roots.pop()
            
                # print(next_point)

                
                splits = len(self.roots)
                # print(splits)




                # if (random.random()*current_fps < 1 * current_fps) and splits > 1:
                #     self.roots.remove(root)
                #     splits -= 1
                # else:      
                #     if next_point:
                #         self.game.sky[next_point[0]][next_point[1]] = old_color-1 if old_color-1>0 else len(self.pallete)-1
                #         self.roots.append(next_point)
                        # splits += 1
                        # self.splits += 1

                        # if random.randint(0,100*round(current_fps)) <= split_threshold*current_fps and self.splits < MAX_SPLITS:
                        #     self.splits += 1
                        # if (random.random()*current_fps) < 0.2 and self.splits < MAX_SPLITS:
                        #     splits += 1
                        # elif self.splits > 1:
                        #     self.roots.remove(root)
                        #     splits -= 1  
                            # self.splits -= 1
