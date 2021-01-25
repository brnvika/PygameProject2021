import pygame  # библиотека для разработки 2D игр
import os  # библиотека для получения файлов
import sys  # обеспечивает доступ к некоторым переменным и функциям
import random  # библиотека для рандомного выбора

pygame.init()
SIZE = WIDTH, HEIGHT = 650, 650  # размеры окна
SCREEN = pygame.display.set_mode(SIZE)
STEP = 25  # шаг
SPRITES = pygame.sprite.Group()  # группы спрайтов
tiles_group = pygame.sprite.Group()
tiles_objects = pygame.sprite.Group()
tiles_obstacles = pygame.sprite.Group()
tiles_obstacles2 = pygame.sprite.Group()
player_group = pygame.sprite.Group()
cars = pygame.sprite.Group()
people_group = pygame.sprite.Group()
finish = pygame.sprite.Group()
finish_man = pygame.sprite.Group()
timer_object = pygame.sprite.Group()
tiles_monsters = pygame.sprite.Group()
trains = pygame.sprite.Group()
clock = pygame.time.Clock()  # счетчик времени
timer = pygame.USEREVENT + 1  # таймеры
pygame.time.set_timer(timer, 1000)
timer2 = pygame.USEREVENT + 2
timer3 = pygame.USEREVENT + 3
timer4 = pygame.USEREVENT + 4


def load_image(name, colorkey=None):  # загрузка изображений
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


def size_image(name, size=None):  # получение нужного размера тайла
    if size is None:
        image = pygame.transform.scale(load_image(name), (50, 50))
    elif size == 1:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (160, 150))
    elif size == 2:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (50, 100))
        image = pygame.transform.rotate(image, 90)
        image = pygame.transform.rotate(image, 180)
    elif size == 3:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (50, 50))
    elif size == 4:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (200, 130))
    elif size == 5:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (220, 170))
    elif size == 6:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (180, 190))
    elif size == 7:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (350, 180))
    elif size == 8:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (300, 200))
    elif size == 9:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (50, 100))
        image = pygame.transform.rotate(image, 90)
    elif size == 10:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (50, 300))
    elif size == 11:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (160, 170))
    elif size == 12:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (250, 190))
    elif size == 13:
        image = pygame.transform.scale(load_image(name, colorkey=-1), (190, 120))
    return image


def load_level(filename):  # загрузка уровней
    filename = "levels/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def start_game():  # начало игры
    pygame.mixer.music.load('music/sound2.mp3')
    pygame.mixer.music.play(-1)
    image = pygame.transform.scale(load_image("screen_game.JPG"),
                                   (WIDTH, HEIGHT))
    SCREEN.blit(image, (0, 0))
    pygame.draw.rect(SCREEN, (255, 0, 0), (275, 550, 100, 50))
    font = pygame.font.Font(None, 50)
    text = font.render("PLAY", True, (0, 255, 127))
    SCREEN.blit(text, (280, 560))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 275 <= event.pos[0] <= 375 and 550 <= event.pos[1] <= 600:
                    pygame.mixer.music.stop()
                    main_menu()
                    return
        pygame.display.flip()


def main_menu():  # главное меню
    pygame.mixer.music.load('music/sound1.mp3')
    pygame.mixer.music.play(-1)
    y = 100
    image_menu = pygame.transform.scale(load_image("Menu_game.jpg"),
                                        (WIDTH, HEIGHT))
    SCREEN.blit(image_menu, (0, 0))
    font = pygame.font.Font(None, 70)
    font2 = pygame.font.Font(None, 50)
    text = font.render("Game menu", True, (0, 0, 255))
    text_x = WIDTH // 2 - text.get_width() // 2
    for i in range(4):
        pygame.draw.rect(SCREEN, (255, 255, 50), (225, y, 200, 50))
        y += 100
    pygame.draw.rect(SCREEN, (255, 255, 255), (text_x - 10, 15, 300, 50))
    SCREEN.blit(text, (text_x, 20))
    text2 = font2.render("Rules", True, (153, 0, 255))
    text2_x = WIDTH // 2 - text2.get_width() // 2
    SCREEN.blit(text2, (text2_x, 110))
    text3 = font2.render("Start", True, (153, 0, 255))
    text3_x = WIDTH // 2 - text3.get_width() // 2
    SCREEN.blit(text3, (text3_x, 210))
    text4 = font2.render("Exit", True, (153, 0, 255))
    text4_x = WIDTH // 2 - text4.get_width() // 2
    SCREEN.blit(text4, (text4_x, 310))
    text5 = font2.render("Developers", True, (153, 0, 255))
    text5_x = WIDTH // 2 - text5.get_width() // 2
    SCREEN.blit(text5, (text5_x, 410))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 225 <= event.pos[0] <= 425 and 100 <= event.pos[1] <= 150:
                    rules_game()
                    return
                if 225 <= event.pos[0] <= 425 and 300 <= event.pos[1] <= 350:
                    terminate()
                    return
                if 225 <= event.pos[0] <= 425 and 200 <= event.pos[1] <= 250:
                    choose_car()
                    return
                if 225 <= event.pos[0] <= 425 and 400 <= event.pos[1] <= 450:
                    about_develops()
                    return
        pygame.display.flip()


