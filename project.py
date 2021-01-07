import pygame
import os
import sys
import random

pygame.init()
SIZE = WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode(SIZE)
STEP = 50
SPRITES = pygame.sprite.Group()

tiles_group = pygame.sprite.Group()
tiles_obstacles = pygame.sprite.Group()
player_group = pygame.sprite.Group()
people_group = pygame.sprite.Group()
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
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


def size_image(name, size=None):
    if size is None:
        image = pygame.transform.scale(load_image(name), (50, 50))
    elif size == 1:
        image = pygame.transform.scale(load_image(name), (100, 100))
    elif size == 2:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (50, 100))
        image = pygame.transform.rotate(image, 90)
        image = pygame.transform.rotate(image, 180)
    elif size == 3:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (50, 50))
    return image


def load_level(filename):
    filename = "levels/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def start_game():
    image = pygame.transform.scale(load_image("screen_game.JPG"),
                                   (WIDTH, HEIGHT))
    SCREEN.blit(image, (0, 0))
    pygame.draw.rect(SCREEN, (255, 0, 0), (250, 530, 100, 50))
    font = pygame.font.Font(None, 50)
    text = font.render("PLAY", True, (0, 255, 127))
    SCREEN.blit(text, (255, 540))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 250 <= event.pos[0] <= 350 and 530 <= event.pos[1] <= 580:
                    main_menu()
                    return
        pygame.display.flip()


def main_menu():
    image_menu = pygame.transform.scale(load_image("Menu_game.jpg"),
                                        (WIDTH, HEIGHT))
    SCREEN.blit(image_menu, (0, 0))
    font = pygame.font.Font(None, 70)
    font2 = pygame.font.Font(None, 50)
    text = font.render("Game menu", True, (0, 0, 255))
    text_x = WIDTH // 2 - text.get_width() // 2
    pygame.draw.rect(SCREEN, (255, 255, 255), (text_x - 10, 15, 300, 50))
    SCREEN.blit(text, (text_x, 20))
    pygame.draw.rect(SCREEN, (255, 255, 50), (200, 100, 200, 50))
    text2 = font2.render("Rules", True, (153, 0, 255))
    text2_x = WIDTH // 2 - text2.get_width() // 2
    SCREEN.blit(text2, (text2_x, 110))
    pygame.draw.rect(SCREEN, (255, 255, 50), (200, 200, 200, 50))
    text3 = font2.render("Start", True, (153, 0, 255))
    text3_x = WIDTH // 2 - text3.get_width() // 2
    SCREEN.blit(text3, (text3_x, 210))
    pygame.draw.rect(SCREEN, (255, 255, 50), (200, 300, 200, 50))
    text4 = font2.render("Exit", True, (153, 0, 255))
    text4_x = WIDTH // 2 - text4.get_width() // 2
    SCREEN.blit(text4, (text4_x, 310))
    pygame.draw.rect(SCREEN, (255, 255, 50), (200, 400, 200, 50))
    text5 = font2.render("Developers", True, (153, 0, 255))
    text5_x = WIDTH // 2 - text5.get_width() // 2
    SCREEN.blit(text5, (text5_x, 410))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= event.pos[0] <= 400 and 100 <= event.pos[1] <= 150:
                    rules_game()
                    return
                if 200 <= event.pos[0] <= 400 and 300 <= event.pos[1] <= 350:
                    terminate()
                    return
                if 200 <= event.pos[0] <= 400 and 200 <= event.pos[1] <= 250:
                    choose_car()
                    return
        pygame.display.flip()


def rules_game():
    image = pygame.transform.scale(load_image("rules.jpg"), (WIDTH, HEIGHT))
    SCREEN.blit(image, (0, 0))
    font = pygame.font.Font(None, 40)
    text = font.render("Close", True, (0, 0, 255))
    pygame.draw.rect(SCREEN, (255, 255, 50), (500, 540, 90, 50))
    SCREEN.blit(text, (505, 555))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= event.pos[0] <= 590 and 540 <= event.pos[1] <= 590:
                    main_menu()
                    return
        pygame.display.flip()


