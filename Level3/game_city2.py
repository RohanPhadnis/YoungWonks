import pygame, random
from pygame.locals import *
pygame.init()

size = 720#int(input('screen size: '))
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption('Game City 2')
clock = pygame.time.Clock()
FR = 25


def show_text(text, x, y, color = (255,255,255)):
    font=pygame.font.SysFont('freesans',40)
    textobj=font.render(text,False,color)
    screen.blit(textobj,(x,y))


class Ball:
    def __init__(self, vel, x = size//2, y = size//2, r = 25):
        self.pos = [x,y]
        self.radius = r
        self.figure = 0
        self.vel = vel
        self.spd = 5
    def draw(self):
        self.figure = pygame.draw.circle(screen, (0,0,255), (self.pos[0], self.pos[1]), self.radius)
    def move(self):
        self.pos[0] += self.vel[0] * int(self.spd)
        self.pos[1] += self.vel[1] * int(self.spd)
        self.spd += 0.001
    def bounce(self, vel = [random.choice([-3,-2,-1,1,2,3]), random.choice([-3,-2,-1,1,2,3])]):
        self.vel = vel

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.pos = [x,y]
        self.dim = [width, height]
        self.figure = 0
        self.color = color
    def draw(self):
        self.figure = pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.dim[0], self.dim[1]))

