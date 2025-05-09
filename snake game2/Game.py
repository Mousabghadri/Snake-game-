import pygame
import config
from snake import Snake
from food import Food
from render import Render

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.width = config.width
        self.height = config.height
        self.speed = config.speed
        self.block_size = config.blok_size
        self.score = 0
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.snake = Snake(self.block_size, self.width // 2, self.height // 2)
        self.food = Food(self.block_size, self.width, self.height, self.snake.snake_body)
        self.render = Render(self.screen)
        self.running = True

    def run(self):
        while self.running:
            self.handle_event()
            self.render.draw_background()
            self.snake.move()

            if self.did_eat():
                self.score += 1
                self.food.position = self.food.creat_food(
                    self.block_size, self.width, self.height, self.snake.snake_body
                )
            else:
                self.snake.remove()

            if self.did_collide():
                self.running = False

            self.render.draw_snake(self.snake)
            self.render.draw_food(self.food)
            self.render.draw_score(self.score)

            if not self.running:
                self.render.draw_gameover()
                pygame.display.flip()
                pygame.time.wait(2000)

            pygame.display.flip()
            self.clock.tick(self.speed)

        pygame.quit()

    def did_eat(self):
        return self.snake.head == self.food.position

    def did_collide(self):
        return (
            self.snake.head[0] < 0 or
            self.snake.head[0] >= self.width or
            self.snake.head[1] < 0 or
            self.snake.head[1] >= self.height or
            self.snake.head in self.snake.snake_body[1:]
        )

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_keypress(event.key)

    def handle_keypress(self, key):
        if key == pygame.K_UP and self.snake.direction != "down":
            self.snake.direction = "up"
        elif key == pygame.K_DOWN and self.snake.direction != "up":
            self.snake.direction = "down"
        elif key == pygame.K_LEFT and self.snake.direction != "right":
            self.snake.direction = "left"
        elif key == pygame.K_RIGHT and self.snake.direction != "left":
            self.snake.direction = "right"
