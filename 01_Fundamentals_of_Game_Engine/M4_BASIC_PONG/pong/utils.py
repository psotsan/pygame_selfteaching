import random

def clamp (val, min_val, max_val):
    return max(min(val, max_val), min_val)

def ball_initial_direction():
    go_right = True if random.randint(0, 1) == 1 else False
    go_down = True if random.randint(0, 1) == 1 else False
    x_amount = clamp(random.random(), 0.2, 1)
    x_dir = x_amount if go_right else x_amount * -1
    y_dir = (1 - x_dir) if go_down else (1 - x_dir) * -1
    return x_dir, y_dir