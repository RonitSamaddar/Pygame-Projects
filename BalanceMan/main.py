import pygame

GAME_NAME = "BalanceMan"
WIDTH = 1200
HEIGHT = 960
FPS = 60
#Defining Colours by their RGB values
White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Green2 = (0,150,0)
Blue = (0,0,255)
RB = (255,0,255)

game = {}

def init():
    h=HEIGHT
    w=WIDTH

    pygame.init()
    game["gameDisplay"] = pygame.display.set_mode((w,h))
    game["clock"] = pygame.time.Clock()
    pygame.display.set_caption(GAME_NAME)

def gen_start_screen():
    for i in range(0,50):
        if (i%2==0): green = Red
        else: green = Blue
        pygame.draw.rect(game["gameDisplay"],green,[i*2,i*2,WIDTH-4*i,HEIGHT-4*i],1)
    
    
    font = pygame.font.Font('freesansbold.ttf', 100)
 
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('BALANCE MAN', True, RB)
    
    
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (WIDTH // 2, HEIGHT // 2 - 100)
    game["gameDisplay"].blit(text, textRect)


def main():
    init()
    gen_start_screen()

    gameExit = False

    #Game Loop
    while not gameExit:
        for event in pygame.event.get():
            #Checking if exit/cross button at right top has been pressed
            if event.type == pygame.QUIT:
                gameExit = True
        pygame.display.update()
    pygame.quit()
    quit()



if __name__ == "__main__":
    main()