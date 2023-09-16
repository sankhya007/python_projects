

import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PIPE_WIDTH = 50
PIPE_HEIGHT = 300
BIRD_RADIUS = 15
BIRD_JUMP = -7
GRAVITY = 0.5
PIPE_SPEED = 3

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def jump(self):
        self.velocity = BIRD_JUMP

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = PIPE_HEIGHT
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED

# Game function
def game():
    bird = Bird()
    pipes = []
    frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        # Update bird
        bird.update()

        # Update pipes
        if frame % 100 == 0:
            pipe = Pipe(SCREEN_WIDTH)
            pipes.append(pipe)

        for pipe in pipes:
            pipe.update()

        # Check collision
        for pipe in pipes:
            if pipe.x < bird.x < pipe.x + PIPE_WIDTH:
                if bird.y < pipe.height or bird.y > pipe.height + 150:
                    print("Game over!")
                    pygame.quit()
                    sys.exit()

            if pipe.x + PIPE_WIDTH < bird.x and not pipe.passed:
                pipe.passed = True

        pipes = [pipe for pipe in pipes if pipe.x > -PIPE_WIDTH]

        # Draw everything
        screen.fill(WHITE)

        for pipe in pipes:
            pygame.draw.rect(screen, BLUE, (pipe.x, 0, PIPE_WIDTH, pipe.height))
            pygame.draw.rect(screen, BLUE, (pipe.x, pipe.height + 150, PIPE_WIDTH, SCREEN_HEIGHT))

        pygame.draw.circle(screen, BLUE, (bird.x, int(bird.y)), BIRD_RADIUS)

        pygame.display.flip()
        frame += 1

        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    game()