def about_develops():  # окно разработчиков
    image = pygame.transform.scale(load_image("develops.jpg"), (WIDTH, HEIGHT))
    SCREEN.blit(image, (0, 0))
    words = ['DEVELOPERS:', '   - Baranova Viktoria']
    font = pygame.font.Font(None, 40)
    font2 = pygame.font.Font(None, 55)
    text = font.render("Close", True, (255, 129, 0))
    pygame.draw.rect(SCREEN, (0, 0, 255), (500, 540, 90, 50))
    SCREEN.blit(text, (505, 555))
    y = 200
    for word in words:
        text2 = font2.render(word, True, (0, 0, 255))
        SCREEN.blit(text2, (60, y))
        y += 50
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= event.pos[0] <= 590 and 540 <= event.pos[1] <= 590:
                    main_menu()
                    return
        pygame.display.flip()


def rules_game():  # правила игры
    image = pygame.transform.scale(load_image("rules.jpg"), (WIDTH, HEIGHT))
    SCREEN.blit(image, (0, 0))
    font = pygame.font.Font(None, 30)
    text = font.render("Close", True, (255, 0, 0))
    pygame.draw.rect(SCREEN, (255, 255, 50), (500, 540, 90, 50))
    SCREEN.blit(text, (515, 555))
    words = ['                  Правила игры', '- После нажатия на кнопку START',
             'появляется окнo, в котором', 'нужно выбрать машину,нажав нужную',
             'цифру на клавиатуре. После этого', 'начнется 1 уровень игры.',
             '- Нажимая "пробел", вы можете срелять,',
             'но убить можно только монстров', 'или пробить стену.',
             '- Доехав до финишной линии, включается новый уровень.',
             'Цель: довести человечка до нужного места.']
    y = 40
    for word in words:
        text2 = font.render(word, True, (255, 0, 0))
        SCREEN.blit(text2, (30, y))
        y += 30
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 500 <= event.pos[0] <= 590 and 540 <= event.pos[1] <= 590:
                    main_menu()
                    return
        pygame.display.flip()


car = 0  # номер машинки по цвету


def choose_car():  # выбор машины
    global car
    image = pygame.transform.scale(load_image("choose_car.jpg"),
                                   (WIDTH, HEIGHT))
    SCREEN.blit(image, (0, 0))
    font = pygame.font.Font(None, 40)
    text = font.render("Choose car", True, (0, 0, 0))
    text_x = WIDTH // 2 - text.get_width() // 2
    SCREEN.blit(text, (text_x, 20))
    image_car1 = pygame.transform.scale(load_image("car1.png"), (300, 100))
    SCREEN.blit(image_car1, (175, 70))
    image_car2 = pygame.transform.scale(load_image("car2.png"), (320, 180))
    SCREEN.blit(image_car2, (175, 190))
    image_car3 = pygame.transform.scale(load_image("car3.png"), (300, 180))
    SCREEN.blit(image_car3, (175, 370))
    text1 = font.render("1", True, (0, 0, 255))
    text2 = font.render("2", True, (0, 0, 0))
    text3 = font.render("3", True, (255, 0, 0))
    SCREEN.blit(text1, (322, 190))
    SCREEN.blit(text2, (322, 360))
    SCREEN.blit(text3, (322, 550))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    car = 1
                    pygame.mixer.music.stop()
                    play_game()
                    return
                elif event.key == pygame.K_2:
                    car = 2
                    pygame.mixer.music.stop()
                    play_game()
                    return
                elif event.key == pygame.K_3:
                    car = 3
                    pygame.mixer.music.stop()
                    play_game()
                    return
        pygame.display.flip()


