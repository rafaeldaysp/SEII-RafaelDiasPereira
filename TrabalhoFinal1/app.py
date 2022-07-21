import pygame, controle, elements

WIDTH, HEIGHT = 1200, 720

NAME_WINDOW = 'Aeropêndulo'

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME_WINDOW)

BACKGROUND = pygame.transform.scale(
    pygame.image.load('Images/background2.jpg'), (WIDTH, HEIGHT) 
)

BUTTON_DIMENTIONS = (250, 100)

COLOR = {'WHITE': (255, 255, 255), 'BLUE': (100, 40, 255), 'RED': (255, 0, 0), 'PURPLE': (100, 40, 150), 'DARK_RED': (150, 50, 50)}

X_ALIGN_BUTTONS = 100
Y_DISPLAY = 150

DISPLAY = elements.Button(COLOR['WHITE'], X_ALIGN_BUTTONS, Y_DISPLAY, BUTTON_DIMENTIONS[0], BUTTON_DIMENTIONS[1])
START = elements.Button(COLOR['BLUE'], X_ALIGN_BUTTONS, DISPLAY.y + BUTTON_DIMENTIONS[1] + 50, BUTTON_DIMENTIONS[0], BUTTON_DIMENTIONS[1], 'Start')
STOP = elements.Button(COLOR['RED'], X_ALIGN_BUTTONS, START.y + BUTTON_DIMENTIONS[1] + 50, BUTTON_DIMENTIONS[0], BUTTON_DIMENTIONS[1], 'Stop')

ANGLE_TEXT = pygame.font.SysFont('comicsans', 60)

PENDULUM_DIMENTIONS = (400, 400)

BASE = pygame.transform.scale(
    pygame.image.load('Images/base.png'), PENDULUM_DIMENTIONS
)
PENDULUM_IMAGE_1 = pygame.transform.scale(
    pygame.image.load('Images/pendulum.png'), PENDULUM_DIMENTIONS 
)
PENDULUM_IMAGE_2 = pygame.transform.scale(
    pygame.image.load('Images/pendulum2.png'), PENDULUM_DIMENTIONS 
)
PENDULUM_IMAGE_3 = pygame.transform.scale(
    pygame.image.load('Images/pendulum3.png'), PENDULUM_DIMENTIONS 
)

PIVOT = (800, 200)
OFFSET = pygame.math.Vector2(30, 190)
FPS = 60
SIMUL_TIME_S = 60

def rotate(image, angle):

    rotated_image = pygame.transform.rotate(image, angle)  
    rotated_offset = OFFSET.rotate(-angle)  

    rect = rotated_image.get_rect(center=PIVOT+rotated_offset)
    
    return rotated_image, rect  

def move_pendulum(angle, k, spin):
    if spin:
        if k%3 == 0:
            rotated_image, rect1 = rotate(PENDULUM_IMAGE_1, angle)
        elif k%2 == 0:
            rotated_image, rect1 = rotate(PENDULUM_IMAGE_2, angle)
        else:
            rotated_image, rect1 = rotate(PENDULUM_IMAGE_3, angle)
    else:
        rotated_image, rect1 = rotate(PENDULUM_IMAGE_1, angle)
    
    return rotated_image, rect1

def draw_window(pendulum, rotated_image, user_input):
    
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(BASE, (PIVOT[0] - OFFSET[1] - 7, PIVOT[1] - OFFSET[0]))
    WIN.blit(rotated_image, pendulum)
    START.draw(WIN, (0,0,0))
    STOP.draw(WIN, (0, 0, 0))
    DISPLAY.draw(WIN, (0, 0, 0))
    text = ANGLE_TEXT.render(user_input, 1, (0, 0, 0))
    WIN.blit(text, (DISPLAY.x + 20, Y_DISPLAY + 10))
    
    pygame.display.update()

def main():
    
    clock = pygame.time.Clock()
    
    output = [0]
    user_input = '0'
    k = 0
    spin = False
    
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEMOTION:
                if START.isOver(pos):
                    START.color = COLOR['PURPLE']
                else:
                    START.color = COLOR['BLUE']
                if STOP.isOver(pos):
                    STOP.color = COLOR['DARK_RED']
                else:
                    STOP.color = COLOR['RED']
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START.isOver(pos):
                    
                    if user_input == '' or user_input == '.':
                        user_input = '0'
                    if user_input[-1] == '.':
                        user_input = user_input[:-1]
                    
                    input = float(user_input)
                    output = controle.main(input, initial_pos, SIMUL_TIME_S, FPS)
                    k=0
                    spin = True
                
                if STOP.isOver(pos):
                    user_input = '0'
                    input = 0
                    output = controle.main(input, initial_pos, SIMUL_TIME_S, FPS)
                    k=0
                    spin = False
            
            if event.type == pygame.KEYDOWN:
                if len(user_input) < 5:
                    if 47 < ord(event.unicode) < 58 or ord(event.unicode)==46:
                        if user_input == '0':
                            user_input = event.unicode
                        else:
                            user_input += event.unicode
                if ord(event.unicode) == 8:
                    user_input = user_input[:-1] 
                    
            
        try:
            rotated_image, rect1 = move_pendulum(output[k], k, spin)
            initial_pos = output[k]
        except:
            pass
        
        k += 1
        
        draw_window(rect1, rotated_image, user_input)
    
if __name__ == "__main__":
    main()
    