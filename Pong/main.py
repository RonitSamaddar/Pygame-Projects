import pygame

GAME_NAME = "Pong"
WIDTH = 1200
HEIGHT = 960
FPS = 60
gameExit = 0 #1 for screenExit, 2 for gameExit 
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

def generate_border(width):
    for i in range(0,width):
        if (i%2==0): color = Black
        else: color = White
        pygame.draw.rect(game["gameDisplay"],color,[i*2,i*2,WIDTH-4*i,HEIGHT-4*i],1)

def get_start_screen():
    global gameExit
    
    #Game Loop
    while gameExit==0:
        for event in pygame.event.get():
            #Checking if exit/cross button at right top has been pressed
            if event.type == pygame.QUIT:
                gameExit = 2
        

        game["gameDisplay"].fill(Black)
        generate_border(50)
        pygame.display.update()


         #Setting frames per second
        game["clock"].tick(FPS)

    return gameExit

def main():
    init()
    gameExit = get_start_screen()
    pygame.quit()
    quit()
    



if __name__ == "__main__":
    main()