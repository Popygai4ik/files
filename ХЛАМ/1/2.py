import pygame
import os
import sys

clock = pygame.time.Clock()
pygame.display.set_caption("Перемещение героя c выбором уровня")


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
screen_size = WIDTH, HEIGHT = (500, 500)
screen = pygame.display.set_mode(screen_size)
FPS = 50
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.abs_pos = (self.rect.x, self.rect.y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        camera.dx -= tile_width * (x - self.pos[0])
        camera.dy -= tile_height * (y - self.pos[1])
        self.pos = (x, y)
        for sprite in tiles_group:
            camera.apply(sprite)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x = obj.abs_pos[0] + self.dx
        obj.rect.y = obj.abs_pos[1] + self.dy

    def update(self, target):
        self.dx = 0
        self.dy = 0


# основной персонаж
player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Перемещение героя", "",
                  "Герой двигается",
                  "Камера двигается"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def move(hero, movement):
    x, y = hero.pos
    if movement == 'up':
        if y > 0 and (level_map[y - 1][x] == '.' or level_map[y - 1][x] == '@'):
            hero.move(x, y - 1)
    elif movement == 'down':
        if y < max_y - 1 and (level_map[y + 1][x] == '.' or level_map[y + 1][x] == '@'):
            hero.move(x, y + 1)
    elif movement == 'left':
        if x > 0 and (level_map[y][x - 1] == '.' or level_map[y][x - 1] == '@'):
            hero.move(x - 1, y)
    elif movement == 'right':
        if x < max_x - 1 and (level_map[y][x + 1] == '.' or level_map[y][x - 1] == '@'):
            hero.move(x + 1, y)


start_screen()
camera = Camera()
print('''Введите номер уровня
Номер 1 2 или 3''')
ans = int(input())
if ans == 1:
    filename = 'map.map'
    level_map = load_level(filename)
elif ans == 2:
    filename = 'close_zone.map'
    level_map = load_level(filename)
elif ans == 3:
    filename = 'free_zone.map'
    level_map = load_level(filename)
else:
    print('Wrong answer')
    sys.exit()
level_map = load_level(filename)
hero, max_x, max_y = generate_level(level_map)
running = True
camera.update(hero)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move(hero, 'up')
            elif event.key == pygame.K_DOWN:
                move(hero, 'down')
            elif event.key == pygame.K_LEFT:
                move(hero, 'left')
            elif event.key == pygame.K_RIGHT:
                move(hero, 'right')
    screen.fill(pygame.Color('black'))
    tiles_group.draw(screen)
    player_group.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()