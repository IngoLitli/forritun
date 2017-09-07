import pygame
from pygame.locals import *
from random import *
from tkinter import *
from tkinter import ttk

pygame.init()
#WINDOW SETUP CONFIG
winTitle = 'Alien Shooter'
winHeight = 400
winWidth = 600
window = winHeight*winWidth
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((winWidth, winHeight), 0, 32)
pygame.display.set_caption(winTitle)

WHITE = (255, 255, 255)
RED = (255,   0,   0)

#Directions
LEFT = 'LEFT'
RIGHT = 'RIGHT'
UP = 'UP'
DOWN = 'DOWN'
STATIC = 'STATIC'

#Sounds
playerShoot = pygame.mixer.Sound('SOUNDS/P_SHOOT.WAV')
playerHitSound = pygame.mixer.Sound('SOUNDS/PLAYERHIT.WAV')
alienShoot = pygame.mixer.Sound('SOUNDS/A_SHOOT.WAV')
newGameSound = pygame.mixer.Sound('SOUNDS/START_GAME.WAV')
hitSound = pygame.mixer.Sound('SOUNDS/HIT.WAV')
gameOverSound = pygame.mixer.Sound('SOUNDS/GAMEOVER.WAV')
levelUpSound = pygame.mixer.Sound('SOUNDS/LEVELUP.WAV')

#Player
playerSprite = pygame.image.load('sprites/player/player.png')
playerObj = playerSprite.get_rect()
playerHeight = playerObj[3]
playerWidth = playerObj[2]
player_X = (playerWidth/2)
player_Y = winHeight-(playerHeight/2)
playerObj.center = (player_X, player_Y)
playerShooting = 0
playerLives = []

#Player lives
livesSprite = pygame.image.load('sprites/player/lives.png')
livesObj = livesSprite.get_rect()
livesHeight = livesObj[3]+winHeight*0.01
livesWidth = livesObj[2]+winWidth*0.01
lives_X = (livesWidth/2)
lives_Y = winHeight-(livesHeight/2)
livesObj.center = (lives_X, lives_Y)
lives = 3

#Alien
alienSprite = pygame.image.load('sprites/aliens/alien.png')
alienObj = alienSprite.get_rect()
alienHeight = alienObj[3]
alienWidth = alienObj[2]
alien_X = alienWidth/2
alien_Y = 0+(alienHeight/2)
alienObj.center = (alien_X, alien_Y)
aliens = [[alien_X, alien_Y]]
alienDirection = [RIGHT, DOWN]
alienRows = 5
alienCount = alienRows * 11
rowWidth = winWidth-alienWidth*2
alienMove = winWidth-rowWidth
alienMove = int(alienMove/4)
alienMoves = 1
alienSpeed = 75
alienFireRate = 5000
alienShotCounter = 0
alienFireMultiply = 30

#Main Menu
Y_pos = 250
btn_pos = {
    'mid': [winWidth/2, winHeight/2],
    'pos1': [70, Y_pos],
    'pos2': [225, Y_pos],
    'pos3': [380, Y_pos],
    'pos4': [530, Y_pos],
    'pos5': [300, Y_pos]
}
menuSprite = pygame.image.load('sprites/menu/main_menu_bcg.png')
menuObj = menuSprite.get_rect()
menuHeight = menuObj[3]
menuWidth = menuObj[2]
menu_X = winWidth/2
menu_Y = winHeight/2
menuObj.center = (menu_X, menu_Y)

playSprite = pygame.image.load('sprites/menu/buttons/play_btn.png')
playObj = playSprite.get_rect()
playHeight = playObj[3]
playWidth = playObj[2]
play_X = btn_pos['pos1'][0]
play_Y = btn_pos['pos1'][1]
playObj.center = (play_X, play_Y)

difficulitySprite = pygame.image.load('sprites/menu/buttons/difficulity_btn.png')
difficulityObj = difficulitySprite.get_rect()
difficulityHeight = difficulityObj[3]
difficulityWidth = difficulityObj[2]
difficulity_X = btn_pos['pos2'][0]
difficulity_Y = btn_pos['pos2'][1]
difficulityObj.center = (difficulity_X, difficulity_Y)

helpSprite = pygame.image.load('sprites/menu/buttons/help_btn.png')
helpObj = helpSprite.get_rect()
helpHeight = helpObj[3]
helpWidth = helpObj[2]
help_X = btn_pos['pos3'][0]
help_Y = btn_pos['pos3'][1]
helpObj.center = (help_X, help_Y)

scoresSprite = pygame.image.load('sprites/menu/buttons/scores_btn.png')
scoresObj = scoresSprite.get_rect()
scoresHeight = scoresObj[3]
scoresWidth = scoresObj[2]
scores_X = btn_pos['pos4'][0]
scores_Y = btn_pos['pos4'][1]
scoresObj.center = (scores_X, scores_Y)


