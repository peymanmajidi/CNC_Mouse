from pygame import *
import random as rd

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUMBER_OF_DOTS = 50

class Ball():
    SIZE = 30
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        draw.circle(screen, (0, 0, 0), (self.x, self.y), Ball.SIZE)
    def move(self, vx, vy):
        self.x += vx
        self.y += vy

class Dot():
    SIZE = 10  
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
    if (ball.x + ball.SIZE >= dot.x - dot.SIZE and ball.x - ball.SIZE <= dot.x - dot.SIZE)\
          and (ball.y - ball.SIZE <= dot.y - dot.SIZE  and ball.y + ball.SIZE >= dot.y + dot.SIZE):
        print("boom")
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
        dot.draw()
        
        if pick_up(ball, dot):
                dots.remove(dot)

    ball.draw()
    display.update()
    time.delay(1) # Speed down

