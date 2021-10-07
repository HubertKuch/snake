import pygame

pygame.init()
screen_width = 800
screen_height = 600

run = True

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((60,60))
        self.surf.fill((100, 100, 100))
        self.rect = self.surf.get_rect()

x = 100
y = 100
speed = 5

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        elif event.type == pygame.QUIT:
            run = False

    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 255, 255))
    ## Player
    player = Player()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= 50
            if event.key == pygame.K_s:
                y += 50
            if event.key == pygame.K_a:
                x -= 50
            if event.key == pygame.K_d:
                x += 50

    if x == screen_width:
        x = screen_width

    screen.blit(player.surf, (x, y, screen_width, screen_height))
    pygame.display.update()

    ##
    pygame.display.flip()

    pygame.display.flip()
