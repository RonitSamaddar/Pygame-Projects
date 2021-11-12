import pygame

GAME_NAME = "Pong"
WIDTH = 1360
HEIGHT = 960
FPS = 60
BORDER_WIDTH = 40
PLAYER_BLOCK_MARGIN = 30
PLAYER_BLOCK_WIDTH = 20
PLAYER_BLOCK_HEIGHT = 200
MOVEMENT_STEP = 5
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

class PlayerBlock:
    x1 = 0
    y1 = 0
    width = PLAYER_BLOCK_WIDTH
    height = PLAYER_BLOCK_HEIGHT
    motion_dir = 0

    def __init__(self,x1,y1,dir):
        self.x1 = x1
        self.y1 = y1
        self.motion_dir = dir
    
    def draw_player_block(self):
        x1=self.x1
        y1=self.y1
        w=self.width
        h=self.height

        pygame.draw.rect(game["gameDisplay"],White,[x1, y1, w, h],1)
        pygame.draw.rect(game["gameDisplay"],White,[x1+1, y1+1, w-2, h-2],1)
        h=h-4
        w=w-4
        index=2
        while(h>=0):
            if((h//3)%2==1): color = Black
            else : color = White
            pygame.draw.rect(game["gameDisplay"],color,[x1+2,y1+index,16,h],1)
            h=h-1
            index=index+1
    
    def move_player_block(self):
        self.y1=self.y1+self.motion_dir * MOVEMENT_STEP


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
    x1_P1 = BORDER_WIDTH + PLAYER_BLOCK_MARGIN
    y1_P1 = BORDER_WIDTH + PLAYER_BLOCK_MARGIN
    x2_P2 = WIDTH - (BORDER_WIDTH + PLAYER_BLOCK_MARGIN + PLAYER_BLOCK_WIDTH)
    y2_P2 = HEIGHT - (BORDER_WIDTH + PLAYER_BLOCK_MARGIN + PLAYER_BLOCK_HEIGHT)
    P1=PlayerBlock(x1_P1,y1_P1,0)
    P2=PlayerBlock(x2_P2,y2_P2,0)

    while gameExit==0:
        for event in pygame.event.get():
            #Checking if exit/cross button at right top has been pressed
            if event.type == pygame.QUIT:
                gameExit = 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    P1.motion_dir=1
                    P2.motion_dir=-1
                else:
                    P1.motion_dir=-1
                    P2.motion_dir=1
        
        P1.move_player_block()
        P2.move_player_block()

        game["gameDisplay"].fill(Black)
        generate_border(BORDER_WIDTH//2)
        P1.draw_player_block()
        P2.draw_player_block()
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