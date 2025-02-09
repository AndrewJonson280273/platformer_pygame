import pygame

# Инициализация Pygame
pygame.init()

# Настройки окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Меню")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка фона
background_image = pygame.image.load('img/bg.jpg').convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Загрузка фоновой музыки
pygame.mixer.music.load('sound/menu_music.mp3')
pygame.mixer.music.play(-1)

# Размеры кнопок
button_sizes = [(250, 80), (250, 80)]
# Кнопки
button_images = [
    pygame.image.load('img/btn_play.png'),
    pygame.image.load('img/btn_credits.png'),

]

# Изменение размеров кнопок
for i, img in enumerate(button_images):
    button_images[i] = pygame.transform.scale(img, button_sizes[i])


# Динамическое определение позиций кнопок
def calculate_button_positions(buttons):
    positions = []
    total_height = sum([b.get_height() for b in buttons]) + len(buttons) * 10  # 10 - отступ между кнопками
    start_y = max(0, (screen_height - total_height) // 2)  # Центрирование по вертикали

    current_y = start_y
    for button in buttons:
        pos_x = (screen_width - button.get_width()) // 2
        pos_y = current_y
        positions.append((pos_x, pos_y))
        current_y += button.get_height() + 10  # Сдвигаемся вниз на высоту кнопки плюс отступ

    return positions


button_positions = calculate_button_positions(button_images)


# Функция для отображения текста на кнопках
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Основной игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    # Отображение фона
    screen.blit(background_image, (0, 0))

    # Отображение кнопок
    for i in range(len(button_images)):
        screen.blit(button_images[i], button_positions[i])

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Проверка нажатия на кнопки
            for i in range(len(button_images)):
                if button_images[i].get_rect(topleft=button_positions[i]).collidepoint(mouse_pos):
                    print(f"Кнопка {i + 1} нажата!")

    # Обновление экрана
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()