#SP3UN Simulator
#Made by Yuxi Qin
#Dec 25, 2019 - Dec 29, 2019
#For the purpose of:
#CodeReach 2019-2020 Volunteer

from pygame import *
from random import *
from math import *
import glob
import time as t

#colours
black = (0,0,0) ##          
white = (255, 255, 255)##
beige = (243, 241, 219) ##
jasperR = (220, 69, 61) ##
solidR =  (185, 7, 27) ##
pastelY = (255, 244, 156) ##
lightSeaG = (39, 171, 178) ##
pastelG = (133, 222, 119) ##
pastelB = (204,229,255)  ## 
pearlAquaB = (116, 203, 204) ##
moonstoneB = (62, 161, 182) ##
prussianB = (0, 49, 83) ##

font.init()                                     #rendering the fonts required      
comic16 = font.SysFont("comicsansms", 16)
comic18 = font.SysFont("comicsansms", 18)
comic36 = font.SysFont("comicsansms", 36)
comic45 = font.SysFont("comicsansms", 45)
comic70 = font.SysFont("comicsansms", 70)
comic130 = font.SysFont("comicsansms", 130)

screenWid, screenHei = 1000,600                 #setting display/screen details
screen = display.set_mode((screenWid,screenHei))
screen.fill(white)
display.set_caption("SPH3UN Simulator")
icon = image.load("mohan.png")
display.set_icon(icon)

page = "menu"
enemyPics = []

eWords = [
        "oh no our functions test",
        "ms can we take up question 25 from the homework",
        "lab report?!",
        "ms you didn't post the homework",
        "ms can we go out carolling",
        "ALL HAIL MOHAN",
        "RED CARPET",
        "ms can we see our kinematics test please",
        "can we watch another Hitler video",
        "can we do trebutchet",
        "can we do rollercoaster",
        "ms if david, daniel, devin, and sat group up again i'm going to drop the class",
        "*APPLAUSE INTENSIFIES*",
        "ms we just had a functions test can we please have another 2 minutes",
        "ok so you're at an intersection",
        "lefties lose the right to go left",
        "can we get a moose plushie from WWF",
        "ms can you please drop the test",
        "*calculating the bmi of tuna cans*",
        "rElAtIvE vEloCIty",
        "WINDING FUNCTION",
        "trust the process",
        "it's okay we're all going to die anyways",
        "THBT believe and you can achieve",
        "wait there's a quiz on wednesday????",
        "we should run for our grade",
        "what is relative velocity",
        "big brainedness",
        "graphing calculators",
        "sONA",
        "ms what's on the test",
        "can we have more questions",
        "who was pythagoras",
        "cOMPONENTS!!",
        "ew cosine law",
        "sig dig xddd",
        "can we have bonus marks",
        "ms please",
        "what is a picometer",
        "have a good day ms",
        "you never taught us this",
        "can i use this board",
        "time was obtained by distance over y component",
        "TBHT mohan physics should be banned under the Geneva Convention",
        "whens the vectors test",
        "jeez im not failing physics - yet",
        "moose chili day",
        "*pulls an all night before the terminal speed lab is due*",
        "steven hawking's bday is also march 14th",
        "i hope i get part marks for part a",
        "acceleration due to gravity means its constantly speeding up",
        "v is proportional to the square root of t",
        "i hate this lab so much",
        "i just wanna hand it in and never see it again",
        "big textbook -p129 #10-12, 16 and p133 #13,16",
        "react if ur down for the carpet",
        "it's only worth 1 years worth of tuition gg",
        "we raised 45 dollars in 2 minutes",
        "sleep is for the weak",
        "there's someone with a shovel outside",
        "ms when are we getting our tests back",
        "class average: 63%",
        "does 0 have any sigdig",
        "0.00 has 3 sigdig right",
        
        ]