easySprite = pygame.image.load('sprites/menu/buttons/easy_btn.png')
easyObj = playSprite.get_rect()
easyHeight = easyObj[3]
easyWidth = easyObj[2]
easy_X = btn_pos['pos1'][0]
easy_Y = btn_pos['pos1'][1]
easyObj.center = (easy_X, easy_Y)

normalSprite = pygame.image.load('sprites/menu/buttons/normal_btn.png')
normalObj = normalSprite.get_rect()
normalHeight = normalObj[3]
normalWidth = normalObj[2]
normal_X = btn_pos['pos2'][0]
normal_Y = btn_pos['pos2'][1]
normalObj.center = (normal_X, normal_Y)

hardSprite = pygame.image.load('sprites/menu/buttons/hard_btn.png')
hardObj = hardSprite.get_rect()
hardHeight = hardObj[3]
hardWidth = hardObj[2]
hard_X = btn_pos['pos3'][0]
hard_Y = btn_pos['pos3'][1]
hardObj.center = (hard_X, hard_Y)

menubtnSprite = pygame.image.load('sprites/menu/buttons/menu_btn.png')
menubtnObj = menubtnSprite.get_rect()
menubtnHeight = menubtnObj[3]
menubtnWidth = menubtnObj[2]
menubtn_X = btn_pos['pos4'][0]
menubtn_Y = btn_pos['pos4'][1]
menubtnObj.center = (menubtn_X, menubtn_Y)

borderSprite = pygame.image.load('sprites/menu/buttons/border.png')
borderObj = borderSprite.get_rect()
borderObj.center = (btn_pos['pos2'][0], btn_pos['pos2'][1])

btn_size = playSprite.get_rect()
btnWidth = btn_size[2]
btnHeight = btn_size[3]

howToPlaySprite = pygame.image.load('sprites/menu/how_to_play.png')
howToPlayObj = howToPlaySprite.get_rect()
howToPlayHeight = howToPlayObj[3]
howToPlayWidth = howToPlayObj[2]
howToPlay_X = btn_pos['pos5'][0]
howToPlay_Y = btn_pos['pos5'][1]
howToPlayObj.center = (howToPlay_X, howToPlay_Y)

leaderboardSprite = pygame.image.load('sprites/menu/leaderboard.png')
leaderboardObj = leaderboardSprite.get_rect()
leaderboardHeight = leaderboardObj[3]
leaderboardWidth = leaderboardObj[2]
leaderboard_X = btn_pos['pos5'][0]
leaderboard_Y = btn_pos['pos5'][1]
leaderboardObj.center = (leaderboard_X, leaderboard_Y)

pauseSprite = pygame.image.load('sprites/menu/paused.png')
pauseObj = pauseSprite.get_rect()
pauseHeight = pauseObj[3]
pauseWidth = pauseObj[2]
pause_X = btn_pos['mid'][0]
pause_Y = btn_pos['mid'][1]
pauseObj.center = (pause_X, pause_Y-21.5)


#Shots
shots = []
shotWidth = 6
shotHeight = 12
fireSpeed = 6

#Alien Shots
alienShots = []
alienShotWidth = 8
alienShotHeight = 8
alienFireSpeed = 6

#Power ups
autoShoot = 0
powers = [autoShoot]

#Config
resetGame = 1
respawn = 1
clearedBoard = 0
maxShots = 10
direction = STATIC
timer = 0
tick = 0
overheat = 0
gameover = 0
gameOverSoundPlayed = 0
level = 1
gameWon = 0
playerHit = 0
paused = 0
resume = 0
resuming = 0
cheatsActivated = 0
openConfig = 0
cheatsDisplay = 'Activate Cheats'
cheatsToggled = 0
score = 0
currentPlayerLives = 0
mainMenu = 1
difficulity = 1
difficulityScreen = 0
scoresScreen = 0
helpScreen = 0
hardScore = 'hard'
normScore = 'normal'
easyScore = 'easy'
scoreForKill = 25
scoresSet = 0

File = 'scores.txt'

def addScore(mode):
    global score, scoreForKill
    score += round((scoreForKill*mode)*1.14159265359)

def setScores(scoresFile):
    global hardScore, normScore, easyScore
    savedScores = open(scoresFile)
    scores = []
    for line in savedScores:
        score = line.strip()
        scores.append(score)
    if len(scores) != 3:
        savedScores.close()
        savedScores = open(scoresFile, 'w')
        savedScores.write("%s \n %s \n %s \n" % (0, 0, 0))
        savedScores.close()
        savedScores = open(scoresFile)
        for line in savedScores:
            score = line.strip()
            scores.append(score)
    hardScore = scores[0]
    normScore = scores[1]
    easyScore = scores[2]
    savedScores.close()

