import pygame, sys
from pygame.locals import *
from random import *


pygame.init()

# WINDOW SETUP CONFIG
winTitle = 'Verkefni ###'
winHeight = 500
winWidth = 600
window = winHeight * winWidth
FPS = 100  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((winWidth, winHeight), 0, 32)
pygame.display.set_caption(winTitle)


LEFT = False
RIGHT = False
UP = False
DOWN = False

skot_breidd = 5
skot_haed = 10
skot_X = winWidth/2
skot_Y = winHeight-skot_haed
skotHradi = 2

morgSkot = []


while True:
    screen.fill((0, 0, 0))
    for skot in morgSkot:
        pygame.draw.rect(screen, (255, 255, 255), skot, 0)
        if skot[1] > 0:
            skot[1] -= skotHradi
        else:
            morgSkot.remove(skot)

    '''
        NEÐST Í Kóðanum:

            if (event.key == K_UP or event.key == K_w):
                morgSkot.append([skot_X, skot_Y, skot_breidd, skot_haed])

            Þegar þú ýtir á skot takkann þá bætast við upplýsingar um skotið í listann "morgSkot = []" þannig að listinn
            verður þá að ------> morgSkot = [[skot_X, skot_Y, skot_breidd, skot_haed]]
            eða í þessu tilfelli morgSkot = [[250, 590, 5, 10]] og svo ef það er ýtt aftur á takkann verður listinnn
            svona -------------> morgSkot = [[250, 590, 5, 10], [250, 590, 5, 10]...] en þar sem for-loopan er í gangi
            verður listinn ekki svona.

            Vegna þess að for-loopan tekur hvert skot úr listanum og athugar hvort að
            skot[1] => [skot_X, (!skot_Y!), skot_breidd, skot_haed] og ef skot_Y er ekki minna en 0 þá minnkar
            for-loopan skot_Y um skotHrada í þessu tilfelli 10, en ef skot_Y er minna en 0 eyðist skotið úr listanum.
            
            Dæmi um það sem er að gerast í loopunni ($$LOOP$$ táknar eina loop-u):
            morgSkot = []
            $$LOOP$$ [ÝTT Á SKOT TAKKANN]
            morgSkot = [[250, 590, 5, 10]]
            $$LOOP$$
            morgSkot = [[250, 580, 5, 10]]
            $$LOOP$$
            morgSkot = [[250, 570, 5, 10]]
            $$LOOP$$ X55 [ÝTT Á SKOT TAKKANN]
            morgSkot = [[250, 20, 5, 10], [250, 590, 5, 10]]
            $$LOOP$$
            morgSkot = [[250, 10, 5, 10], [250, 570, 5, 10]]
            $$LOOP$$
            morgSkot = [**EYDDIST ÚT**, [250, 560, 5, 10]]
            $$LOOP$$
            morgSkot = [[250, 550, 5, 10]]
        '''



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_UP or event.key == K_w):
                morgSkot.append([skot_X, skot_Y, skot_breidd, skot_haed])


    pygame.display.update()
    fpsClock.tick(FPS)
