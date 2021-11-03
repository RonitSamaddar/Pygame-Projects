import pygame

GAME_NAME = "BalanceMan"
WIDTH = 1200
HEIGHT = 960
FPS = 60
TEXT_ANGLE = 0
TEXT_X_CENTRE = 0
TEXT_Y_CENTRE = 0
mpx = 0
mpy = 0
bx1 = WIDTH//2-250
by1 = 150 + HEIGHT//2-75
bwidth = 500
bheight = 150
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

def generate_border():
    for i in range(0,50):
        if (i%2==0): green = Red
        else: green = Blue
        pygame.draw.rect(game["gameDisplay"],green,[i*2,i*2,WIDTH-4*i,HEIGHT-4*i],1)

def generate_text(xcentre,angle):
    font = pygame.font.Font('freesansbold.ttf', 100)
        
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('BALANCE MAN', True, RB)
    text = pygame.transform.rotate(text, angle)
    
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (WIDTH // 2 + 5*xcentre, HEIGHT // 2 - 150)
    game["gameDisplay"].blit(text, textRect)

def generate_button(mpx,mpy):
    bx1 = WIDTH//2-250
    by1 = 150 + HEIGHT//2-75
    bwidth = 500
    bheight = 150
    

    color1=RB
    color2=(color1[0]//2, color1[1]//2, color1[2]//2)

    if(mpx>=bx1 and mpx<=(bx1+bwidth) and mpy>=by1 and mpy<=(by1+bheight)):
        color=color2
        bx1=bx1+5
        by1=by1+5
    else:
        color=color1
    bxc=bx1+bwidth//2
    byc=by1+bheight//2

    pygame.draw.rect(game["gameDisplay"],color,[bx1,by1,bwidth,bheight],5)
    font = pygame.font.Font('freesansbold.ttf', 50)
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('START', True, color)
    
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (bxc,byc)
    game["gameDisplay"].blit(text, textRect)

def get_start_screen():
    text_d = [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
    index=0

    global gameExit
    
    #Game Loop
    while gameExit==0:
        for event in pygame.event.get():
            #Checking if exit/cross button at right top has been pressed
            if event.type == pygame.QUIT:
                gameExit = 2
            if event.type == pygame.MOUSEMOTION:
                mpx = event.pos[0]
                mpy = event.pos[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                mpx = event.pos[0]
                mpy = event.pos[1]
                if (event.button == 1 and mpx>=bx1 and mpx<=(bx1+bwidth) and mpy>=by1 and mpy<=(by1+bheight)):
                    gameExit = 1
                

        xc = TEXT_X_CENTRE + text_d[index//3]
        angle = TEXT_ANGLE + -1*text_d[index//3]
        index= (index+1)%(3*len(text_d))

        game["gameDisplay"].fill(Black)
        generate_border()
        generate_text(xc,angle)
        generate_button(mpx,mpy)
        pygame.display.update()


         #Setting frames per second
        game["clock"].tick(FPS)

    return gameExit

def main():
    init()
    get_start_screen()
    pygame.quit()
    quit()
    



if __name__ == "__main__":
    main()