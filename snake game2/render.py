import config
import pygame

class Render:
    def __init__(self, screen):
        self.screen = screen
        self.green = config.COLORS["green"]
        self.red = config.COLORS["red"]
        self.white = config.COLORS["white"]
        self.black = config.COLORS["black"]
        self.background_color = config.COLORS["navy"]
        self.font = pygame.font.Font(None, 24)

    def draw_background(self):
        self.screen.fill(self.background_color)

    def draw_snake(self, snake):
        for x, y in snake.snake_body:
            pygame.draw.rect(self.screen, self.green, [x, y, config.blok_size, config.blok_size])

    def draw_food(self, food):
        pygame.draw.rect(self.screen, self.red, [food.position[0], food.position[1], config.blok_size, config.blok_size])

    def draw_score(self, score):
        text = self.font.render("Score: " + str(score), True, self.white)
        self.screen.blit(text, (10, 10))

    def draw_gameover(self):
        text = self.font.render("Game Over", True, self.white)
        center_x = self.screen.get_width() // 2
        center_y = self.screen.get_height() // 2
        self.screen.blit(text, (center_x, center_y))