pWords = [
        "kinematics part 1",
        "kinematics part 2",
        "density lab",
        "constant acceleration",
        "main 5 formulas",
        "terminal speed lab",
        "trebutchet project",
        "rollercoaster project",
        "instantaneous acceleration",
        "storytime",
        "hitler taking an AP physics exam",
        "slope",
        "SOH CAH TOA",
        "displacement",
        "average velocity",
        "time",
        "vector subtraction",
        "VECTORS",
        "electricity unit",
        "exam",
        "david do the edsby",
        "SPH4UN :))",
        "posted at 11:59pm",
        "scalars",
        "position time graph",
        "velocity",
        "instantaneous velocity",
        "delta d",
        "physics is fun",
        "cosine law",
        "sine law",
        "components smh",
        "components is boring",
        "[N 34 E]",
        "do the textbook questions",
        "whoops that answer was wrong",
        "SIG DIG",
        "no bonus marks lol",
        "hamza is cool",
        "convert from picometers to megabytes",
        "km/s^2",
        "my words are forever behind this whiteboard",
        "gravity is 9.81 m/s^2 dOWN",
        "constant speed",
        "this will be on the test",
        "union strike",
        "i had fun marking these tests",
        "i have such a beautiful question for you guys",
        "these worksheets are my christmas gift to you :))",
        "change in velocity",
        "i met michelle obama <<3",
        "slope is delta y over delta x",
        "who did the textbook questions",
        "who did every single question in the homework?",
        "there are actually a few good textbook questions in there",
        "0 has no sigdig",
        ]

losing_M = [
        "Oof",
        "Yikes, want to try again?",
        "That wasn't so good, was it?",
        "Might want to try again lol",
        "Congrats, you lost",
        "You had one job smh",
        "Yikes",
        "You lose(r)",
        "-1 sigdig :((",
        "no vector symbol, no living",
        "Jerry wouldn't do that",
        "Disappointment ensues",
        ]

for e in glob.glob("enemies/*.png"):
    img = transform.scale(image.load(e), (80,80))
    enemyPics.append(img)

#======== ADDITIONAL FUNCTIONS

def addEnemy(): #spawns an enemy
    x,y = choice( [ (randint(0, screenWid) , choice( [0, screenHei] ) ) ,   #spawns either from top/bottom, or from the sides
                    (choice( [0, screenWid]) , randint(0, screenHei) ) ])
    r = 80
    pic = choice(enemyPics)

    quote = choice( [ choice(eWords), choice(eWords), " "] )
    rect = Rect(x-r, y-r, r*2, r*2)
    enemies.append( [x,y,0,0,20,r,rect,pic, quote] ) #0 -current x, 1 current y,2 x change, 3 y change, 4 health, 5 radius, 6 its position, 7 its image/face, 8 its accompanying quote

#======== PAGES

