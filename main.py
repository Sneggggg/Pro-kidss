import pygame

width = 400  # Окно игры
height = 500
Black = (150, 255, 234)

FPS = 30


class Player(pygame.sprite.Sprite):  # Игрок
    def __init__(self):  # Инициализация игрока
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((100, 50))  # Размер прямоуголника
        self.image.fill((255, 145, 3))  # Цвет прямоуголника
        self.rect = self.image.get_rect()  # Создание прямоуголника
        self.rect.center = (width / 2, height / 2)  # Центр прямоуголника

    def uppdate(self):
        self.rect.x += 5

        if self.rect.left > width:
            self.rect.right = 0


pygame.init()  # Запуск игры
pygame.mixer.init()  # Звук
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра Бога")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()  # Добовление спрайта в групу
player = Player()
all_sprites.add(player)

run = True
while run:

    clock.tick(FPS)  # Ограничения FPS

    for event in pygame.event.get():  # Выход на крестик
        if event.type == pygame.QUIT:
            run = False

    all_sprites.update()
    screen.fill(Black)  # Заливка
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