car = 0


def choose_car():
    global car
    image = pygame.transform.scale(load_image("choose_car.jpg"),
                                   (WIDTH, HEIGHT))
    SCREEN.blit(image, (0, 0))
    font = pygame.font.Font(None, 40)
    text = font.render("Choose car", True, (0, 0, 0))
    text_x = WIDTH // 2 - text.get_width() // 2
    SCREEN.blit(text, (text_x, 20))
    image_car1 = pygame.transform.scale(load_image("car1.png"), (300, 100))
    SCREEN.blit(image_car1, (150, 70))
    image_car2 = pygame.transform.scale(load_image("car2.png"), (320, 180))
    SCREEN.blit(image_car2, (150, 190))
    image_car3 = pygame.transform.scale(load_image("car3.png"), (300, 180))
    SCREEN.blit(image_car3, (150, 370))
    text1 = font.render("1", True, (0, 0, 255))
    text2 = font.render("2", True, (0, 0, 0))
    text3 = font.render("3", True, (255, 0, 0))
    SCREEN.blit(text1, (299, 190))
    SCREEN.blit(text2, (299, 360))
    SCREEN.blit(text3, (299, 550))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    car = 1
                    play_game()
                    return
                elif event.key == pygame.K_2:
                    car = 2
                    play_game()
                    return
                elif event.key == pygame.K_3:
                    car = 3
                    play_game()
                    return
        pygame.display.flip()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, SPRITES)
        self.image = dict_tiles[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class Obstacles(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_obstacles, SPRITES)
        self.image = dict_obstacles[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__(player_group, SPRITES)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Man(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        super().__init__(people_group, SPRITES)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Shell():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 20

    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN, self.color, (self.x, self.y), self.radius)


class Camera:
    def __init__(self, size):
        self.dx = 0
        self.dy = 0
        self.field_size = size

    def apply(self, obj):
        obj.rect.x += self.dx
        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.field_size[0] + 1) * obj.rect.width
        if obj.rect.x >= self.field_size[0] * obj.rect.width:
            obj.rect.x -= (self.field_size[0] + 1) * obj.rect.width

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 3)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


