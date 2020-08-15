import pygame















#Variables
points1 = 0
points2 = 0
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VEL = 5

#Classes
class Ball:
    RAD = 20
    white = (255,255,255)
    black = (0,0,0)
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def show(self,color):
        global screen
        pygame.draw.circle(screen, color,(self.x,self.y),self.RAD)
    def update(self):
        global points1,points2
        if self.vx == 0 or self.vy == 0:
            
            return
        self.show(self.black)
        if ((self.x+self.RAD) <= (2*BORDER)):
            self.vx = -self.vx
            points1 += 1
        if ((self.x-self.RAD) >= WIDTH-(2*BORDER)):
            self.vx = -self.vx
            points2 += 1
        if ((self.y-self.RAD) <= BORDER) or ((self.y+self.RAD) >= HEIGHT-BORDER):
            self.vy = -self.vy
        
        self.x += self.vx
        self.y += self.vy
        self.show(self.white)
    @property
    def rect(self):
        return pygame.Rect(self.x-self.RAD,self.y-self.RAD,2*self.RAD,2*self.RAD)


#pygame.draw.rect(screen,(self.BREADTH+5),(HEIGHT//2))

class Paddle:
    LENGTH = 80
    BREADTH = 15
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self,color):
        global screen,HEIGHT,WIDTH
        pygame.draw.rect(screen,color,pygame.Rect(self.x,self.y,self.BREADTH,self.LENGTH))
    def update(self):
        global fgColor,bgColor
        self.show(bgColor)
        self.y = pygame.mouse.get_pos()[1]-(self.LENGTH//2)
        self.show(fgColor)
    @property
    def rect(self):
        return pygame.Rect(self.x,self.y,self.BREADTH,self.LENGTH)




ball = Ball(600,300,-VEL,VEL)
paddle1 = Paddle((WIDTH-Paddle.BREADTH-5),((HEIGHT-Paddle.LENGTH)//2))
paddle2 = Paddle((5),((HEIGHT-Paddle.LENGTH)//2))
#pygame.display.set_caption("woooooooooooooooooop")
#Draw screen

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

bgColor = (0,0,0)
fgColor = pygame.Color("white")

pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH,BORDER))
#pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))
ball.show(fgColor)
paddle1.show(fgColor)
paddle2.show(fgColor)

clock = pygame.time.Clock()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    else:
        pass
    ball.update()
    paddle1.update()
    paddle2.update()
    if pygame.sprite.collide_rect(ball,paddle1):
        print('boom boom ciao1')
        ball.vx = -ball.vx
        ball.vy = -ball.vy
    elif pygame.sprite.collide_rect(ball,paddle2):
        print('boom boom ciao2')
        ball.vx = -ball.vx
        ball.vy = -ball.vy
    pygame.display.set_caption("Player1:"+str(points1)+"   Player2:"+str(points2))
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