class Tile(pygame.sprite.Sprite):  # тайлы фона
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, SPRITES)
        self.image = dict_tiles[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class Objects(pygame.sprite.Sprite):  # тайлы объектов
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_objects, SPRITES)
        self.image = objects[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class Obstacles(pygame.sprite.Sprite):  # тайлы препятствий 1
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_obstacles, SPRITES)
        self.image = dict_obstacles[tile_type]
        if tile_type == 'box':
            self.rect = self.image.get_rect().move((tile_width * pos_x),
                                                   tile_height * pos_y)
        else:
            self.rect = self.image.get_rect().move((tile_width * pos_x) + 25,
                                                   tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Obstacles2(pygame.sprite.Sprite):  # тайлы препятствий 2
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_obstacles2, SPRITES)
        self.image = dict_obstacles2[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Timer(pygame.sprite.Sprite):  # тайл увеличения времени
    def __init__(self, image, pos_x, pos_y):
        super().__init__(timer_object, SPRITES)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class PlayerCar(pygame.sprite.Sprite):  # игрок
    def __init__(self, image, pos_x, pos_y):
        super().__init__(player_group, SPRITES)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class OtherCars(pygame.sprite.Sprite):  # машины
    def __init__(self, image, pos_x, pos_y):
        super().__init__(cars, SPRITES)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Trains(pygame.sprite.Sprite):  # поезда
    def __init__(self, image, pos_x, pos_y):
        super().__init__(trains, SPRITES)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Monsters(pygame.sprite.Sprite):  # монстры
    def __init__(self, image, pos_x, pos_y):
        super().__init__(tiles_monsters, SPRITES)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Man(pygame.sprite.Sprite):  # заказчик такси 1
    def __init__(self, image, pos_x, pos_y):
        super().__init__(people_group, SPRITES)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class FinishMan(pygame.sprite.Sprite):  # заказчик такси 2
    def __init__(self, image, pos_x, pos_y):
        super().__init__(finish_man, SPRITES)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class Shell:  # снаряды
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 30

    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN, self.color, (self.x, self.y), self.radius)


class Finish(pygame.sprite.Sprite):  # конец уровня
    def __init__(self, image, pos_x, pos_y):
        super().__init__(finish, SPRITES)
        self.image = image
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)
        self.mask = pygame.mask.from_surface(self.image)


class Camera:  # камера
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


level = 2  # уровень