def setHighScore(mode, scoresFile):
    global score, easyScore, normScore, hardScore
    savedScores = open(scoresFile, 'w')
    difficulities = {
        0.5: easyScore,
        1: normScore,
        2: hardScore
    }
    if int(difficulities[difficulity]) < score:
        if mode == 0.5:
            savedScores.write("%s \n %s \n %s \n" % (hardScore, normScore, score))
        elif mode == 1:
            savedScores.write("%s \n %s \n %s \n" % (hardScore, score, easyScore))
        elif mode == 2:
            savedScores.write("%s \n %s \n %s \n" % (score, normScore, easyScore))
    else:
        savedScores.write("%s \n %s \n %s \n" % (hardScore, normScore, easyScore))
        savedScores.close()
    savedScores.close()
    setScores(File)

setScores(File)
setScores(File)

def levelUp():
    global level
    global maxShots
    global alienSpeed
    global fireSpeed
    global gameWon
    global alienFireRate
    global difficulity
    levelUpSound.play()
    level += 1
    if maxShots > 1:
        maxShots -= 1
    alienSpeed -= int(alienSpeed*(level/(30*difficulity)))
    fireSpeed += int(fireSpeed*(0.15/difficulity))
    alienFireRate += (alienFireMultiply*difficulity)*alienRows
    alienFireRate -= int(((20*difficulity)*level))
    if level >= 9:
        gameWon = 1

def setFullLife():
    global lives
    global playerLives
    global lives_X
    livesWidth
    for num in range(0,lives):
        playerLives.append(lives_X)
        lives_X += livesWidth

def setMaxShots():
    global maxShots
    global currentMaxShots
    maxShots = int(maxShotsEntered.get())
    currentMaxShots.configure(text=str(int(maxShots)))

def setLives():
    global lives
    global currentLives
    global playerLives
    global lives_X
    global currentPlayerLives
    lives_X = (livesWidth / 2)
    playerLives = []
    lives = currentPlayerLives
    if livesEntered.get() != '':
        lives = int(livesEntered.get())
    if lives <= 0:
        lives = 1
    currentLives.configure(text=str(lives))
    setFullLife()

def setAlienRows():
    global alien_X, alien_Y, alienRows, alienCount, aliens
    global respawn
    if alienRowsEntered.get() != '' and int(alienRowsEntered.get()) <= 11:
        respawn = 1
        alien_X = alienWidth / 2
        alien_Y = 0 + (alienHeight / 2)
        aliens = [[alien_X, alien_Y]]
        alienRows = int(alienRowsEntered.get())
        if alienRows <= 0:
            alienRows = 1
        alienCount = alienRows * 11
        currentalienRows.configure(text=str(alienRows))
        alienCountDisp.configure(text=str(alienCount)+' Aliens on screen every respawn')

def activateCheat():
    global cheatsActivated, cheatsDisplay, cheatsToggled, playerLives, currentPlayerLives
    cheatsToggled = 1
    if cheatsActivated == 0:
        currentPlayerLives = len(playerLives)
        cheatsActivated = 1
        cheatsDisplay = 'Dectivate Cheats'
        actionActiveCheat.configure(text=cheatsDisplay)
    else:
        cheatsActivated = 0
        cheatsDisplay = 'Activate Cheats'
        actionActiveCheat.configure(text=cheatsDisplay)
        setLives()

def newGame():
    #Reset Variables
    global resetGame, score, cheatsToggled, level, tick, difficulity, scoresSet
    global gameover, gameOverSoundPlayed
    global player_X, player_Y, playerObj, playerShooting
    global playerLives, lives, lives_X, lives_Y, shots, maxShots, fireSpeed
    global alien_X, alien_Y, aliens, alienDirection, alienMoves, alienSpeed
    global alienRows, respawn
    global alienFireRate, alienShotCounter, alienFireMultiply
    #New Game Stats Reset
    newGameSound.play()
    resetGame = 1
    score = 0
    cheatsToggled = 0
    level = 1
    tick = 0
    scoresSet = 0

    #Game Over Reset
    gameover = 0
    gameOverSoundPlayed = 0

    #Player Reset
    #Player Position Reset
    player_X = (playerWidth / 2)
    player_Y = winHeight - (playerHeight / 2)
    playerObj.center = (player_X, player_Y)
    playerShooting = 0
    #Player Lives Reset
    playerLives = []
    lives = int(3/difficulity)
    lives_X = (livesWidth / 2)
    lives_Y = winHeight - (livesHeight / 2)
    setFullLife()

    #Player Shots Reset
    shots = []
    maxShots = (10/difficulity)
    fireSpeed = 6

    #Aliens Reset
    #Alien Postion and Direction Reset
    alien_X = alienWidth / 2
    alien_Y = 0 + (alienHeight / 2)
    aliens = [[alien_X, alien_Y]]
    alienDirection = [RIGHT, DOWN]
    alienMoves = 8
    alienSpeed = 75
    alienRows = 5
    respawn = 1
    #Alien Shots Reset
    alienFireRate = (10000/difficulity)
    alienShotCounter = 0
    alienFireMultiply = (30*difficulity)

