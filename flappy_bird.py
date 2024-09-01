# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("The Snake Game")
#
# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()
# screen.listen()
# screen.onkey(fun=snake.up, key="Up")
# screen.onkey(fun=snake.down, key="Down")
# screen.onkey(fun=snake.left, key="Left")
# screen.onkey(fun=snake.right, key="Right")
#
# game_on = True
# while game_on:
#     screen.update()
#     time.sleep(0.005)
#     snake.move()
#     # Detect collision with food.
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.grow()
#         scoreboard.increase_score()
#     # Detect collision with wall.
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         scoreboard.reset()
#         snake.reset()
#     # Detect collision with tail.
#     for segment in snake.snake:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 10:
#             scoreboard.reset()
#             snake.reset()
#
# screen.exitonclick()

import pygame
import random
import sys

# Constants
WIDTH = 400
HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
BIRD_COLOR = (255, 255, 255)  
PIPE_COLOR = (0, 255, 0)
GRAVITY = 0.25
FLAP_FORCE = -5
PIPE_WIDTH = 70
GAP_SIZE = 200

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.radius = 15

    def flap(self):
        self.velocity = FLAP_FORCE

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, BIRD_COLOR, (self.x, int(self.y)), self.radius)

# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.gap_y = random.randint(50, HEIGHT - GAP_SIZE - 50)
        self.passed = False

    def move(self):
        self.x -= 2

    def off_screen(self):
        return self.x < -PIPE_WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, PIPE_WIDTH, self.gap_y))
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, self.gap_y + GAP_SIZE, PIPE_WIDTH, HEIGHT - self.gap_y - GAP_SIZE))

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()

    bird = Bird()
    pipes = []

    score = 0
    font = pygame.font.Font(None, 36)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        # Update bird
        bird.update()

        # Generate pipes
        if len(pipes) == 0 or pipes[-1].x < WIDTH - 150:
            pipes.append(Pipe())

        # Move pipes
        for pipe in pipes:
            pipe.move()

        # Remove off-screen pipes
        if pipes[0].off_screen():
            pipes.pop(0)

        # Check for collisions
        for pipe in pipes:
            if pipe.x < bird.x < pipe.x + PIPE_WIDTH:
                if bird.y < pipe.gap_y or bird.y > pipe.gap_y + GAP_SIZE:
                    print("Collision!")
                    pygame.quit()
                    sys.exit()
                elif not pipe.passed:
                    pipe.passed = True
                    score += 1

        # Draw everything
        screen.fill(BACKGROUND_COLOR)
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        # Display score
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