def play_game():
    player, level_x, level_y, man = generate_level(load_level('level1.txt'))
    camera = Camera((level_x, level_y))
    start_grass = 0
    bombs = []
    run = True
    run2 = False
    while run:
        clock.tick(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        man.rect.y += STEP
        if pygame.sprite.groupcollide(player_group, people_group, False, True):
            run2 = True
            run = False
        tiles_group.draw(SCREEN)
        tiles_obstacles.draw(SCREEN)
        player_group.draw(SCREEN)
        people_group.draw(SCREEN)
        pygame.display.flip()
    while run2:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        player.rect.x += STEP
        for bomb in bombs:
            if bomb.x < 600:
                bomb.x += bomb.speed
            else:
                bombs.pop(bombs.index(bomb))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if len(bombs) < 3:
                bombs.append(Shell(player.rect.x + 40,
                                   player.rect.y + 25, 8, (random.randrange(0, 255),
                                                           random.randrange(0, 255),
                                                           random.randrange(0, 255))))
        if keys[pygame.K_UP] and start_grass < 2:
            start_grass += 1
            player.rect.y -= STEP
        if keys[pygame.K_DOWN] and start_grass > -2:
            start_grass -= 1
            player.rect.y += STEP
        camera.update(player)
        for sprite in SPRITES:
            camera.apply(sprite)
        tiles_group.draw(SCREEN)
        tiles_obstacles.draw(SCREEN)
        player_group.draw(SCREEN)
        people_group.draw(SCREEN)
        for bomb in bombs:
            bomb.draw(SCREEN)
        if pygame.sprite.groupcollide(player_group, tiles_obstacles, False, False):
            run2 = False
            player_group.empty()
            tiles_obstacles.empty()
            tiles_group.empty()
        pygame.display.flip()
    game_over()


def game_over():
    image = pygame.transform.scale(load_image("game_over.jpg"),
                                   (400, 400))
    SCREEN.blit(image, (100, 100))
    font = pygame.font.Font(None, 40)
    text = font.render("restart", True, (255, 51, 0))
    pygame.draw.rect(SCREEN, (0, 255, 204), (120, 440, 120, 40))
    SCREEN.blit(text, (135, 448))
    text2 = font.render("menu", True, (255, 51, 0))
    pygame.draw.rect(SCREEN, (0, 255, 204), (360, 440, 120, 40))
    SCREEN.blit(text2, (380, 448))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 360 <= event.pos[0] <= 480 and 440 <= event.pos[1] <= 480:
                    main_menu()
                    return
                if 120 <= event.pos[0] <= 240 and 440 <= event.pos[1] <= 480:
                    restart()
                    return
        pygame.display.flip()


def restart():
    play_game()


def generate_level(level):
    global car
    if car == 1:
        image = size_image('blue_car.PNG', size=2)
    elif car == 2:
        image = size_image('white_car.PNG', size=2)
    elif car == 3:
        image = size_image('red_car.PNG', size=2)
    new_player, x, y, man = None, None, None, None
    dict_symbols = {'.': 'road', 'f': 'fountain', 'R': 'red_car',
                    'W': 'white_car', 'B': 'blue_car', '1': 'home1',
                    '2': 'home2', '3': 'home3', '4': 'home4',
                    '5': 'home5', '6': 'home6', '7': 'home7',
                    '8': 'home8', '9': 'home9', '0': 'home10',
                    'e': 'home11', 't': 'home12', 'g': 'grass',
                    '*': 'grass2', 's': 'stump', 'w': 'water',
                    'd': 'wood', 'r': 'rock', '-': 'flower1',
                    '+': 'flower2', '#': 'finish'}
    obstacles = {'&': 'stones', '%': 'stones2', '!': 'box'}
    people = [size_image('man1.PNG', size=3), size_image('man2.PNG', size=3),
              size_image('man3.PNG', size=3)]
    image2 = random.choice(people)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 'R' or level[y][x] == 'B' or level[y][x] == 'W' \
                    and level[y][x] != ' ':
                Tile('road', x, y)
                new_player = PlayerCar(image, x, y)
            else:
                if level[y][x] != ' ' and level[y][x] in dict_symbols:
                    Tile(dict_symbols[level[y][x]], x, y)
                elif level[y][x] != ' ' and level[y][x] in obstacles:
                    Obstacles(obstacles[level[y][x]], x, y)
                elif level[y][x] != ' ' and level[y][x] == '@':
                    Tile('grass', x, y)
                    man = Man(image2, x, y)
    return new_player, x, y, man


def terminate():
    pygame.quit()
    sys.exit()


dict_tiles = {'road': size_image('road.JPG'),
              'wood': size_image('wood2.PNG', size=3),
              'fountain': size_image('fountain.JPG'),
              'home1': size_image('home1.JPG', size=1),
              'home2': size_image('home2.JPG'), 'home3':
                  size_image('home3.JPG', size=1), 'home4':
                  size_image('home4.JPG', size=1), 'home5':
                  size_image('home5.JPG', size=1),
              'home6': size_image('home6.JPG', size=1),
              'home7': size_image('home7.JPG'), 'home8': size_image('home8.JPG'),
              'home9': size_image('home9.JPG', size=1), 'home10':
                  size_image('home10.JPG'), 'home11': size_image('home11.JPG'),
              'home12': size_image('home12.JPG', size=1),
              'water': size_image('water.JPG'), 'stump': size_image('stump.JPG'),
              'rock': size_image('rock.JPG'), 'flower1': size_image('flower1.JPG'),
              'flower2': size_image('flower2.JPG'), 'grass': size_image('grass.JPG'),
              'grass2': size_image('grass2.JPG'), 'finish': size_image('finish.gif')}
dict_obstacles = {'stones': size_image('stones.png', size=3),
                  'stones2': size_image('stones2.png', size=3),
                  'box': size_image('box.png')}
tile_width = tile_height = 50
if __name__ == "__main__":
    running = True
    start_game()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()