def removeShot(current):
    hitSound.play()
    shots.remove(current)

def goToMainMenu():
    global mainMenu, scoresScreen, difficulityScreen, helpScreen, gameWon
    global shots, aliens
    shots = []
    aliens = []
    mainMenu = 1
    if gameover == 1 or gameWon == 1:
        scoresScreen = 1
        gameWon = 0
    else:
        scoresScreen = 0
    difficulityScreen = 0
    helpScreen = 0

def restartGame():
    global resetGame, paused
    resetGame = 1
    paused = 0



while True:#Keyrir leikinn
    if cheatsToggled == 1:  #Ef spilarinn kveiti á svindlum
        score = 0           #Þá fer scorið hanns í 0 og breytist ekki


    if openConfig == 1: #Ef spilarinn ýtir á "C" þegar leikurinn er á pásu opnast CONFIG gluggi
        openConfig = 0  #Passar að gluggin opnist ekki strax aftur þegar honum hefur verið lokað
        tk_screen = Tk()#Býr til Tkinter glugga til þess að breyta CONFIG breytum
        tk_screen.title(winTitle+' Config')#Setur nafnið á config glugganum sem "'nafnið á leiknum'+'config'"

        tabControl = ttk.Notebook(tk_screen)
        gameTab = ttk.Frame(tabControl)
        tabControl.add(gameTab, text="Game")

        # Activate Cheat-mode
        ticksDisp = Label(gameTab, text='Game Ticks = '+str(tick))
        ticksDisp.grid(column=0, row=0, columnspan = 2, sticky='ew')
        actionActiveCheat = Button(gameTab, text=cheatsDisplay, command=activateCheat)
        actionActiveCheat.grid(column=0, row=8, columnspan=2, sticky='ew')

        # Activate Cheat-mode
        actionReset = Button(gameTab, text='RESET GAME', command=restartGame)
        actionReset.grid(column=2, row=8, columnspan=2, sticky='ew')

        tabPlayer = ttk.Frame(tabControl)
        tabControl.add(tabPlayer, text='Player')

        #Change maxShots in Config
        enterMaxShots = Label(tabPlayer, text='Max shots: ')
        enterMaxShots.grid(column=0, row=0, sticky='e')
        maxShotsEntered = Entry(tabPlayer, width=8, textvariable=int(maxShots))
        maxShotsEntered.grid(column=1, row=0, sticky='ew')
        currentMaxShots = Label(tabPlayer, text=str(maxShots))
        currentMaxShots.grid(column=2,row=0, sticky='ew')
        action = Button(tabPlayer, text="Set MaxShots", command=setMaxShots)
        action.grid(column=3, row=0, sticky ='w')

        # Change lives in Config
        enterLives = Label(tabPlayer, text='Lives: ')
        enterLives.grid(column=0, row=1, sticky='e')
        livesEntered = Entry(tabPlayer, width=8, textvariable=int(lives))
        livesEntered.grid(column=1, row=1, sticky='ew')
        currentLives = Label(tabPlayer, text=str(lives))
        currentLives.grid(column=2, row=1, sticky='ew')
        action = Button(tabPlayer, text="Set Lives", command=setLives)
        action.grid(column=3, row=1, sticky='w')

        tabAlien = ttk.Frame(tabControl)
        tabControl.add(tabAlien, text='Aliens')

        # Change alienRows in Config
        alienRowsDisp = Label(tabAlien, text='Alien Rows: ')
        alienRowsDisp.grid(column=0, row=0, sticky='e')
        alienCountDisp = Label(tabAlien, text=str(alienCount)+' Aliens on screen every respawn')
        alienCountDisp.grid(column=4, row=0, columnspan = 2, sticky='e')
        alienRowsEntered = Entry(tabAlien, width=8, textvariable=int(alienRows))
        alienRowsEntered.grid(column=1, row=0, sticky='ew')
        currentalienRows = Label(tabAlien, text=str(alienRows))
        currentalienRows.grid(column=2, row=0, sticky='ew')
        action = Button(tabAlien, text="Set Alien Rows", command=setAlienRows)
        action.grid(column=3, row=0, sticky='w')


        tabControl.grid(column=0, row=0, padx=5, pady=5)
        tk_screen.mainloop()
    #Tkinter kóðinn endar hér


    tick += 1 #Þetta virkar eins og klukka fyrir leikinn án þess að breyta FPS
    #Ef leikurinn er settur á pásu keyrist þessi kóði
    if mainMenu == 1:
        mousePostition = pygame.mouse.get_pos()
        gameover = 0
        screen.blit(menuSprite, menuObj)
        maxShots = 1
        screen.blit(playerSprite, playerObj)
        playerObj.center = (player_X, player_Y)
        for shot in shots:
            if shot[0] in range(int(btn_pos['pos1'][0] - btnWidth / 2), int(btn_pos['pos1'][0] + btnWidth / 2)) \
                    and shot[1] in range(int(btn_pos['pos1'][1] - btnHeight / 2), int(btn_pos['pos1'][1] + btnHeight / 2)):
                if (difficulityScreen == 0) or (scoresScreen == 1) or (helpScreen == 1):
                    removeShot(shot)
                    mainMenu = 0
                    newGame()
                elif (difficulityScreen == 1) and (scoresScreen == 0) and (helpScreen == 0):
                    removeShot(shot)
                    if difficulity == 0.5:
                        mainMenu = 0
                        newGame()
                    difficulity = 0.5
            elif shot[0] in range(int(btn_pos['pos2'][0] - btnWidth / 2), int(btn_pos['pos2'][0] + btnWidth / 2)) \
                    and shot[1] in range(int(btn_pos['pos2'][1] - btnHeight / 2), int(btn_pos['pos2'][1] + btnHeight / 2)):
                if (difficulityScreen == 0) and (scoresScreen == 0) and (helpScreen == 0):
                    removeShot(shot)
                    difficulityScreen = 1
                elif (difficulityScreen == 1) and (scoresScreen == 0) and (helpScreen == 0):
                    removeShot(shot)
                    if difficulity == 1:
                        mainMenu = 0
                        newGame()
                    difficulity = 1
            elif shot[0] in range(int(btn_pos['pos3'][0] - btnWidth / 2), int(btn_pos['pos3'][0] + btnWidth / 2)) \
                    and shot[1] in range(int(btn_pos['pos3'][1] - btnHeight / 2),int(btn_pos['pos3'][1] + btnHeight / 2)):
                if (difficulityScreen == 0) and (scoresScreen == 0) and (helpScreen == 0):
                    removeShot(shot)
                    helpScreen = 1
                elif (difficulityScreen == 1) and (scoresScreen == 0) and (helpScreen == 0):
                    removeShot(shot)
                    if difficulity == 2:
                        mainMenu = 0
                        newGame()
                    difficulity = 2
            elif shot[0] in range(int(btn_pos['pos4'][0] - btnWidth / 2), int(btn_pos['pos4'][0] + btnWidth / 2)) \
                 and shot[1] in range(int(btn_pos['pos4'][1] - btnHeight / 2),int(btn_pos['pos4'][1] + btnHeight / 2)):
                if (difficulityScreen == 0) and (scoresScreen == 0) and (helpScreen == 0):
                    removeShot(shot)
                    scoresScreen = 1
                elif (difficulityScreen == 1) or (scoresScreen == 1) or (helpScreen == 1):
                    removeShot(shot)
                    goToMainMenu()
            if shot[1] > 0:
                shot[1] -= fireSpeed
            else:
                playerHitSound.play()
                shots.remove(shot)
            pygame.draw.rect(screen, RED, (shot[0], shot[1], shot[2], shot[3]))

        if (pygame.mouse.get_pressed())[0]:
            if len(shots) < maxShots:
                shots.append([player_X, player_Y, shotWidth, shotHeight])
        if (difficulityScreen == 0) and (scoresScreen == 0) and (helpScreen == 0):
            if 310 < mousePostition[0] < winWidth-160 and 200 < mousePostition[1] < 300:
                player_X = mousePostition[0]
        if (direction == LEFT) and playerObj[0] >= 0:
            player_X -= 6
        elif (direction == RIGHT) and playerObj[0] <= winWidth - playerObj[2]:
            player_X += 6

        if (difficulityScreen == 0) and (scoresScreen == 0) and (helpScreen == 0):
            screen.blit(playSprite, playObj)
            screen.blit(difficulitySprite, difficulityObj)
            screen.blit(helpSprite, helpObj)
            screen.blit(scoresSprite, scoresObj)
        elif (difficulityScreen == 1) and (scoresScreen == 0) and (helpScreen == 0):
            if difficulity == 1:
                borderObj.center = (btn_pos['pos2'][0], btn_pos['pos2'][1])
            elif difficulity == 0.5:
                borderObj.center = (btn_pos['pos1'][0], btn_pos['pos1'][1])
            elif difficulity == 2:
                borderObj.center = (btn_pos['pos3'][0], btn_pos['pos3'][1])
            screen.blit(borderSprite, borderObj)
            screen.blit(easySprite, easyObj)
            screen.blit(normalSprite, normalObj)
            screen.blit(hardSprite, hardObj)
            screen.blit(menubtnSprite, menubtnObj)
        elif (difficulityScreen == 0) and (scoresScreen == 1) and (helpScreen == 0):
            hardScoreDispl = pygame.font.Font('freesansbold.ttf', int((scoresWidth + scoresHeight) / 6))
            hardScoreSurfObj = hardScoreDispl.render(hardScore, True, (255, 0, 0), (255, 255, 255))
            hardScoreRectObj = hardScoreSurfObj.get_rect()
            hardScoreRectObj.center = (winWidth/2, scores_Y-hardScoreRectObj[3])

            normScoreDispl = pygame.font.Font('freesansbold.ttf', int((scoresWidth + scoresHeight) / 6))
            normScoreSurfObj = normScoreDispl.render(normScore, True, (255, 255, 0), (255, 255, 255))
            normScoreRectObj = normScoreSurfObj.get_rect()
            normScoreRectObj.center = (winWidth / 2, scores_Y+10)

            easyScoreDispl = pygame.font.Font('freesansbold.ttf', int((scoresWidth + scoresHeight) / 6))
            easyScoreSurfObj = easyScoreDispl.render(easyScore, True, (0, 255, 0), (255, 255, 255))
            easyScoreRectObj = easyScoreSurfObj.get_rect()
            easyScoreRectObj.center = (winWidth / 2, scores_Y + easyScoreRectObj[3]+20)

            screen.blit(playSprite, playObj)
            screen.blit(leaderboardSprite, leaderboardObj)
            screen.blit(hardScoreSurfObj, hardScoreRectObj)
            screen.blit(normScoreSurfObj, normScoreRectObj)
            screen.blit(easyScoreSurfObj, easyScoreRectObj)
            screen.blit(menubtnSprite, menubtnObj)
        elif (difficulityScreen == 0) and (scoresScreen == 0) and (helpScreen == 1):
            screen.blit(playSprite, playObj)
            screen.blit(howToPlaySprite, howToPlayObj)
            screen.blit(menubtnSprite, menubtnObj)

    elif paused == 1:
        if resetGame:
            paused = 0
        elif resume == 0 and resuming == 0:#Notandinn er ekki búinn að ýta aftur á ESC eða P þessi if setning
            screen.blit(pauseSprite, pauseObj)  #| Birtir "PAUSE" merkið
        else: #Ef notandinn hefur ýtt aftur á ESC eða P þá: Birtist "RESUME IN: ###"
            if tick % 50 == 0:                            # ### stendur fyrir breytu sem er bið-tíminn fyrir leikinn að
                if resume > 0:                            # byrja afur, sem minnkar um einn (50 ticks)
                    resuming = 1
                    resume += -1
                    resumeDispl = pygame.font.Font('freesansbold.ttf', int((winWidth + winHeight) / 16))        #//
                    resumeObj = resumeDispl.render('RESUME IN: '+str(resume), True, (255, 255, 255), (0, 0, 0)) #/
                    resumeRectObj = resumeObj.get_rect()
                    resumeRectObj[0] = pauseHeight                                                              #|Birtit "RESUME"
                    resumeRectObj[1] = pauseWidth
                    resumeRectObj.center = (winWidth / 2, winHeight / 2)                                        #\
                    screen.blit(resumeObj, resumeRectObj)                                                       #\\
                else:#Þegar resume er komið niður í 0,
                    paused = 0#lives = int(livesEntered.get())


    elif gameWon == 1:#Ef notandinn vann leikinn, þá keyrirst þessi kóði
        if scoresSet == 0:
            currentTick = tick
            setHighScore(difficulity, File)
            #setScores(File)
            scoresSet = 1
        #screen.fill((255, 255, 255))
        hiScoreDispl = pygame.font.Font('freesansbold.ttf', int((winWidth + winHeight) / 16))
        if difficulity == 0.5:
            hiScoreSurfObj = hiScoreDispl.render('High Score: ' + str(easyScore), True, (0, 255, 0), (0, 0, 0))
        elif difficulity == 1:
            hiScoreSurfObj = hiScoreDispl.render('High Score: ' + str(normScore), True, (255, 255, 0), (0, 0, 0))
        elif difficulity == 2:
            hiScoreSurfObj = hiScoreDispl.render('High Score: ' + str(hardScore), True, (255, 0, 0), (0, 0, 0))
        hiScoreRectObj = hiScoreSurfObj.get_rect()
        hiScoreRectObj.center = (winWidth / 2, winHeight / 1.5)

        overDisplay = 'You Won!'
        if gameover == 1:
            overDisplay = 'GAMEOVER'
        youWonDispl = pygame.font.Font('freesansbold.ttf', int((winWidth + winHeight) / 16))
        youWonSurfObj = youWonDispl.render((overDisplay), True, (255, 255, 255), (0, 0, 0))
        youWonRectObj = youWonSurfObj.get_rect()
        youWonRectObj.center = (winWidth / 2, (winHeight / 1.5)-hiScoreRectObj[3])

        yourScoreDispl = pygame.font.Font('freesansbold.ttf', int((winWidth + winHeight) / 16))
        yourScoreSurfObj = yourScoreDispl.render(('Your Score: '+str(score)), True, (255, 255, 255), (0, 0, 0))
        yourScoreRectObj = yourScoreSurfObj.get_rect()
        yourScoreRectObj.center = (winWidth / 2, (winHeight / 1.5) + hiScoreRectObj[3])

        screen.blit(menuSprite, menuObj)
        screen.blit(hiScoreSurfObj, hiScoreRectObj)
        screen.blit(youWonSurfObj, youWonRectObj)
        screen.blit(yourScoreSurfObj, yourScoreRectObj)
        if(tick-currentTick == 100):
            goToMainMenu()
            scoresScreen = 1

    elif gameover != 1:#Ef notandinn er ekki búinn að tapa keyrist þessi kóði
        resume = 0
        resuming = 0

        #Svindlið
        if cheatsActivated == 1:#Ef kevikt er á svindlum
            cheatsToggled = 1   #Slekkur á stigagjöf fyrir spilarann
            autoShoot = 1       #Virkjar þaða að spilari getur haldið inni til þess að skjóta
            maxShots = 50       #Setur hámarks skota fjölda upp
            playerLives = [livesWidth / 2, livesWidth / 2] #Lætur endalaust af lífi í spilarann
            if playerShooting == 1:         #Athugar hvort spilari haldi inni skot takka
                if len(shots) < maxShots:   #Athugar hvort fjöldi skota á skjá nái ekki hámarksfjölda skota
                            #Ef fjöldi skota er ekki í hámarki, skýtur skipið einu skoti
                    shots.append([int(player_X - (shotWidth / 2) - 1), int((player_Y - shotHeight)), shotWidth, shotHeight])
                    playerShoot.play()  #Spilar skothljóð fyrir spilara skot

        if resetGame:   #Ef spilari velur að restarta leiknum keyrirst þetta
            newGame()   #Keyrir fallið newGame()
            resetGame = 0

        if len(playerLives) <= 0:#Ef spilari er með meira en eða jafnt og 0 líf tapar hann
            gameover = 1         #Lætur spilarann tapa

        if len(aliens) == 0:    #Athugar hvort það séu geimverur eftir á skjánum
            respawn = 1         #Setur respawn breytuna = True
            clearedBoard = 1    #Setur clearedBoard breytuna = True
            shots = []          #Eyðir öllum skotum frá spilara af skjánum
            alien_X = alienWidth / 2            # /
            alien_Y = 0+(alienHeight/2)         #| Staðsetur fyrstu geimveruna á réttann stað
            aliens.append([alien_X, alien_Y])   # \

        if respawn == 1:#Athugar hvort geiverurnar eigi að koma aftur
            alienDirection[0] = RIGHT   #/ Setur hreyfingar átt geimveranna til hægri
            alienMoves = 1              #\  og lætur þær byrja að hreyfast á réttum stað
            alien_X = alienWidth / 2       #/ Finnur rétt X- og Y-hnit
            alien_Y = 0 + (alienHeight / 2)#\  fyrir næstu geimveru sem á að birtast
            for num in range(1, alienCount):        #///
                if num % 11 != 0:                   #// Fyrir hverja geimveru sem á að birtast hækkar breytan "num"
                    alien_X += alienWidth           #/      ef "num" deilt með 11 skilar engum afgang þá bætist við
                else:                               #|      X-hnitið á geimverunni, breiddin á geimverunni, annars
                    alien_Y = alien_Y + alienHeight #\      bætist við Y-hnitið, hæðin á geimverunni, og X-hnitið
                    alien_X = alienWidth / 2        #\\     fer aftur alveg vinstramegin á skjáinn.
                aliens.append([alien_X, alien_Y])   #\\\Þegar þessu er lokið bætist geimveran í listann af geimverunum
            respawn = 0#Setur respawn breytuna í 0

        if clearedBoard == 1:#Athugar hvort borðið sé tómt
            levelUp()   #Ef borðið er tómt, þá keyrirst fallið levelUp() og spilarinn fer upp um borð
            clearedBoard = 0#Setur breytuna aftur í False



        screen.fill((0, 0, 0))
        playerObj.center = (player_X, player_Y)
        for shot in shots:
            for alien in aliens:
                if shot[0] in range(int(alien[0]-alienWidth/2),int(alien[0]+alienWidth/2)) \
                        and shot[1] in range(int(alien[1]-alienHeight/2),int(alien[1]+alienHeight/2)):
                    addScore(difficulity)
                    hitSound.play()
                    alienShotCounter += 1
                    aliens.remove(alien)
                    shots.remove(shot)
                    if alienShotCounter == 11:
                        alienFireRate -= (alienFireMultiply*difficulity)
                        alienShotCounter = 0
            if shot[1] > 0:
                shot[1] -= fireSpeed
            else:
                playerHitSound.play()
                shots.remove(shot)
            pygame.draw.rect(screen, RED, (shot[0], shot[1], shot[2], shot[3]))


        for alien in aliens:
            if (tick % alienSpeed) == 0:
                if alienMoves == 0 or alienMoves == 4:
                    alien[1] += alienHeight
                else:
                    if (alienDirection[0] == LEFT):
                        alien[0] -= alienMove
                    elif (alienDirection[0] == RIGHT):
                        alien[0] += alienMove
            if alien[1] >= winHeight:
                gameover = 1
            alien_X = alien[0]
            alien_Y = alien[1]
            alienObj.center = (alien_X, alien_Y)
            screen.blit(alienSprite, alienObj)
            randomNumber = randint(0,int(alienFireRate))
            if randomNumber == 1:
                alienShoot.play()
                alienShots.append(
                    [int(alien[0] - (alienShotWidth / 2) - 1), int((alien[1] - alienShotHeight)), alienShotWidth, alienShotHeight])
        if (tick % alienSpeed) == 0:
            alienMoves += 1
            if alienMoves in range(1,3):
                alienDirection[0] = RIGHT
            elif alienMoves in range(5,7):
                alienDirection[0] = LEFT
            if alienMoves == 8:
                alienMoves = 0

        for a_shot in alienShots:
            if a_shot[0] in range(int(player_X - playerWidth / 2), int(player_X + playerWidth / 2)) and a_shot[1] in range(
                    int(player_Y - alienHeight / 2), int(player_Y + playerHeight / 2)):
                playerHit = 1
                alienShots.remove(a_shot)
            if a_shot[1] < winHeight:
                a_shot[1] += alienFireSpeed
            else:
                hitSound.play()
                alienShots.remove(a_shot)
            pygame.draw.rect(screen, RED, (a_shot[0], a_shot[1], a_shot[2], a_shot[3]))
        if playerHit == 1:
            hitSound.play()
            playerLives.remove(playerLives[len(playerLives)-1])
            playerHit = 0


        for life in playerLives:
            screen.blit(livesSprite, livesObj)
            livesObj.center = ((winWidth-life), lives_Y-winHeight*0.01)

        screen.blit(playerSprite, playerObj)
        if (direction == LEFT) and playerObj[0] != 0:
            player_X -= 2
        elif (direction == RIGHT)and playerObj[0] != winWidth-playerObj[2]:
            player_X += 2


    else:#Ef notandinn er búinn að tapa keyrist þessi kóði
        setHighScore(difficulity, File)
        #setScores(File)
        if gameOverSoundPlayed == 0:
            gameOverSound.play()
            gameOverSoundPlayed = 1
        gameWon = 1
        #goToMainMenu()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_LEFT or event.key == K_a) and playerObj[0] >= 0:
                direction = LEFT
            elif (event.key == K_RIGHT or event.key == K_d)and playerObj[0] <= winWidth:
                direction = RIGHT
            elif (event.key == K_SPACE or event.key == K_UP or event.key == K_w) and (gameover != 1 and paused != 1) or (mainMenu == 1):
                if autoShoot == 1:
                    playerShooting = 1
                if len(shots) < maxShots:
                    shots.append(
                        [int(player_X - (shotWidth / 2) - 1), int((player_Y - shotHeight)), shotWidth, shotHeight])
                    playerShoot.play()
            elif (event.key == K_BACKSPACE):
                cheatsActivated = 1
            elif (event.key == K_ESCAPE):
                if paused == 1:
                    goToMainMenu()
            elif (event.key == K_p):
                if paused == 0:
                    paused = 1
                elif paused == 1:
                    resume = 4
            elif (event.key == K_c) and paused == 1:
                openConfig = 1

        elif event.type == KEYUP:
            if (event.key == K_LEFT or event.key == K_a):
                direction = STATIC
            elif (event.key == K_RIGHT or event.key == K_d):
                direction = STATIC
            elif (event.key == K_SPACE or event.key == K_UP or event.key == K_w):
                playerShooting = 0
    pygame.display.update()
    fpsClock.tick(FPS)