# Display settings
import math


WIN_SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 60

# Lighning settings
PIXEL_SIZE = 3
LIGHT_WIDTH = math.ceil(WIDTH / PIXEL_SIZE)
LIGHT_HEIGHT = math.ceil(HEIGHT / PIXEL_SIZE)
# COLORS = ["black", "darkviolet", "purple", "white"]
COLORS = ["black", "darkorchid2", "darkorchid1", "darkorchid", "hotpink", "white"]
# COLORS = ["black", "chocolate4", "chocolate3", "chocolate2", "chocolate1", "white"]
MAX_SPLITS = 3
MAX_SIDEWAYS = 10
STEPS_BETWEEN_COLORS = 50
SPEED = 20
SPLIT_CHANCE = 0
SPLIT_CHANCE_INCREASE_RATE = HEIGHT//10
SPLIT_CHANCE_INCREASE_STEP = 0.5