def play_game():  # основной цикл игры
    global level
    levels = {1: 'level1.txt', 2: 'level2.txt', 3: 'level3.txt', 4: 'level4.txt',
              5: 'level5.txt'}
    speed_player = {1: (15, 25, 25), 2: (13, 20, 30), 3: (14, 20, 30),
                    4: (15, 25, 30), 5: (13, 20, 30)}
    player, level_x, level_y, man, man_f, end, other_cars, time, monsters, locomotives = \
        generate_level(load_level(levels[level - 1]))
    camera = Camera((level_x, level_y))
    font = pygame.font.Font(None, 50)
    num_level = font.render('level: ' + str(level - 1), True, (0, 0, 0))
    pygame.time.set_timer(timer2, 100)
    pygame.time.set_timer(timer3, 65)
    pygame.time.set_timer(timer4, 70)
    traffic_car = 0  # движение машин
    traffic_monster = True  # движение монстров
    speed = speed_player[level - 1][0]  # скорость машины
    seconds = speed_player[level - 1][-1]  # количество секунд для прохождения
    bombs = []  # снаряды
    run = True
    run2 = False
    run3 = False
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        man.rect.y += 10
        pygame.mixer.music.load('music/sound6.mp3')
        pygame.mixer.music.play(1)
        if pygame.sprite.groupcollide(player_group, people_group, False, True):
            run2 = True
            run = False
        draw_tiles()
        people_group.draw(SCREEN)
        pygame.display.flip()
    while run2:
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT + 1:
                if seconds > 0:
                    seconds -= 1
                elif seconds == 0:
                    delete_tiles()
                    game_over()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and traffic_car < 2:
                    traffic_car += 1
                    player.rect.y -= tile_height
                if event.key == pygame.K_DOWN and traffic_car > -2:
                    traffic_car -= 1
                    player.rect.y += tile_height
            if event.type == pygame.USEREVENT + 2:
                if len(monsters) >= 1:
                    for monster in monsters:
                        if monster.rect.y == 400:
                            traffic_monster = False
                        elif monster.rect.y == 200:
                            traffic_monster = True
                        if traffic_monster:
                            monster.rect.y += 10
                        else:
                            monster.rect.y -= 10
            if event.type == pygame.USEREVENT + 3:
                if len(other_cars) >= 1:
                    for other_car in other_cars:
                        if abs(other_car.rect.y - player.rect.x) <= 300:
                            other_car.rect.x -= STEP
            if event.type == pygame.USEREVENT + 4:
                if len(locomotives) >= 1:
                    for locomotive in locomotives:
                        if locomotive.rect.y <= 600:
                            if abs(locomotive.rect.x - player.rect.x) <= 500:
                                locomotive.rect.y -= 15
        player.rect.x += STEP
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and speed != 1:
            speed -= 1
        else:
            if speed < speed_player[level - 1][0]:
                speed += 1
        if keys[pygame.K_RIGHT] and speed < speed_player[level - 1][1]:
            speed += 1
        else:
            if speed > speed_player[level - 1][0]:
                speed -= 1
        for bomb in bombs:
            if bomb.x < 700:
                bomb.x += bomb.speed
            else:
                bombs.pop(bombs.index(bomb))
        if keys[pygame.K_SPACE]:
            pygame.mixer.music.load('music/sound4.mp3')
            pygame.mixer.music.play(1)
            if len(bombs) < 3:
                bombs.append(Shell(player.rect.x + 90,
                                   player.rect.y + 25, 8, (random.randrange(0, 255),
                                                           random.randrange(0, 255),
                                                           random.randrange(0, 255))))
        camera.update(player)
        for sprite in SPRITES:
            camera.apply(sprite)
        draw_tiles()
        finish.draw(SCREEN)
        SCREEN.blit(num_level, (10, 10))
        if seconds <= 10:
            timer_text = font.render('time: ' + str(seconds), True, (255, 0, 100))
        else:
            timer_text = font.render('time: ' + str(seconds), True, (0, 255, 0))
        SCREEN.blit(timer_text, (250, 10))
        for bomb in bombs:
            bomb.draw(SCREEN)
            for s in tiles_obstacles2:
                if bomb.x >= s.rect.x - player.rect.x + 100 \
                        and s.rect.y <= bomb.y <= s.rect.y + 50:
                    bombs = bombs[1:]
                    s.kill()
            for m in tiles_monsters:
                if bomb.x >= m.rect.x - player.rect.x + 100 \
                        and m.rect.y <= bomb.y <= m.rect.y + 50:
                    pygame.mixer.music.load('music/sound6.mp3')
                    pygame.mixer.music.play(1)
                    bombs = bombs[1:]
                    m.kill()
        if pygame.sprite.groupcollide(player_group, finish, False, False):  # проверка на столкновения
            level += 1
            run2 = False
            run3 = True
        if pygame.sprite.groupcollide(player_group, tiles_obstacles, False, False) \
                or pygame.sprite.groupcollide(player_group, tiles_obstacles2, False, False) \
                or pygame.sprite.groupcollide(player_group, cars, False, False) \
                or pygame.sprite.groupcollide(player_group, tiles_monsters, False, False) \
                or pygame.sprite.groupcollide(player_group, trains, False, False):
            run2 = False
            delete_tiles()
            game_over()
        if pygame.sprite.groupcollide(player_group, timer_object, False, True):
            seconds += 5
        pygame.display.flip()
    man_f.rect.y = player.rect.y + 50
    while run3:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        man_f.rect.y += 10
        pygame.mixer.music.load('music/sound6.mp3')
        pygame.mixer.music.play(1)
        if man_f.rect.y == 500:
            delete_tiles()
            if level >= 6:
                level = 2
                game_win()
            else:
                play_game()
            return
        draw_tiles()
        finish_man.draw(SCREEN)
        pygame.display.flip()


def delete_tiles():  # удаление тайлов
    player_group.empty()
    tiles_obstacles.empty()
    tiles_obstacles2.empty()
    tiles_group.empty()
    finish.empty()
    tiles_objects.empty()
    people_group.empty()
    finish_man.empty()
    cars.empty()
    timer_object.empty()
    tiles_monsters.empty()
    trains.empty()


