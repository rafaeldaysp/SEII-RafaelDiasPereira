from ast import YieldFrom
import pygame


WIDTH, HEIGHT = 900, 500
NAME_WINDOW = 'First Game'

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME_WINDOW)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

pygame.font.init()
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

pygame.mixer.init()
BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

FPS = 165
VEL = 2
VEL_BULLET = 4
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

SPACESHIP_DIMENSIONS = (55, 40)

YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(pygame.image.load('Assets/spaceship_yellow.png'), SPACESHIP_DIMENSIONS), 90)
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(pygame.image.load('Assets/spaceship_red.png'), SPACESHIP_DIMENSIONS), -90)
SPACE_BACKGROUND = pygame.transform.scale(
    pygame.image.load('Assets/space.png'), (WIDTH, HEIGHT) 
)



def yellow_move(key_pressed, yellow):
    if key_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.right < BORDER.x:
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.bottom < HEIGHT:
        yellow.y += VEL
        
def red_move(key_pressed, red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT] and red.right < WIDTH:
        red.x += VEL
    if key_pressed[pygame.K_UP] and red.y > 0:
        red.y -= VEL
    if key_pressed[pygame.K_DOWN] and red.bottom < HEIGHT:
        red.y += VEL

def bullets_handle(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += VEL_BULLET
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= VEL_BULLET
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.x < 0:
            red_bullets.remove(bullet)

def draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health):
    WIN.blit(SPACE_BACKGROUND, (0,0))
    pygame.draw.rect(WIN, (0, 255, 0), BORDER)
    
    red_health_text = HEALTH_FONT.render('Health: ' + str(red_health), 1, (0, 255, 0))
    yellow_health_text = HEALTH_FONT.render('Health: ' + str(yellow_health), 1, (0, 255, 0))
    
    WIN.blit(yellow_health_text, (0, 0))
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width(), 0))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (255, 255, 0), bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)
    pygame.display.update()
    
def draw_winner(winner_text):
    text = WINNER_FONT.render(winner_text, 1, (0, 255, 0))
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    

def main():
    
    yellow = pygame.Rect(180, 250, SPACESHIP_DIMENSIONS[0], SPACESHIP_DIMENSIONS[1])
    red = pygame.Rect(720, 250, SPACESHIP_DIMENSIONS[0], SPACESHIP_DIMENSIONS[1])
    
    red_bullets = []
    yellow_bullets = []
    
    red_health = 3
    yellow_health = 3
    
    winner_text = ''
    
    pause = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and len(yellow_bullets) < 3:
                    bullet = pygame.Rect(yellow.right, yellow.centery - 2, 10, 4)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    
                if event.key == pygame.K_BACKSPACE and len(red_bullets) < 3:
                    bullet = pygame.Rect(red.left, red.centery - 2, 10, 4)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        
        
        key_pressed = pygame.key.get_pressed()
        
        if pause == 0:
            yellow_move(key_pressed, yellow)
            red_move(key_pressed, red)
            bullets_handle(yellow_bullets, red_bullets, yellow, red)
            draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health)
        
        elif key_pressed[pygame.K_SPACE]:
            main()
        
        if red_health < 1:
            winner_text = 'Yellow Wins!'
            
        if yellow_health < 1:
            winner_text = 'Red Wins!'
        
        if winner_text != '':
            pause = 1
            draw_winner(winner_text)
            
    pygame.quit()
                
if __name__ == "__main__":
    main()
    