class Snake(Paddle):
    def __init__(self, x, y, index, width = size//30, height = size//30, color = (0,255,0)):
        super().__init__(x, y, width, height, color)
        self.old_pos = [x,y]
        self.index = index
        self.vel = []
    def move(self, snakeList, vel = None):
        self.vel = vel
        self.old_pos[0] = self.pos[0]
        self.old_pos[1] = self.pos[1]
        if self.index == 0:
            self.pos[0] += self.vel[0] * size//30
            self.pos[1] += self.vel[1] * size//30
        else:
            self.pos[0] = snakeList[self.index-1].old_pos[0]
            self.pos[1] = snakeList[self.index-1].old_pos[1]

class Tile(Paddle):
    def __init__(self, x, y, color, index, width = size//3, height = size//3):
        super().__init__(x, y, width, height, color)
        self.status = 'n'
        self.index = index
    def draw(self):
        super().draw()
        if self.status == 'x':
            pygame.draw.line(screen, (255,0,0), (self.pos[0], self.pos[1]), (self.pos[0]+self.dim[0], self.pos[1]+self.dim[1]), 4)
            pygame.draw.line(screen, (255,0,0), (self.pos[0]+self.dim[0], self.pos[1]), (self.pos[0], self.pos[1]+self.dim[1]), 4)
        elif self.status == 'o':
            pygame.draw.circle(screen, (255,0,0), ((self.pos[0]*2+self.dim[0])//2, (self.pos[1]*2+self.dim[1])//2), self.dim[0]//2, 4)

class Button(Paddle):
    def __init__(self, text, x, y, color, command):
        self.text = text
        self.command = command
        super().__init__(x,y,len(text)*25,50,color)
    def do(self):
        self.command()
    def draw(self):
        super().draw()
        show_text(self.text, self.pos[0]+15, self.pos[1])


def nothing():
    pass

def pong1():
    
    ball = Ball(vel = [random.choice([-1,1]), random.choice([-1,1])])
    paddleA = Paddle(20, (size//2)-50, 20, 100, (255,0,0))
    paddleB = Paddle(size-40, (size//2)-50, 20, 100, (255,0,0))
    vel = 0
    do = True
    back = Button('menu', 50,50, (150,150,150), nothing)
    score = 0
    while do:
        screen.fill((0,0,0))
        back.draw()
        show_text('score: '+str(score), size-200, 50)
        ball.draw()
        ball.move()
        paddleA.draw()
        paddleB.draw()
        paddleA.pos[1] = ball.pos[1]-50
        paddleB.pos[1]+=vel*ball.spd
        
        if paddleB.pos[1]<0:
            paddleB.pos[1] = 0
        elif paddleB.pos[1]+100>size:
            paddleB.pos[1] = size-100
        if ball.pos[1]<25 and ball.vel[1]<0:
            ball.bounce(vel = [random.choice([-3,-2,-1,1,2,3]), random.randint(1,3)])
        elif ball.pos[1]>size-25 and ball.vel[1]>0:
            ball.bounce(vel = [random.choice([-3,-2,-1,1,2,3]), random.randint(-3,-1)])

        if ball.figure.colliderect(paddleB.figure) and ball.vel[0]>0:
            ball.bounce(vel = [random.randint(-3,-1), random.choice([-3,-2,-1,1,2,3])])
            score+=1
        elif ball.figure.colliderect(paddleA.figure) and ball.vel[0]<0:
            ball.bounce(vel = [random.randint(1,3), random.choice([-3,-2,-1,1,2,3])])

        if ball.pos[0]>900:
            show_text('Game Over!', (size//2) - 50, size//2)
            ball.vel = [0,0]
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    vel = -5
                elif event.key == K_DOWN:
                    vel = 5
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    vel = 0
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and back.figure.collidepoint(event.pos):
                do = False
            
        pygame.display.update()
        clock.tick(FR)


def pong2():
    ball = Ball(vel = [random.choice([-1,1]), random.choice([-1,1])])
    paddleA = Paddle(20, (size//2)-50, 20, 100, (255,0,0))
    paddleB = Paddle(size-40, (size//2)-50, 20, 100, (255,0,0))
    velA = 0
    velB = 0
    do = True
    back = Button('menu', 50,50, (150,150,150), nothing)
    while do:
        screen.fill((0,0,0))
        back.draw()
        ball.draw()
        ball.move()
        paddleA.draw()
        paddleB.draw()
        paddleA.pos[1] += velA*ball.spd
        paddleB.pos[1]+=velB*ball.spd
        if paddleA.pos[1]<0:
            paddleA.pos[1] = 0
        elif paddleA.pos[1]+100>size:
            paddleA.pos[1] = size-100
        if paddleB.pos[1]<0:
            paddleB.pos[1] = 0
        elif paddleB.pos[1]+100>size:
            paddleB.pos[1] = size-100
        if ball.pos[1]<25 and ball.vel[1]<0:
            ball.bounce(vel = [random.choice([-3,-2,-1,1,2,3]), random.randint(1,3)])
        elif ball.pos[1]>size-25 and ball.vel[1]>0:
            ball.bounce(vel = [random.choice([-3,-2,-1,1,2,3]), random.randint(-3,-1)])

        if ball.figure.colliderect(paddleB.figure) and ball.vel[0]>0:
            ball.bounce(vel = [random.randint(-3,-1), random.choice([-3,-2,-1,1,2,3])])
        elif ball.figure.colliderect(paddleA.figure) and ball.vel[0]<0:
            ball.bounce(vel = [random.randint(1,3), random.choice([-3,-2,-1,1,2,3])])

        if ball.pos[0]>size or ball.pos[0]<0:
            show_text('Game Over!', (size//2) - 50, size//2)
            ball.vel = [0,0]

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    velB = -2
                elif event.key == K_DOWN:
                    velB = 2
                elif event.key == K_w:
                    velA = -2
                elif event.key == K_s:
                    velA = 2
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    velB = 0
                elif event.key == K_w or event.key == K_s:
                    velA = 0
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and back.figure.collidepoint(event.pos):
                do = False
            
        pygame.display.update()
        clock.tick(FR)
        

def flappy_ball():
    ball = Ball([0,1])
    gap = random.randint(100, 200)
    up = Paddle(size, 0, 100, random.randint(70,size-150), color = (255,0,0))
    down = Paddle(up.pos[0], up.dim[1]+gap, 100, size, color = (255,0,0))
    do = True
    back = Button('menu', 50,50, (150,150,150), nothing)
    score = 0
    old_pos = 0
    while do:
        screen.fill((0,0,0))
        ball.move()
        old_pos = up.pos[0]
        up.pos[0]-=int(ball.spd)
        down.pos[0] = up.pos[0]
        up.draw()
        down.draw()
        back.draw()
        show_text('score: '+str(score), size-200, 50)
        ball.draw()

        if ball.pos[0]-25>up.pos[0]+100 and ball.pos[0]-25<old_pos+100:
            score+=1
        
        if up.pos[0] <= -100:
            up.pos[0] = size
            up.dim[1] = random.randint(0, size-150)
            gap = random.randint(100,200)
            down.pos[1] = up.dim[1]+gap

        if ball.pos[1]<25 or ball.pos[1]>size-25 or ball.figure.colliderect(up.figure) or ball.figure.colliderect(down.figure):
            ball.vel = [0,0]
            ball.spd = 0
            show_text('Game Over!', (size//2) - 50, size//2)
        
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                ball.vel[1] = -1
            elif event.type == KEYUP and event.key == K_SPACE:
                ball.vel[1] = 1
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and back.figure.collidepoint(event.pos):
                do = False
        pygame.display.update()
        clock.tick(FR)



def tic_tac_toe():
    tiles = []
    active = 0
    for x in range(3):
        for y in range(3):
            if active % 2 == 0:
                tiles.append(Tile(x*size//3,y*size//3,(255,255,255), active))
            else:
                tiles.append(Tile(x*size//3,y*size//3,(0,0,0), active))
            active+=1
    do = True
    active = 1
    count = 0
    winner = 'n'
    back = Button('menu', 50,50, (150,150,150), nothing)
    while do:
        screen.fill((0,0,0))
        
        count = 0
        for tile in tiles:
            tile.draw()
            if tile.status == 'n':
                count+=1
        back.draw()
        if count == 0 and winner == 'n':
            show_text('Draw!', (size//2) - 50, size//2, color = (0,0,255))
        if (tiles[0].status == tiles[1].status == tiles[2].status == 'x' or
            tiles[3].status == tiles[4].status == tiles[5].status == 'x' or
            tiles[6].status == tiles[7].status == tiles[8].status == 'x' or
            tiles[0].status == tiles[3].status == tiles[6].status == 'x' or
            tiles[1].status == tiles[4].status == tiles[7].status == 'x' or
            tiles[2].status == tiles[5].status == tiles[8].status == 'x' or
            tiles[0].status == tiles[4].status == tiles[8].status == 'x' or
            tiles[2].status == tiles[4].status == tiles[6].status == 'x') and winner == 'n':
            winner = 'x'
        elif (tiles[0].status == tiles[1].status == tiles[2].status == 'o' or
            tiles[3].status == tiles[4].status == tiles[5].status == 'o' or
            tiles[6].status == tiles[7].status == tiles[8].status == 'o' or
            tiles[0].status == tiles[3].status == tiles[6].status == 'o' or
            tiles[1].status == tiles[4].status == tiles[7].status == 'o' or
            tiles[2].status == tiles[5].status == tiles[8].status == 'o' or
            tiles[0].status == tiles[4].status == tiles[8].status == 'o' or
            tiles[2].status == tiles[4].status == tiles[6].status == 'o') and winner == 'n':
            winner = 'o'
        if winner != 'n':
            show_text(winner.upper()+' Wins!', (size//2) - 50, size//2, color = (0,0,255))
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                for tile in tiles:
                    if tile.figure.collidepoint(event.pos) and tile.status == 'n':
                        if active == -1:
                            tile.status = 'o'
                        else:
                            tile.status = 'x'
                        active*=-1
                if back.figure.collidepoint(event.pos):
                    do = False
        pygame.display.update()
        clock.tick(FR)


def snake():
    snakeList = [Snake(random.randint(0,29)*size//30, random.randint(0,29)*size//30, 0)]
    do = True
    vel = [0,0]
    index = 0
    food = Paddle(random.randint(0,29) * size//30, random.randint(0,29) * size//30, size//30, size//30, (255,0,0))
    back = Button('menu', 50,50, (150,150,150), nothing)
    game = False
    screen.fill((0,0,0))
    for x in range(30):
        pygame.draw.line(screen, (255,255,255), (x*size//30, 0), (x*size//30, 900), 1)
    for y in range(30):
        pygame.draw.line(screen, (255,255,255), (0, y*size//30), (900, y*size//30), 1)
    while do:
        
        
        back.draw()
        pygame.draw.rect(screen, (0,0,0), (size-200, 50, 200,30))
        show_text('score: '+str(index), size-200, 50)
        food.draw()
        for body in snakeList:
            body.move(snakeList, vel)
            body.draw()
            if (snakeList[0].figure.colliderect(body.figure) and body.index!=0) or snakeList[0].pos[0]<0 or snakeList[0].pos[0]>=size or snakeList[0].pos[1]<0 or snakeList[0].pos[1]>=size:
                vel = [0,0]
                show_text('Game Over!', (size//2) - 50, size//2)
                game = True
        if vel!=[0,0]:
            pygame.draw.rect(screen, (0,0,0), (snakeList[-1].old_pos[0], snakeList[-1].old_pos[1], snakeList[-1].dim[0], snakeList[-1].dim[1]))
            pygame.draw.rect(screen, (255,255,255), (snakeList[-1].old_pos[0], snakeList[-1].old_pos[1], snakeList[-1].dim[0]+1, snakeList[-1].dim[1]+1), 1)
        
        if snakeList[0].figure.colliderect(food.figure):
            index+=1
            snakeList.append(Snake(snakeList[index-1].old_pos[0], snakeList[index-1].old_pos[1], index))
            food.pos = [random.randint(0,29) * size//30, random.randint(0,29) * size//30]
            
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN and game == False:
                if event.key == K_UP and vel[1] == 0:
                    vel[1] = -1
                    vel[0] = 0
                elif event.key == K_DOWN and vel[1] == 0:
                    vel[1] = 1
                    vel[0] = 0
                elif event.key == K_LEFT and vel[0] == 0:
                    vel[0] = -1
                    vel[1] = 0
                elif event.key == K_RIGHT and vel[0] == 0:
                    vel[1] = 0
                    vel[0] = 1
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and back.figure.collidepoint(event.pos):
                do = False
        pygame.display.update()
        clock.tick(FR)

def brick():
    ball = Ball([0,0])
    ball.radius = 5
    paddle = Paddle(size//2 - 35, size-30, 70, 20, (255,0,0))
    pad_vel = 0
    do = True
    back = Button('menu', 50,50, (150,150,150), nothing)
    bricks = [Paddle(x*size//20 + 10, 50, size//20, 10, (255,255,0)) for x in range(8)]
    ball.draw()
    score = 0
    while do:
        screen.fill((0,0,0))
        back.draw()
        
        for brick in bricks:
            brick.draw()
            if ball.figure.colliderect(brick.figure):
                if brick.color == (255,255,0):
                    brick.color = (150,150,150)
                    ball.pos[1]+=5
                    ball.vel[1] = 1
                elif brick.color == (150,150,150):
                    brick.color = (0,0,0)
                    ball.pos[1]+=5
                    ball.vel[1] = 1
                    score+=1
                    if score%8 == 0:
                        for brick in bricks:
                            brick.color = (255,255,0)
                #if brick.color!=(0,0,0):
                #ball.vel[1]  = 1
        
        ball.pos[0]+=ball.vel[0]*2
        ball.pos[1]+=int(ball.vel[1])
        ball.vel[1]+=0.75
        ball.draw()
        paddle.pos[0]+=pad_vel*15
        paddle.draw()
        show_text('score: '+str(score), size-200, 50)
        if paddle.figure.colliderect(ball.figure):
            ball.vel[1] = -28.5
            ball.vel[0] = random.randint(-8,8)

        if 0>=ball.pos[0]-ball.radius or size<=ball.pos[0]+ball.radius:
            ball.vel[0]*=-1

        if paddle.pos[0]<=0 or paddle.pos[0]+150>=size:
            pad_vel = 0

        if ball.pos[1]+ball.radius>=size:
            show_text('Game Over!', (size//2) - 50, size//2)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and not paddle.pos[0]<=0:
                    pad_vel = -1
                elif event.key == K_RIGHT and not paddle.pos[0]+150>=size:
                    pad_vel = 1
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    pad_vel = 0
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and back.figure.collidepoint(event.pos):
                do = False
        pygame.display.update()
        clock.tick(FR)


#brick()

def quitter():
    pygame.quit()
    exit()

def menu():
    colors = [(0,255,255),(150,150,0),(255,0,255),(0,0,255),(0,255,0), (255,0,0)]
    games = ['tic tac toe', 'pong (single player)', 'pong (double player)', 'flappy ball', 'snake', 'quit']
    functions = [tic_tac_toe, pong1, pong2, flappy_ball, snake, quitter]
    buttons = []
    for game in range(0,len(games)):
        buttons.append(Button(games[game], 75,150+game*80, colors[game], functions[game]))
    while True:
        screen.fill((0,0,0))
        show_text('''Game City 2''', size//2 - 100, 50)
        show_text('By: Rohan Phadnis', size//2 - 100, 100)
        for button in buttons:
            button.draw()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                for button in buttons:
                    if button.figure.collidepoint(event.pos):
                        button.do()
            elif event.type == QUIT:
                quitter()
        pygame.display.update()
        clock.tick(FR)


menu()