def draw_tiles():  # отображение тайлов
    tiles_group.draw(SCREEN)
    tiles_objects.draw(SCREEN)
    tiles_obstacles.draw(SCREEN)
    tiles_obstacles2.draw(SCREEN)
    player_group.draw(SCREEN)
    cars.draw(SCREEN)
    timer_object.draw(SCREEN)
    tiles_monsters.draw(SCREEN)
    trains.draw(SCREEN)


def game_over():  # экран проигрыша
    pygame.mixer.music.load('music/sound3.mp3')
    pygame.mixer.music.play(1)
    image = pygame.transform.scale(load_image("game_over.jpg"),
                                   (400, 400))
    SCREEN.blit(image, (125, 125))
    font = pygame.font.Font(None, 40)
    text = font.render("restart", True, (255, 51, 0))
    pygame.draw.rect(SCREEN, (0, 255, 204), (145, 465, 120, 40))
    SCREEN.blit(text, (160, 473))
    text2 = font.render("menu", True, (255, 51, 0))
    pygame.draw.rect(SCREEN, (0, 255, 204), (385, 465, 120, 40))
    SCREEN.blit(text2, (405, 473))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 385 <= event.pos[0] <= 505 and 465 <= event.pos[1] <= 505:
                    main_menu()
                    return
                if 145 <= event.pos[0] <= 265 and 465 <= event.pos[1] <= 505:
                    restart()
                    return
        pygame.display.flip()


def game_win():  # экран победы
    pygame.mixer.music.load('music/sound5.mp3')
    pygame.mixer.music.play(1)
    image = pygame.transform.scale(load_image("game_passed.JPG"),
                                   (400, 400))
    SCREEN.blit(image, (125, 125))
    font = pygame.font.Font(None, 40)
    text = font.render("restart", True, (255, 51, 0))
    pygame.draw.rect(SCREEN, (0, 255, 222), (145, 465, 120, 40))
    SCREEN.blit(text, (160, 473))
    text2 = font.render("menu", True, (255, 51, 0))
    pygame.draw.rect(SCREEN, (0, 255, 222), (385, 465, 120, 40))
    SCREEN.blit(text2, (405, 473))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 385 <= event.pos[0] <= 505 and 465 <= event.pos[1] <= 505:
                    main_menu()
                    return
                if 145 <= event.pos[0] <= 265 and 465 <= event.pos[1] <= 505:
                    restart()
                    return
        pygame.display.flip()


def restart():  # начать заново уровень
    play_game()