def menu():     #menu screen, can direct to play (level selector - easy, medium, hard)
    screen.fill(white)
    
    back = transform.scale(image.load("backgrounds/menu.jpg"), (screenWid, screenHei))      #background
    screen.blit(back, (0,0))

    logo = transform.scale(icon, (250, 250))                        #mohan physics icon, but bigger and blurrier
    screen.blit(logo, (650,50))

    sph3un_x , sph3un_y = 50, 25
    sph3un = comic130.render("SPH3UN", True, prussianB)             #title
    simulator = comic70.render("simulator", True, prussianB)
    screen.blit(sph3un, (sph3un_x, sph3un_y))
    screen.blit(simulator, (sph3un_x + 225, sph3un_y + sph3un.get_size()[1]-40))

    cred = comic18.render("Yuxi Qin", True, prussianB)
    screen.blit(cred, (10, 565))
    
    buttons = [Rect(625, 350, 300, 75), Rect(625, 450, 300, 75)]    #main buttons
    vals = ["game", "instructions"]
    text = ["Play", "Instructions"]

    colour = [beige, pearlAquaB, lightSeaG]                         #level difficulty - details
    levels  = ["Easy", "Medium", "Hard"]
    diff = [5, 3, 1]

    global difficulty
    
    while running:
        keys = key.get_pressed()
        for evt in event.get():
            if evt.type == QUIT or keys[K_ESCAPE]:
                return "exit"
            
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()                

        for b,v,t in zip(buttons, vals, text):
            draw.rect(screen, pastelB, b, 0)
            draw.rect(screen, moonstoneB, b, 2)
            txtPic = comic36.render(t, True, prussianB)
            screen.blit(txtPic, ( (b[0] + (b[2]-txtPic.get_size()[0])//2 , (b[1] + (b[3] - txtPic.get_size()[1])//2 ))))
            if b.collidepoint(mx,my):
                draw.rect(screen, prussianB, b, 2)
                if v == "game":
                    for c, lev, d in zip(colour, levels, diff):
                        i = colour.index(c)
                        draw.rect(screen, c, Rect( int(b[0] + i*(b[2]/3)), b[1], int(b[2]/3), b[3]), 0)
                        txtPic = comic18.render(lev, True, prussianB)
                        screen.blit(txtPic, ((int((b[0] + i*(b[2]/3))+((b[2]/3)-txtPic.get_size()[0])/2)), int((b[1] + (b[3]/3))+((b[3]/3)-txtPic.get_size()[1])/2)))
                        draw.rect(screen, prussianB, b, 2)
                        if Rect( int(b[0] + i*(b[2]/3)), b[1], int(b[2]/3), b[3]).collidepoint(mx,my):
                            txtPic = comic18.render(lev, True, black)
                            screen.blit(txtPic, ((int((b[0] + i*(b[2]/3))+((b[2]/3)-txtPic.get_size()[0])/2)), int((b[1] + (b[3]/3))+((b[3]/3)-txtPic.get_size()[1])/2)))
                            if mb[0] == 1:
                                difficulty = diff[i]
                                return v
                else:
                    txtPic = comic36.render(t, True, black)
                    screen.blit(txtPic, ( (b[0] + (b[2]-txtPic.get_size()[0])//2 , (b[1] + (b[3] - txtPic.get_size()[1])//2 ))))
                    if mb[0] == 1:
                        return v
                
        display.flip()

def game():
    running = True
    myClock = time.Clock()
    import time as t

    shieldsLeft = 3
    shieldTime = 0
    shield = False

    slayed = 0

    global player, enemies, pBullets, eBullets, copy, win_loss

    player = [screenWid//2,screenHei//2, 100, 50] #starting x, starting y, health, radius
    enemies = []
    pBullets = []
    eBullets = []

    mohan = transform.scale(image.load("mohan.png"), (player[3]*2, player[3]*2))
    
    win_loss = ""
    
    start = t.time()
    while running:
        keys = key.get_pressed()
        for evt in event.get():
            if evt.type == QUIT:
                return "exit"
            if evt.type == MOUSEBUTTONDOWN:
                if evt.button == 1:                                         #stats when left click is held
                    xDiff,yDiff = mx - player[0], my - player[1]
                    magn = hypot(xDiff, yDiff)
                    x_B , y_B = xDiff/magn , yDiff/magn
                    quote = choice([choice(pWords),choice(pWords), " "])
                    pBullets.append( [player[0], player[1], x_B, y_B, quote] )
                if evt.button == 3:                                         #stats when right click is held
                    shieldTime = t.time()
                    if shieldsLeft > 0:
                        shieldsLeft -= 1
            if keys[K_ESCAPE]:
                return "menu"
            elif keys[K_r]:     #restart
                return "game"
            
        mx,my = mouse.get_pos()                                             #declaring stuff
        mb = mouse.get_pressed()
        
        myClock.tick(150)
        screen.fill(moonstoneB)

        s_propor = 2.5
        playerRect = Rect(player[0]-player[3], player[1]-player[3], player[3]*2, player[3]*2)
        shieldRect = Rect( int(player[0]-player[3]*s_propor) , int(player[1]-player[3]*s_propor), int(player[3]*s_propor*2), int(player[3]*s_propor*2))

        shield = False
        dead = False

        if mb[2] == 1:                                                      #drawing the shield and its ghetto timer
            if t.time() - shieldTime <= 15 and shieldsLeft > 0:
                shield = True
                draw.circle(screen, pastelB, (player[0], player[1]), int(player[3]*s_propor - 20), 2)
            else:
                shieldTime = 0
                if shieldsLeft > 0:
                    shieldsLeft -= 1

        if (t.time() - start) >= difficulty:                                #varies by difficulty, sorta ghetto way to generate but meh
            for e in enemies:
                eBullets.append( [int(e[0]), int(e[1]), e[2], e[3]] )
            addEnemy()
            start = t.time()
            
        for e in enemies:
            xDiff , yDiff = player[0] - e[0] , player[1] - e[1]             #updates and draws each enemy
            magn = hypot(xDiff, yDiff)
            e[2] = xDiff/magn
            e[3] = yDiff/magn
            e[0] += e[2]*0.5
            e[1] += e[3]*0.5
            e[6] = Rect(int(e[0]-e[5]//2), int(e[1]-e[5]//2), e[5], e[5])
            col = [None, black, jasperR, pastelY, pastelG]                  #ex. health of 20 corresponds to index 4 - green

            draw.circle(screen, col[int(e[4]//5)], (int(e[0]),int(e[1])), int(e[5]//2 + 5), 7)
            txtPic = comic16.render(e[8], True, black)
            screen.blit(txtPic, (e[0]-txtPic.get_size()[0]//2,e[1]-txtPic.get_size()[1]*3))
            screen.blit(e[7], (e[6][0], e[6][1]))
            if shield and shieldRect.collidepoint((e[0], e[1])):            #enemy is removed if they hit the shield - doen't count towards slay count
                enemies.remove(e)
            elif playerRect.collidepoint((e[0], e[1])):
                dead = True

            for pB in pBullets:                                             #if a player's bullet hits an enemy
                if e[6].collidepoint((pB[0], pB[1])):
                    e[4] -= 5
                    pBullets.remove(pB)
                    if e[4] == 0:
                        enemies.remove(e)
                        slayed += 1

        for eB in eBullets:                                                 #updating and drawig the bullets
            eB[0] += eB[2]
            eB[1] += eB[3]
            draw.circle(screen, black, (int(eB[0]),int(eB[1])), 5)
            if shield and shieldRect.collidepoint((int(eB[0]), int(eB[1]))):
                eBullets.remove(eB)
            elif playerRect.collidepoint((int(eB[0]), int(eB[1]))):         #changing the bullet's position, and checking if it hit the player
                player[2] -= 5
                eBullets.remove(eB)
                if player[2] == 0:
                    dead = True
                
        for pB in pBullets:
            pB[0] += pB[2] * 1.25
            pB[1] += pB[3] * 1.25
            draw.circle(screen, solidR, (int(pB[0]), int(pB[1])), 5)          #player's bullets are drawn
            txtPic = comic16.render(pB[4], True, solidR)
            screen.blit(txtPic, (pB[0]-txtPic.get_size()[0]//2,pB[1]-txtPic.get_size()[1]*2))
            
        screen.blit(mohan, (player[0]-player[3],player[1]-player[3]))

        if 0<=player[0]<=screenWid and 0<=player[1]<=screenHei:             #the controls - WASD and keys
            if keys[K_LEFT] or keys[K_a] and player[0] - 2 >= 0:
                player[0] -= 2
            if keys[K_RIGHT] or keys[K_d] and player[0] + 2 <= screenWid:
                player[0] += 2
            if keys[K_UP] or keys[K_w] and player[1] - 2 >= 0:
                player[1] -= 2
            if keys[K_DOWN] or keys[K_s] and player[1] + 2 <= screenHei:
                player[1] += 2

        health_bar = Rect(850, 25, 100, 50)                                 #drawing the heatlh bar on the top right, along with the shield stats and the kill count
        draw.rect(screen, white, health_bar, 0)
        draw.rect(screen, black, (health_bar[0] - 2 ,health_bar[1] -2, health_bar[2] +3, health_bar[3] +3), 2)
        
        if 75 <= player[2]:
            colour = pastelG
        elif 50 <= player[2] < 75:
            colour = pastelY
        elif 25 <= player[2] < 50:
            colour = jasperR
        else:
            colour = black
        draw.rect(screen, colour, (health_bar[0], health_bar[1], player[2], health_bar[3]), 0)

        if shield == False:
            shieldTime = t.time()
            if shieldsLeft == 0:
                shieldTime = t.time() - 15

        txtPic = comic16.render(("Shields Left:  " + str(shieldsLeft)), True, black)
        screen.blit(txtPic, (health_bar[0]-txtPic.get_size()[0]-20 , health_bar[1]))
        txtPic = comic16.render(("Shield Time Left: " + str(15-int(t.time()-shieldTime))), True, black)
        screen.blit(txtPic, (health_bar[0]-txtPic.get_size()[0]-20 , health_bar[1]+txtPic.get_size()[1]+5))

        txtPic = comic18.render("Kill Count: " + str(slayed), True, black)
        screen.blit(txtPic, (20,20))

        if dead or slayed == 30:                                            #checking if the player is allowed to see the message yet
            copy = screen.copy()
            copy.set_alpha(125)
            if dead:
                win_loss = choice(losing_M)
            elif slayed == 30:
                win_loss = "You Win!"
            return "message"
        
        display.flip()
        
        
def message():
    screen.fill(white)
    screen.blit(copy, (0,0))
    
    txtPic = comic45.render(win_loss, True, black)
    x,y = (screenWid-txtPic.get_size()[0])//2, ((screenHei - txtPic.get_size()[1])//2 - 50)
    screen.blit(txtPic, (x,y))

    try_again = Rect( (screenWid-650)//2 , y+txtPic.get_size()[1] + 50, 300, 75)
    menu_screen = Rect(try_again[0] + try_again[2] + 50, try_again[1], try_again[2], try_again[3])
    buttons = [try_again, menu_screen]
    text = ["Try Again", "Return to Menu"]
    vals = ["game" , "menu"]

    running = True
    while running:
        keys = key.get_pressed()
        for evt in event.get():
            if evt.type == QUIT:
                return "exit"
            if keys[K_ESCAPE]:
                return "menu"
        
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()

        for b,t,v in zip(buttons, text, vals):
            draw.rect(screen, pastelB, b, 0)
            draw.rect(screen, moonstoneB, (b[0]-2, b[1]-2, b[2]+3, b[3]+3), 2)
            txtPic = comic36.render(t, True, prussianB)
            screen.blit(txtPic, ( (b[0] + (b[2]-txtPic.get_size()[0])//2 , (b[1] + (b[3] - txtPic.get_size()[1])//2 ))))
            if b.collidepoint(mx,my):
                txtPic = comic36.render(t, True, black)
                screen.blit(txtPic, ( (b[0] + (b[2]-txtPic.get_size()[0])//2 , (b[1] + (b[3] - txtPic.get_size()[1])//2 ))))
                draw.rect(screen, prussianB, (b[0]-2, b[1]-2, b[2]+3, b[3]+3), 2)
                if mb[0] == 1:
                    return v
        display.flip()

def instructions():
    instruct_B = transform.scale(image.load("backgrounds/instructions.jpg"), (screenWid, screenHei))
    screen.blit(instruct_B, (0,0))

    menuRect = Rect(350, 60, 300, 75)
    
    running = True
    while running:
        keys = key.get_pressed()
        for evt in event.get():
            if evt.type == QUIT:
                return "exit"
            if keys[K_ESCAPE]:
                return "menu"

        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()

        draw.rect(screen, pastelB, menuRect, 0)
        draw.rect(screen, moonstoneB, menuRect, 2)
        txtPic = comic36.render("Back to Menu", True, prussianB)
        screen.blit(txtPic, ( (menuRect[0] + (menuRect[2]-txtPic.get_size()[0])//2 , (menuRect[1] + (menuRect[3] - txtPic.get_size()[1])//2 ))))

        if menuRect.collidepoint(mx,my):
            txtPic = comic36.render("Back to Menu", True, black)
            screen.blit(txtPic, ( (menuRect[0] + (menuRect[2]-txtPic.get_size()[0])//2 , (menuRect[1] + (menuRect[3] - txtPic.get_size()[1])//2 ))))
            draw.rect(screen, prussianB, menuRect, 2)
            if mb[0] == 1:
                return "menu"
        
        display.flip()
        
running = True
while page != "exit":
    if page == "menu":
        page = menu()
    elif page == "game":
        page = game()
    elif page == "message":
        page = message()
    elif page == "instructions":
        page = instructions()

    display.flip()
quit()
    
    
