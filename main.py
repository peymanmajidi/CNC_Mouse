from pygame import *
import random as rd

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUMBER_OF_DOTS = 100

class Ball():
    SIZE = 25
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        draw.circle(screen, (0, 0, 0), (self.x, self.y), Ball.SIZE)
        
    def clear(self):
        draw.circle(screen, (255, 255, 255), (self.x, self.y), Ball.SIZE)
    def move(self, vx, vy):
        self.x += vx
        self.y += vy

class Dot():
    SIZE = 7
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random_color()

    def draw(self):
        draw.circle(screen, self.color, (self.x, self.y), Dot.SIZE)
    
def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)

def pick_up(ball, dot):
    ball_size = (int)(Ball.SIZE - (Ball.SIZE/8))
    ball_rect = Rect( ball.x - ball_size , ball.y - ball_size , ball_size*2, ball_size*2)
    dot_rect = Rect( dot.x - dot.SIZE , dot.y - dot.SIZE , dot.SIZE*2, dot.SIZE*2)
    

    if ball_rect.colliderect(dot_rect)>0:
        return True
    if dot_rect.colliderect(ball_rect)>0:
        return True
    return False


init()
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

dots = []
ball = Ball(200,200)



for i in range(NUMBER_OF_DOTS):
    x = rd.randint(100, 700)
    y = rd.randint(100, 500)
    dots.append(Dot(x,y))

while True:
    screen.fill((255, 255, 255))
    
    keys=key.get_pressed()

    for events in event.get():
        keys=key.get_pressed()
        if events.type == QUIT:
            quit()

    if keys[K_RIGHT]:
        ball.move(+1,0)
    if keys[K_LEFT]:
        ball.move(-1,0)
    if keys[K_UP]:
        ball.move(0,-1)
    if keys[K_DOWN]:
        ball.move(0,+1)

    for dot in dots:
        if pick_up(ball, dot): # if dot in range ball
                dots.remove(dot)
                Ball.SIZE+=1
        dot.draw()


    ball.draw()
    display.update()
    time.delay(1) # Speed down