def generate_level(level):  # генерация уровня
    global car
    if car == 1:
        image = size_image('blue_car.PNG', size=2)
    elif car == 2:
        image = size_image('white_car.PNG', size=2)
    elif car == 3:
        image = size_image('red_car.PNG', size=2)
    new_player, x, y, man, man_f, end, time = \
        None, None, None, None, None, None, None
    monsters = []
    other_cars = []
    locomotives = []
    dict_symbols = {'g': 'grass', '*': 'grass2', 's': 'stump',
                    'z': 'wood', 'r': 'rock', '-': 'flower1', '+': 'flower2',
                    '.': 'road', '$': 'train_road', '/': 'bridge'}
    objects_symbols = {'1': 'home1', 'k': 'home20',
                       '2': 'home2', '3': 'home3', '4': 'home4',
                       '5': 'home5', '6': 'home6', '7': 'home7',
                       '8': 'home8', '9': 'home9', '0': 'home10',
                       'a': 'home11', 'b': 'home12', 'c': 'home13',
                       'd': 'home14', 'e': 'home15', 'f': 'home1',
                       'i': 'home17', 'j': 'home18', 'n': 'home19',
                       '<': 'wood1', '>': 'wood2', ')': 'wood3'}
    obstacles = {'&': 'stones', '%': 'stones2', '!': 'box'}
    obstacles2 = {'x': 'wall'}
    people = [size_image('man1.PNG', size=3), size_image('man2.PNG', size=3),
              size_image('man3.PNG', size=3)]
    arr_cars = [size_image('car4.PNG', size=9), size_image('car5.PNG', size=9),
                size_image('car6.PNG', size=9), size_image('car7.PNG', size=9),
                size_image('car8.PNG', size=9), size_image('car9.PNG', size=9),
                size_image('car10.PNG', size=9), size_image('car11.PNG', size=9),
                size_image('car12.PNG', size=9), size_image('car13.PNG', size=9),
                size_image('car14.PNG', size=9), size_image('car15.PNG', size=9),
                size_image('car16.PNG', size=9), size_image('car17.PNG', size=9)]
    arr_monsters = [size_image('monster1.PNG', size=3), size_image('monster2.PNG', size=3),
                    size_image('monster3.PNG', size=3), size_image('monster4.PNG', size=3),
                    size_image('monster5.PNG', size=3), size_image('monster6.PNG', size=3),
                    size_image('monster7.PNG', size=3)]
    arr_trains = [size_image('train1.PNG', size=10), size_image('train2.PNG', size=10)]
    image_man = random.choice(people)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 'C':
                Tile('road', x, y)
                new_player = PlayerCar(image, x, y)
            else:
                if level[y][x] in dict_symbols:
                    Tile(dict_symbols[level[y][x]], x, y)
                elif level[y][x] in objects_symbols:
                    Tile('grass', x, y)
                    Objects(objects_symbols[level[y][x]], x, y)
                elif level[y][x] in obstacles:
                    Tile('road', x, y)
                    Obstacles(obstacles[level[y][x]], x, y)
                elif level[y][x] == 'w':
                    Obstacles('water', x, y)
                elif level[y][x] in obstacles2:
                    Tile('road', x, y)
                    Obstacles2(obstacles2[level[y][x]], x, y)
                elif level[y][x] == '@':
                    Tile('grass', x, y)
                    man = Man(image_man, x, y)
                elif level[y][x] == '#':
                    end = Finish(size_image('finish.gif'), x, y)
                elif level[y][x] == 'p':
                    Tile('road', x, y)
                    man_f = FinishMan(image_man, x, y)
                elif level[y][x] == '?':
                    Tile('road', x, y)
                    other_cars.append(OtherCars(random.choice(arr_cars), x, y))
                elif level[y][x] == 't':
                    Tile('road', x, y)
                    time = Timer(size_image('timer.PNG', size=3), x, y)
                elif level[y][x] == 'M':
                    Tile('road', x, y)
                    monsters.append(Monsters(random.choice(arr_monsters), x, y))
                elif level[y][x] == 'T':
                    Tile('train_road', x, y)
                    locomotives.append(Trains(random.choice(arr_trains), x, y))
    return new_player, x, y, man, man_f, end, other_cars, time, monsters, locomotives


def terminate():  # остановка работы приложения
    pygame.quit()
    sys.exit()


dict_tiles = {'road': size_image('road.JPG'), 'train_road': size_image('train_road.JPG'),
              'stump': size_image('stump.JPG'),
              'rock': size_image('rock.JPG'), 'flower1': size_image('flower1.JPG'),
              'flower2': size_image('flower2.JPG'), 'grass': size_image('grass.JPG'),
              'grass2': size_image('grass2.JPG'), 'bridge': size_image('bridge.JPG')}
objects = {'home1': size_image('home1.PNG', size=1), 'home3': size_image('home3.PNG', size=1),
           'home4': size_image('home4.PNG', size=4), 'home5': size_image('home5.PNG', size=4),
           'home6': size_image('home6.PNG', size=1), 'home7': size_image('home7.PNG', size=5),
           'home8': size_image('home8.PNG', size=5), 'home9': size_image('home9.PNG', size=5),
           'home10': size_image('home10.PNG', size=6), 'home11': size_image('home11.PNG', size=5),
           'home12': size_image('home12.PNG', size=6), 'home13': size_image('home13.PNG', size=6),
           'home14': size_image('home14.PNG', size=6), 'home15': size_image('home15.PNG', size=6),
           'home16': size_image('home16.PNG', size=6), 'home18': size_image('home18.PNG', size=1),
           'home17': size_image('home17.PNG', size=12), 'home19': size_image('home19.PNG', size=13),
           'home20': size_image('home20.PNG', size=7), 'home2': size_image('home2.PNG', size=1),
           'wood1': size_image('wood1.PNG', size=11), 'wood2': size_image('wood2.PNG', size=11),
           'wood3': size_image('wood3.PNG', size=11)}
dict_obstacles = {'stones': size_image('stones.PNG', size=3),
                  'stones2': size_image('stones2.PNG', size=3),
                  'box': size_image('box.png'), 'water': size_image('water.JPG')}
dict_obstacles2 = {'wall': size_image('wall.JPG')}
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
