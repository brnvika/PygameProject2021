import pygame
import os
import sys

pygame.init()
SIZE = WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode(SIZE)
STEP = 50
SPRITES = pygame.sprite.Group()

tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
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


def size_image(name):
    image = pygame.transform.scale(load_image(name), (50, 50))
    return image


def load_level(filename):
    filename = "levels/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def start_game():
    image = pygame.transform.scale(load_image("screen_game.JPG"), (WIDTH, HEIGHT))
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
    image_menu = pygame.transform.scale(load_image("Menu_game.jpg"), (WIDTH, HEIGHT))
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
                    play_game()
                    return
        pygame.display.flip()


def rules_game():
    image = pygame.transform.scale(load_image("rules.jpg"), (WIDTH, HEIGHT))
    SCREEN.blit(image, (0, 0))
    font2 = pygame.font.Font(None, 40)
    text = font2.render("Close", True, (0, 0, 255))
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


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, SPRITES)
        self.image = dict_tiles[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, SPRITES)
        self.image = car_player
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


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
        obj.rect.y += self.dy
        if obj.rect.y < -obj.rect.height:
            obj.rect.y += (self.field_size[1] + 1) * obj.rect.height
        if obj.rect.y >= self.field_size[1] * obj.rect.height:
            obj.rect.y -= (self.field_size[1] + 1) * obj.rect.height

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 4 - HEIGHT // 1.5)


def play_game():
    while True:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rect.x -= STEP
        if keys[pygame.K_RIGHT]:
            player.rect.x += STEP
        if keys[pygame.K_UP]:
            player.rect.y -= STEP
        if keys[pygame.K_DOWN]:
            player.rect.y += STEP
        camera.update(player)
        for sprite in SPRITES:
            camera.apply(sprite)
        tiles_group.draw(SCREEN)
        player_group.draw(SCREEN)
        pygame.display.flip()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('road', x, y)
            elif level[y][x] == '1':
                Tile('home1', x, y)
            elif level[y][x] == 'R':
                Tile('road', x, y)
                new_player = PlayerCar(x, y)
            elif level[y][x] == '2':
                Tile('home2', x, y)
            elif level[y][x] == '3':
                Tile('home3', x, y)
            elif level[y][x] == '4':
                Tile('home4', x, y)
            elif level[y][x] == '5':
                Tile('home5', x, y)
            elif level[y][x] == '6':
                Tile('home6', x, y)
            elif level[y][x] == '7':
                Tile('home7', x, y)
            elif level[y][x] == '8':
                Tile('home8', x, y)
            elif level[y][x] == '9':
                Tile('home9', x, y)
            elif level[y][x] == '0':
                Tile('home10', x, y)
            elif level[y][x] == 'e':
                Tile('home11', x, y)
            elif level[y][x] == 't':
                Tile('home12', x, y)
            elif level[y][x] == 'd':
                Tile('wood', x, y)
            elif level[y][x] == '+':
                Tile('flower2', x, y)
            elif level[y][x] == 's':
                Tile('stump', x, y)
            elif level[y][x] == 'g':
                Tile('grass', x, y)
            elif level[y][x] == '-':
                Tile('flower1', x, y)
            elif level[y][x] == 'w':
                Tile('water', x, y)
            elif level[y][x] == 'r':
                Tile('rock', x, y)
    return new_player, x, y


def terminate():
    pygame.quit()
    sys.exit()


dict_tiles = {'road': size_image('road.JPG'), 'wood': size_image('wood.JPG'),
              'fountain': size_image('fountain.JPG'), 'home1': size_image('home1.JPG'),
              'home2': size_image('home2.JPG'), 'home3': size_image('home3.JPG'),
              'home4': size_image('home4.JPG'), 'home5': size_image('home5.JPG'),
              'home6': size_image('home6.JPG'), 'home7': size_image('home7.JPG'),
              'home8': size_image('home8.JPG'), 'home9': size_image('home9.JPG'),
              'home10': size_image('home10.JPG'), 'home11': size_image('home11.JPG'),
              'home12': size_image('home12.JPG'), 'water': size_image('water.JPG'),
              'stump': size_image('stump.JPG'), 'rock': size_image('rock.JPG'),
              'flower1': size_image('flower1.JPG'), 'flower2': size_image('flower2.JPG'),
              'grass': size_image('grass.JPG'), 'grass2': size_image('grass2.JPG')}
car_player = size_image('red_car.JPG')
tile_width = tile_height = 50
player, level_x, level_y = generate_level(load_level('level1.txt'))
camera = Camera((level_x, level_y))

if __name__ == "__main__":
    running = True
    start_game()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()
