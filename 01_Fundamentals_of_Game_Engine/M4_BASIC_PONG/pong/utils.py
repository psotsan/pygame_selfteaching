import random
from entities import Ball
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BALL_RADIUS, WHITE

def clamp (val, min_val, max_val):
    return max(min(val, max_val), min_val)

def ball_initial_direction():
    go_right = True if random.randint(0, 1) == 1 else False
    go_down = True if random.randint(0, 1) == 1 else False
    x_amount = clamp(random.random(), 0.4, 1)
    x_dir = x_amount if go_right else -x_amount
    y_dir = (1 - abs(x_dir)) if go_down else (1 - abs(x_dir)) * -1
    return x_dir, y_dir


def score(scores:dict, player:int):
    scores[player] += 1
    print(scores)