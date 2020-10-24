import pygame
import random

screen_size = (800, 600)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()


class Ball:
    def __init__(self):
        self.source = "basketball.png"
        self.delta_x_coordinate = random.randint(-3, 3)
        self.delta_y_coordinate = random.randint(-3, 3)
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)
        self.height = 100
        self.width = 100

    def frame(self, screen):
        image = pygame.image.load(self.source)
        rect = (self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
        screen.blit(image, rect)

        if self.x - self.width // 2 <= 0 or self.x + self.width // 2 >= 800:
            self.delta_x_coordinate = -self.delta_x_coordinate
        if self.y - self.height // 2 <= 0 or self.y + self.height // 2 >= 600:
            self.delta_y_coordinate = -self.delta_y_coordinate

        self.x += self.delta_x_coordinate
        self.y += self.delta_y_coordinate


class Platform:
    def __init__(self):
        self.x_left_top = 350
        self.y_left_top = 500
        self.height = 50
        self.width = 200
        self.color = (231, 127, 103)
        self.current_shift = 0

    def frame(self, screen):
        pygame.draw.rect(screen, self.color, (self.x_left_top, self.y_left_top, self.width, self.height))

    def move(self):
        if self.x_left_top > 0 and self.x_left_top + self.width < 800:
            self.x_left_top += self.current_shift
        if self.x_left_top == 0 and self.current_shift == 1:
            self.x_left_top += self.current_shift
        if self.x_left_top + self.width == 800 and self.current_shift == -1:
            self.x_left_top += self.current_shift

    def set_shift(self, shift):
        self.current_shift = shift


class Game:
    def __init__(self):
        self.color = BLACK
        self.screen_size = screen_size
        self.screen = None
        self.ball = Ball()
        self.platform = Platform()
        self.run_program = True

    def set_game(self):
        pygame.init()

        self.screen = pygame.display.set_mode(screen_size)
        self.screen.fill(BLACK)

        self.ball.frame(self.screen)
        self.platform.frame(self.screen)
        pygame.display.flip()

    def show_lose_screen(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, GREEN, [200, 150, 50, 50])
        kek = pygame.font.Font(None, 36)
        text = kek.render("Game Over", True, WHITE)
        text_rect = text.get_rect()
        text_x = self.screen.get_width() / 2 - text_rect.width / 2
        text_y = self.screen.get_height() / 2 - text_rect.height / 2
        self.screen.blit(text, [text_x, text_y])

        pygame.display.flip()

    def check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                run_program = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.platform.set_shift(-1)
                if event.key == pygame.K_d:
                    self.platform.set_shift(1)
            if event.type == pygame.KEYUP:
                self.platform.set_shift(0)
        if self.ball.y + self.ball.height//2 >= self.screen_size[1]:
            self.run_program = False

    def emulate_game(self):
        while self.run_program:
            self.check_events(pygame.event.get())
            self.frame()
        self.show_lose_screen()
        pygame.time.wait(100000)
        pygame.quit()

    def frame(self):
        self.screen.fill(self.color)
        self.ball.frame(self.screen)
        self.platform.move()
        self.platform.frame(self.screen)
        pygame.display.flip()
        pygame.time.wait(10)


def main():
    game = Game()
    game.set_game()
    game.emulate_game()


if __name__ == '__main__':
    main()
