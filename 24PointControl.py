import pygame,sys,time,random
from cubeCommon import button,printText
import twenty4
c_pos = [(100,50),(250,50),(400,50),(550,50)]
#按钮颜色
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
bright_green = (240,0,0)
bright_red = (0,240,0)
gameExit = False
cards = []
answer = ""
def displayCards(screen,cards):
    for i in range(4):
        img = pygame.image.load("./image/" + cards[i][0] + str(cards[i][1]) + ".jpg").convert()
        screen.blit(img, c_pos[i])

def initCards():
    c1 = int(random.random()*13)+1
    c2 = int(random.random()*13)+1
    c3 = int(random.random()*13)+1
    c4 = int(random.random()*13)+1
    return [("s",c1),("h",c2),("c",c3),("d",c4)]

def newGame(dumy):
    global cards
    cards = initCards()
    displayCards(screen,cards)

def calcAnswer(dumy):
    global answer
    card_data = [item[1] for item in cards]
    r = twenty4.calc24(card_data)
    if r == None:answer = "No Answer!"
    else:answer = twenty4.real(r)

def quitGame(dumy):
    global gameExit
    gameExit = True        
  

def game_loop():
    global gameExit
    clock = pygame.time.Clock()
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        button(screen,u"重开",300,550,60,30,green,bright_green,newGame,"None")
        button(screen,u"答案",400,550,60,30,green,bright_green,calcAnswer,"None")  
        button(screen,u"退出",500,550,60,30,green,bright_green,quitGame,"None")

        pygame.draw.rect(screen,(128,128,128),(300,500,260,30))
        if answer != "":
            printText(screen, answer, "kaiti", 25, 310, 500, black)

        
        clock.tick(30)
        pygame.display.update()
    
        
if __name__ == "__main__":
    global screen
    gameExit = False
    #初始化数据模型
    cards = initCards()

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    #screen = pygame.display.set_mode(pygame.FULLSCREEN)
    screen.fill((0,0,0))
    pygame.display.set_caption("24点")

    displayCards(screen,cards)
   #初始化pygame屏幕
    #进入游戏循环
    game_loop()
    pygame.quit()
  
