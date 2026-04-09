import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

RED = (255, 0, 0)
BLUE = (20, 20, 80)
WHITE = (255, 255, 255)

FONT = pygame.font.SysFont("monospace", 24)

clock = pygame.time.Clock()
color = BLUE
frames = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FPS")

running = True

screen.fill(BLUE)
pygame.display.flip()

# Main loop
while running:
    # Clock
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    running = False
                case pygame.K_f:
                    color = RED
                    pygame.display.set_caption("FPS - Red bg")
                case pygame.K_n:
                    color = BLUE
                    pygame.display.set_caption("FPS - Blue bg")
    # Status
    fps = clock.get_fps()
    frames += fps

    # Render
    screen.fill(color)
    fps_text = FONT.render(f"fps: {str(fps)}", True, WHITE)
    screen.blit(fps_text, (10, 10))
    frames_text = FONT.render(f"total frames: {str(frames)}", True, WHITE)
    screen.blit(frames_text, (10, 50))
    pygame.display.flip()

pygame.quit()
sys.exit()