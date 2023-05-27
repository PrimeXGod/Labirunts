from pygame import *

class GameSprite(sprite.Sprite):
   
    def __init__(self, player_image, player_x, player_y, player_speed, image_size):
        super().__init__()

        self.image = transform.scale(image.load(player_image), image_size)
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 or self.rect.x > win_width - self.rect.width:
            self.speed = -self.speed


class WallSprite(GameSprite):
   
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


def draw_wall(x, y, width, height):
    for i in range(height // 50):
        for j in range(width // 50):
            wall = WallSprite('wall.png', x + j * 50, y + i * 50, 0, (50, 50))
            wall.reset(window)


win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))


player = GameSprite('hero.png', 5, win_height - 80, 8, (65, 65))
monster = GameSprite('cyborg.png', win_width - 80, 280, 2, (80, 80))
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0, (100, 100))

draw_wall(200, 0, 50, 200)
draw_wall(200, 400, 50, 200)
draw_wall(400, 150, 50, 200)
draw_wall(600, 500, 50, 200)
draw_wall(800, 0, 50, 200)


game = True
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

pickup_sound = mixer.Sound('money.ogg')
kick_sound = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))

    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and player.rect.x > 0:
        player.rect.x -= player.speed
    if keys_pressed[K_RIGHT] and player.rect.x < win_width - player.rect.width:
        player.rect.x += player.speed
    if keys_pressed[K_UP] and player.rect.y > 0:
        player.rect.y -= player.speed
    if keys_pressed[K_DOWN] and player.rect.y < win_height - player.rect.height:
        player.rect.y += player.speed

    player.reset(window)
    monster.reset(window)
    final.reset(window)

    monster.update()
    if player.rect.colliderect(monster.rect):
        kick_sound.play()
        font.init()
        my_font = font.Font(None, 70)
        text = my_font.render("Ти програв!", True, (255, 0, 0))
        window.blit(text, (win_width // 2 - text.get_width() // 2, win_height // 2 - text.get_height() // 2))
        display.update()
        time.wait(2000)
        game = False

    if player.rect.colliderect(final.rect):
        pickup_sound.play()
        font.init()
        my_font = font.Font(None, 70)
        text = my_font.render("Молодець!",True, (255, 0, 0))
        window.blit(text, (win_width // 2 - text.get_width() // 2, win_height // 2 - text.get_height() // 2))
        display.update()
        time.wait(2000)
        game = False

    display.update()
    clock.tick(FPS)

if not game:
    quit()
