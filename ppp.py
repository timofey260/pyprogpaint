from os import system
import codecs
import pygame
from time import sleep
file = input("filename: ")
fname = file + ".ppp"
prg = codecs.open(fname, "r+", encoding="ansi").readlines()
st = 0
w = int(prg[0])
h = int(prg[1])
capt = prg[2]
gameDisplay = pygame.display.set_mode((w,h))
pygame.display.set_caption(capt)
pygame.init()
pygame.font.init()
system('cls||clear')
def mts(text, x, y, col1, col2, col3, size):
    font = pygame.font.SysFont("arial", size)
    screen_text = font.render(text, True, [col1, col2, col3], None)
    gameDisplay.blit(screen_text, [x, y])


def error(index):
    if index == 1:
        print("Error: argument must be int")
    input()
    exit()

def func(indx, func):
    #pygame.display.update()
    if indx == 0:
        ind = ''
    else:
        ind = ' ' * indx
    text = func.split()
    try:
        token = text[0]
    except IndexError:
        return
    try:
        arg1 = text[1]
    except:
        pass
    # tokens
    if token == ind:
        pass
    if token == ind + 'fill':
        col = (int(text[1]), int(text[2]), int(text[3]))
        gameDisplay.fill(col)
    if token == ind + "wait":
        try:
            int(arg1)
        except ValueError:
            error(1)
        sleep(int(arg1))
    if token == ind + "print":
        print(arg1)
    if token == ind + "stroke":
        try:
            int(arg1)
        except ValueError:
            error(1)
        ust = prg[int(arg1)].split()
        print(ust[0])
    #rect
    if token == ind + "rect":
        try:
            col = (int(text[1]), int(text[2]), int(text[3]))
            rect = (int(text[4]), int(text[5]), int(text[6]), int(text[7]))
            width = int(text[8])
        except ValueError:
            error(1)
        pygame.draw.rect(gameDisplay, col, rect, width=width)
    if token == ind + "sqr":
        try:
            col = (int(text[1]), int(text[2]), int(text[3]))
            rect = (int(text[4]), int(text[5]), int(text[6]), int(text[6]))
            width = int(text[7])
        except ValueError:
            error(1)
        pygame.draw.rect(gameDisplay, col, rect, width=width)
    if token == ind + 'cir':
        col = (int(text[1]), int(text[2]), int(text[3]))
        center = (int(text[4]), int(text[5]))
        width = int(text[6])
        rad = int(text[7])
        c1 = True
        c2 = True
        c3 = True
        c4 = True
        try:
            if text[8] == 'false':
                c1 = False
            if text[8] == 'true':
                c1 = True
            if text[9] == 'false':
                c2 = False
            if text[9] == 'true':
                c2 = True
            if text[10] == 'false':
                c3 = False
            if text[10] == 'true':
                c3 = True
            if text[11] == 'false':
                c4 = False
            if text[11] == 'true':
                c4 = True

        except IndexError:
            pass
        pygame.draw.circle(gameDisplay, col, center, rad, width, c1, c2, c3, c4)
    if token == "poly":
        col = (int(text[1]), int(text[2]), int(text[3]))
        all = prg[int(text[4]) - 1].split()
        try:
            x = len(all) / 2
            int(x)
        except:
            pass
        num = 0
        points = []
        for a in all:
            if num == 0:
                var1 = []
                var1.append(int(a))
                var1 = tuple(var1)
                num = 1
            elif num == 1:
                var1 = list(var1)
                var1.append(int(a))
                num = 0
                var1 = tuple(var1)
                points.append(var1)
        width = int(text[5])
        pygame.draw.polygon(gameDisplay, col, points, width)


    if token == ind + 'mts':
        textd = text[1]
        x = text[2]
        y = text[3]
        col1 = text[4]
        col2 = text[5]
        col3 = text[6]
        sca = text[7]
        try:
            x = int(x)
            y = int(y)
            col1 = int(col1)
            col2 = int(col2)
            col3 = int(col3)
            sca = int(sca)
        except ValueError:
            error(1)

        mts(textd, x, y, col1, col2, col3, sca)
    if token == 'line':
        col = (int(text[1]), int(text[2]), int(text[3]))
        sp = (int(text[4]), int(text[5]))
        ep = (int(text[6]), int(text[7]))
        pygame.draw.line(gameDisplay, col, sp, ep, int(text[8]))
run = True
while run:
    for t in prg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        func(0, t)
        st = st + 1
        pygame.display.flip()
    sleep(1)

pygame.quit()
