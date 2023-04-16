import pygame
import random

# Oyun alanı boyutu
WIDTH = 600
HEIGHT = 600

# Yılanın başlangıç pozisyonu
snake_pos = [WIDTH/2, HEIGHT/2]

# Yılanın boyu ve hızı
snake_body = [[snake_pos[0], snake_pos[1]], [snake_pos[0]-10, snake_pos[1]], [snake_pos[0]-20, snake_pos[1]]]
snake_speed = 5

# Yem pozisyonlarını oluşturmak için rastgele x ve y değerleri üretin
food_pos = [random.randrange(1, WIDTH/10)*10, random.randrange(1, HEIGHT/10)*10]
food_spawned = True

# Skor
score = 0

# Pygame başlat
pygame.init()
pygame.font.init()

# Font
font = pygame.font.SysFont('bahnschrift', 25)

# Oyun ekranı boyutu ve başlığı
screen = pygame.display.set_mode((WIDTH, HEIGHT+20))
pygame.display.set_caption('Yılan Oyunu')

# Başlangıç yönü
direction = 'RIGHT'

# Oyun döngüsü
game_over = False
lives = 3
clock = pygame.time.Clock()

while not game_over:
    # Oyuncu etkileşimi için eventleri yakalayın
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'

    # Yılanın hareketini hesaplayın
    if direction == 'LEFT':
        snake_pos[0] -= snake_speed
    elif direction == 'RIGHT':
        snake_pos[0] += snake_speed
    elif direction == 'UP':
        snake_pos[1] -= snake_speed
    elif direction == 'DOWN':
        snake_pos[1] += snake_speed

    # Yılanın duvara çarpıp çarpmadığını kontrol edin
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10 or snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        lives -= 1
        if lives == 0:
            game_over = True
        else:
            snake_pos = [WIDTH/2, HEIGHT/2]
            snake_body = [[snake_pos[0], snake_pos[1]], [snake_pos[0]-10, snake_pos[1]], [snake_pos[0]-20, snake_pos[1]]]
            direction = 'RIGHT'
    # Yılanın yemi yiyip yemediğini kontrol ed
    if snake_pos == food_pos:
        food_spawned = False
        score += 10
        snake_body.append([0, 0])

    # Yem oluşturma
    if not food_spawned:
        food_pos = [random.randrange(1, WIDTH/10)*10, random.randrange(1, HEIGHT/10)*10]
        food_spawned = True

    # Yılanın boyunu güncelle
    for i in range(len(snake_body)-1, 0, -1):
        snake_body[i][0] = snake_body[i-1][0]
        snake_body[i][1] = snake_body[i-1][1]
    snake_body[0][0] = snake_pos[0]
    snake_body[0][1] = snake_pos[1]

    # Ekranı temizleyin
    screen.fill((0, 0, 0))

    # Yılanı ve yemi çizin
    for pos in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Skoru ekrana yazdırın
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (WIDTH-100, HEIGHT))

    # Canları ekrana yazdırın
    lives_text = font.render("Lives: " + "❤"*lives, True, (255, 255, 255))
    screen.blit(lives_text, (10, HEIGHT))

    # Ekranı güncelleyin
    pygame.display.update()

    # Oyun hızını ayarlayın
    clock.tick(20)

# Oyun bittiğinde skoru ekrana yazdırın
game_over_text = font.render("GAME OVER - Score: " + str(score), True, (255, 255, 255))
screen.blit(game_over_text, (WIDTH/2-100, HEIGHT/2))
pygame.display.update()

# Oyunu kapatın
pygame.quit()


